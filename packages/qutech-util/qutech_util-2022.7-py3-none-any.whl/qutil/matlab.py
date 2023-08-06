"""This module contains utility functions that help interacting with matlab and matlab files"""
import itertools
import warnings
import os
from typing import Tuple, Sequence, Union, Any

import numpy
import hdf5storage
import pandas
import json

import qutil.caching

try:
    import matlab.engine
except (ImportError, OSError):
    warnings.warn("Matlab engine  interface not installed. "
                  "Some functionality requires using MATLAB directly.\n"
                  "Navigate to 'C:\Program Files\MATLAB\R2020b\extern\engines\python' and call 'python setup.py install'")
    matlab = None

__all_ = ['load_special_measure_scan', 'cached_load_mat_file', 'special_measure_to_dataframe',
          'load_special_measure_with_matlab_engine', 'mlarray_to_numpy']


def mlarray_to_numpy(d) -> numpy.ndarray:
    """Converts a mlarray (matlab engine array) into a readable numpy array in an efficient manner if possible.

    Calling np.asarray(your_matlab_array) is very slow because mlarray does not implement the buffer protocol.
    This function utilizes the internal private representation if possible
    """
    try:
        data = d._data
        strides = d._strides
        shape = d._size
        item_size = data.itemsize

        return numpy.lib.stride_tricks.as_strided(
            data,
            shape=shape, strides=[s * item_size for s in strides], writeable=False
        )

    except AttributeError:
        # slow fallback
        return numpy.asarray(d)


class ModuleEngineWrapper:
    """The purpose of this class is to be a default argument for engine requiring functions different from None.
     This is the least stupid default interface I came up with (Simon)."""
    ENGINE = None

    @classmethod
    def get_engine(cls):
        if cls.ENGINE is None:
            cls.ENGINE = matlab.engine.connect_matlab()
        return cls.ENGINE

    @staticmethod
    def to_engine(obj) -> 'matlab.engine.MatlabEngine':
        if isinstance(obj, str):
            return matlab.engine.connect_matlab(name=obj)
        elif obj is None:
            print('Connecting to (and maybe starting) MATLAB')
            return matlab.engine.connect_matlab()
        elif isinstance(obj, matlab.engine.MatlabEngine):
            return obj
        else:
            return obj.get_engine()


def read_table(engine, path: str) -> pandas.DataFrame:
    """Read a table from the given path in the engine namespace and return it
    as a pandas.DataFrame."""
    row_names = engine.eval(f'{path}.Properties.RowNames')
    col_names = engine.eval(f'{path}.Properties.VariableNames')
    values = engine.eval(f'{path}.Variables')
    return pandas.DataFrame(numpy.array(values),
                            columns=col_names, index=row_names)


def load_data_from_matlab_figure(file_name: os.PathLike,
                                 engine=ModuleEngineWrapper):
    """
    Loads data saved in matlab figures

    Args:
        file_name: fig file to load
        engine:
            None, str -> passed to matlab.engine.connect_matlab()
            () -> Use module instance
            MatlabEngine -> used directly

    Returns:
        fig_data
        user_data

    """
    engine = ModuleEngineWrapper.to_engine(engine)

    engine.eval(f"fig = openfig('{file_name}', 'invisible');", nargout=0)
    engine.eval(f"plot = fig.Children;", nargout=0)
    n_plots = int(engine.eval("length(plot)", nargout=1))

    fig_data = []

    for i in range(n_plots):
        n_children = int(engine.eval(f"length(plot({i+1}).Children)", nargout=1))
        if n_children > 0:
            title = engine.eval(f"plot({i+1}).Title.String", nargout=1)
            if isinstance(title, list):
                title = [str(e) for e in title if len(e)]
            else:
                title = str(title) if len(title) else ''

            plot_data = {
                'title': title,
                'subtitle': engine.eval(f"plot({i+1}).Subtitle.String", nargout=1),
                'XLim': mlarray_to_numpy(engine.eval(f"plot({i+1}).XLim", nargout=1)).astype(float).reshape((-1)),
                'YLim': mlarray_to_numpy(engine.eval(f"plot({i+1}).YLim", nargout=1)).astype(float).reshape((-1)),
                'XLabel': str(engine.eval(f"plot({i+1}).XLabel.String", nargout=1)),
                'YLabel': str(engine.eval(f"plot({i+1}).YLabel.String", nargout=1)),
                'XScale': str(engine.eval(f"plot({i+1}).XScale")),
                'YScale': str(engine.eval(f"plot({i+1}).YScale")),
            }
            """
            other properties to potentially use:

            XTick
            YTick
            XAxis
            YAxis
            """

            plot_data['content'] = []
            for j in range(n_children):
                child = {
                    'type': engine.eval(f"plot({i+1}).Children({j+1}).Type", nargout=1).lower()
                }

                if child['type'] == 'image':
                    child['CData'] = mlarray_to_numpy(engine.eval(f"plot({i+1}).Children({j+1}).CData", nargout=1)).astype(float)
                    child['XData'] = mlarray_to_numpy(engine.eval(f"plot({i+1}).Children({j+1}).XData", nargout=1)).astype(float)
                    child['YData'] = mlarray_to_numpy(engine.eval(f"plot({i+1}).Children({j+1}).YData", nargout=1)).astype(float)
                elif child['type'] == 'text':
                    child['text'] = engine.eval(f"plot({i+1}).Children({j+1}).String", nargout=1)
                    child['text'] = [str(e) for e in child['text'] if len(e)]
                elif child['type'] == 'line':
                    child['XData'] = mlarray_to_numpy(engine.eval(f"plot({i+1}).Children({j+1}).XData", nargout=1)).astype(float)
                    child['YData'] = mlarray_to_numpy(engine.eval(f"plot({i+1}).Children({j+1}).YData", nargout=1)).astype(float)
                    child['LineStyle'] = engine.eval(f"plot({i+1}).Children({j+1}).LineStyle", nargout=1)
                else:
                    warnings.warn(f"Don't know what {child['type']} is. Thus nothing extracted.")

                plot_data['content'].append(child)
            fig_data.append(plot_data)

    fig_data = list(reversed(fig_data))

    engine.eval(f"ud = fig.UserData;", nargout=0)
    if engine.eval("isfield(ud, 'scan')"):
        engine.eval(f"ud = rmfield(ud, 'scan');", nargout=0)
    engine.eval(f"ud = jsonencode(ud);", nargout=0)
    user_data = json.loads(engine.workspace['ud'])

    return fig_data, user_data


def load_special_measure_with_matlab_engine(file_name: os.PathLike,
                                            engine=ModuleEngineWrapper,
                                            return_disp:bool=False,
                                            return_rng_as_linspace_params:bool=False) -> Union[
    Tuple[pandas.DataFrame, Sequence[numpy.ndarray], pandas.Series, Sequence[Sequence[str]]],
    Tuple[pandas.DataFrame, Sequence[numpy.ndarray], pandas.Series, Sequence[Sequence[str]], Any],
]:
    """
    Load special measure scan using MATLAB. This requires that the package delivered with MATLAB is installed.

    Args:
        file_name: mat file to load
        engine:
            None, str -> passed to matlab.engine.connect_matlab()
            () -> Use module instance
            MatlabEngine -> used directly

    Returns:
        scan_axes
        data
        config
        getchans
    """
    if matlab is None:
        raise RuntimeError("Requires MATLAB engine interface.")

    engine = ModuleEngineWrapper.to_engine(engine)

    def normalize_chan(chan) -> Sequence[str]:
        if isinstance(chan, str):
            return [chan]
        elif len(chan) == 0:
            # {} or []
            return []
        else:
            return chan

    # we cannot return a struct array to python so we load it into the namespace
    engine.load(os.fspath(file_name), 'scan', 'data', 'configch', 'configvals', nargout=0)

    for f in ['scan', 'data', 'configch', 'configvals']:
        if not engine.eval(f"exist('{f}', 'var')"):
            raise ValueError(f"{file_name} does not contain {f}.")

    data = engine.workspace['data']
    configch = engine.workspace['configch']
    configvals = engine.workspace['configvals']

    config = pandas.Series(numpy.array(configvals).ravel(), index=configch)

    n_loops = int(engine.eval('numel(scan.loops)'))
    getchans = []
    for ii in range(n_loops):
        getchans.append(normalize_chan(engine.eval(f'scan.loops({ii + 1}).getchan')))

    rngs = []
    npoints_list = []
    setchans = []

    for ii in range(n_loops):
        rng = numpy.array(engine.eval(f'scan.loops({ii+1}).rng')).ravel()
        if engine.eval(f"isfield(scan.loops({ii + 1}), 'npoints') && ~isempty(scan.loops({ii + 1}).npoints)"):
            npoints = int(engine.eval(f'scan.loops({ii + 1}).npoints'))
        else:
            npoints = rng.size

        if not len(rng) == 0:
            # TODO rng==[] could be used as a flag to look for awg pulses. 
            rngs.append(rng)
            npoints_list.append(npoints)
            setchans.append(normalize_chan(engine.eval(f'scan.loops({ii + 1}).setchan')))

    # hacked together method for detecting qupulse pulses:
    # looking for awg program
    has_pulse_info = engine.eval("isfield(scan, 'data') && isfield(scan.data, 'awg_program')", nargout=1)
    if has_pulse_info:
        awg_program = json.loads(engine.eval("jsonencode(scan.data.awg_program)"))

        # scan_name = awg_program["pulse_template"]["main"]
        pulse_is_named = True
        scan_name = engine.eval('scan.data.conf_seq_args.pulse_template', nargout=1) # maybe one could take the information which pulse template to use from awg_program["pulse_template"]["main"].
        # if scan.data.conf_seq_args.pulse_template is empty, one will use something else:
        if len(scan_name) == 0 or str(scan_name) == "" or str(scan_name) == "[]":
            if 'main' in awg_program["pulse_template"]:
                scan_name = awg_program["pulse_template"]["main"]

        # ok, then the scan does not have a name and we hope that awg_program["parameters_and_dicts"] still contains the necessary information
        if len(scan_name) == 0:
            scan_name = ""
            pulse_is_named = False
        # there are multiple dicts given for the pulse parameters. The later ones overwrite the settings of the prior ones. This is done in the next lines of code.
        scan_params = {}
        for d in awg_program["parameters_and_dicts"]:
            if (pulse_is_named) and (scan_name in d.keys()):
                scan_params = {**scan_params, **d[scan_name]}
            else:
                scan_params = {**scan_params, **d}
            
        # the hacky way is now to look for start_x, ..., stop_y within the scan_params

        keywords_of_interest = ['start', 'stop', 'N']
        found_kws = {}
        for kw in keywords_of_interest:
            for sp in scan_params.keys():
                if kw in sp:
                    # the keyword of interest is in the selected scan_param
                    se = sp.replace(scan_name, "").replace(kw, "").split("_")
                    axis_name = "_".join([x for x in se if (x != "")])

                    # save that to the dict
                    found_kws.setdefault(kw, {})
                    found_kws[kw].setdefault(axis_name, [])
                    found_kws[kw][axis_name].append(sp)

        prefix_priority = [scan_name, ""]
        selected_kws = {}
        for kw, v in found_kws.items():
            selected_kws[kw] = {}
            for ax, a in v.items():
                a_sorted = [*a]
                a_sorted.sort(key=len)
                for pp in prefix_priority:
                    for e in a_sorted:
                        if pp in e:
                            # now the interesting keywords are found, the corresponding values is to be obtained
                            # selected_kws[kw][pf] = v2[pp][-1] # set the keyword
                            selected_kws[kw][ax] = scan_params[e] # set the value
                            break
                    if ax in selected_kws[kw]:
                        break
                else:
                    warnings.warn(f"The parameter for the keyword {kw} and the axis {ax} has not been found to match with prefix_priority. Will use the shortest one instead.")
                    selected_kws[kw][ax] = scan_params[a_sorted[0]]

        # checking if every axis has all the necessary entries
        all_axes = {}
        for k, v in selected_kws.items():
            for kk in v.keys():
                all_axes.setdefault(kk, 0)
                all_axes[kk] += 1
        _v = -1
        for v in all_axes.values():
            if _v == -1:
                _v = v
            elif _v != v:
                warnings.warn(f"incomplete information about scan axes.")

        # TODO need to throw out the entries that do not contain all of the keywords_of_interest values
        # TODO this might need to use user specific parameters.

        # filling the output arrays (could also be more dynamic)
        qupulse_rngs = numpy.full((len(list(all_axes.keys())), 2), numpy.nan).astype(float)
        qupulse_npoints_list = numpy.full(len(list(all_axes.keys())), numpy.nan).astype(int)
        qupulse_setchans = list(all_axes.keys())
        for i, c in enumerate(qupulse_setchans):
            qupulse_rngs[i][0] = selected_kws['start'][c]
            qupulse_rngs[i][1] = selected_kws['stop'][c]
            qupulse_npoints_list[i] = selected_kws['N'][c]

        rngs = [*list(qupulse_rngs), *rngs]
        npoints_list = [*list(qupulse_npoints_list), *npoints_list]
        setchans = [*list(qupulse_setchans), *setchans]

    # process trafofn
    if engine.eval("isfield(scan.loops, 'trafofn') && any(arrayfun(@(loop) ~isempty(loop.trafofn), scan.loops))"):
        try:
            n_setchans = int(engine.eval('numel(scan.loops(1).trafofn)'))
            _scan_axes = []
            for ii in range(n_setchans):
                _scan_axes.append(read_table(engine, f'scan.loops(1).trafofn({ii+1}).args{{1}}'))
            scan_axes = pandas.concat(_scan_axes, axis='columns')

        except matlab.engine.MatlabExecutionError as e:
            warnings.warn(f"The used trafofns are not understood. And applying them to the extracted ranges and stuff is not implemented.")
            warnings.warn(f"matlab.engine.MatlabExecutionError: {str(e)}")

    if not return_rng_as_linspace_params:
        scan_axes_col = list({chan for chans in setchans for chan in chans})
        scan_axes_rows = [('origin', 0)]
        for l, rng in enumerate(rngs):
            scan_axes_rows.extend((f'loop_{l + 1}', jj) for jj in range(1, rng.size))
        scan_axes_rows = pandas.MultiIndex.from_tuples(scan_axes_rows, names=('axis', 'n'))

        scan_axes = pandas.DataFrame(index=scan_axes_rows, columns=scan_axes_col)

        for col in scan_axes.columns:
            for idx, setchan in enumerate(setchans):
                if col in setchan:
                    axis = f'loop_{idx+1}'
                    for n, x in enumerate(rngs[idx]):
                        if n == 0:
                            scan_axes.loc[('origin', 0), col] = x
                        else:
                            scan_axes.loc[(axis, n), col] = x
                    break
    else:
        scan_axes = {}
        for i, c in enumerate(setchans):
            if isinstance(c, list):
                _c = ",".join(c)
            else:
                _c = c
            scan_axes[_c] = (*rngs[i], npoints_list[i])

    if return_disp:
        disp = json.loads(engine.eval("jsonencode(scan.disp)", nargout=1))
        return scan_axes, [numpy.array(d) for d in data], config, getchans, disp
    else:
        return scan_axes, [numpy.array(d) for d in data], config, getchans


def special_measure_to_dataframe(loaded_scan_data: dict,
                                 squeeze_constant_setchan: bool = True) -> pandas.DataFrame:
    """Try to interpret the data returned from hdf5storage.loadmat(filename)
    as a pandas.DataFrame.

    Not handled/tested yet:
        - Buffered measurements
        - trafofn
        - procfn
        - any thing with MATLAB tables or other classes.
    """
    scan = loaded_scan_data['scan']
    assert scan.shape == (1, 1)
    scan = scan[0, 0]

    loops = scan['loops']
    assert len(loops.shape) == 2
    assert loops.shape[0] == 1
    loops = loops[0, :]

    n_loops = loops.size

    # fails if a loop has more than one npoints
    npoints = list(loops['npoints'].astype(numpy.int64))
    for idx, npoint in enumerate(npoints):
        if npoint < 0:
            warnings.warn(f"Negative npoints {npoint} in loop {idx} gets clamped to 0")
            npoints[idx] = max(npoint, 0)

    setchan = list(loops['setchan'])
    for loop_idx, chan in enumerate(setchan):
        assert len(chan.shape) == 2
        assert chan.shape[0] == 1
        setchan[loop_idx] = tuple(ch[0] for ch in chan.ravel())

    # rngs can be per channel or
    rngs = list(loops['rng'])
    for loop_idx, rng in enumerate(rngs):
        assert rng.shape == (1, 2)
        rngs[loop_idx] = tuple(rng.ravel())

    # This code needs to be adapted if it is possible to use different ranges
    # for different setchannels in the same loop. This might require
    # interpreting the trafofn
    sweeps = []
    for loop_idx in range(n_loops):
        loop_sweeps = {}

        span = numpy.linspace(*rngs[loop_idx], num=npoints[loop_idx])

        for ch in setchan[loop_idx]:
            loop_sweeps[ch] = span
        sweeps.append(loop_sweeps)

    labels, values = [], []
    for sweep in sweeps:
        if len(sweep) > 1:
            vals = list(sweep.values())
            if numpy.unique(vals, axis=0).shape[0] != 1:
                raise RuntimeError('Simultaneous sweep with different ranges not supported', vals)
            labels.append('-'.join(sweep.keys()))
            values.append(vals[0])

    idx = pandas.MultiIndex.from_product(values, names=labels)

    # buffered measurements no handled?
    getchan = loops['getchan']
    for loop_idx, chan in enumerate(getchan):
        assert len(chan.shape) == 2
        assert chan.shape[0] == 1
        getchan[loop_idx] = tuple(ch[0] for ch in chan.ravel())

    measured = list(itertools.chain.from_iterable(getchan))

    # always vector cell
    data = loaded_scan_data['data']
    assert data.shape == (1, len(measured))
    data = data[0, :]

    result = pandas.DataFrame(index=idx)
    assert len(measured) == len(data)
    for meas, val in zip(measured, data):
        val = val.transpose()
        result[meas] = val.flatten()
        assert result[meas].shape == idx.levshape

    if squeeze_constant_setchan:
        to_squeeze = [lvl_idx
                      for lvl_idx, lvl_dim in enumerate(idx.levshape)
                      if lvl_dim == 1]
        result = result.droplevel(to_squeeze)

    try:
        result.attrs['consts'] = loaded_scan_data['scan']['consts']
    except ValueError:
        pass

    return result


def load_special_measure_scan(file_name: os.PathLike,
                              squeeze_constant_setchan: bool = True) -> pandas.DataFrame:
    """
    :param file_name: Path of the file to load
    :param squeeze_constant_setchan: If true, "set channels" that are constant are not included in the index
    :return: Data frame with a multi-index that corresponds to the "set channels" and columns that correspond to the
    "get channels".
    """
    file_name = os.fspath(file_name)

    # this is slow as the scan stuct is quite complicated and hdf5storage creates a dtype for the whole thing
    file_contents = hdf5storage.loadmat(file_name)

    return special_measure_to_dataframe(file_contents, squeeze_constant_setchan)


@qutil.caching.file_cache
def cached_load_mat_file(filename):
    return hdf5storage.loadmat(filename)
