"""This module contains some useful plotting functions"""
from collections import OrderedDict
from weakref import WeakValueDictionary
from typing import Sequence, Tuple
import warnings
from contextlib import contextmanager

import matplotlib as mpl
from matplotlib import cycler
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


__all__ = ["changed_plotting_backend", "plot_2d_dataframe", "cycle_plots", "rwth_color_cycle", "update_plot"]

_color_names = ['blue', 'magenta', 'green', 'orange', 'teal', 'maygreen',
                'red', 'purple', 'violet', 'bordeaux', 'petrol', 'yellow']
_color_tuples = [
    (0/255, 84/255, 159/255),       # blue
    (227/255, 0/255, 102/255),      # magenta
    (87/255, 171/255, 39/255),      # green
    (246/255, 168/255, 0/255),      # orange
    (0/255, 152/255, 161/255),      # teal
    (189/255, 205/255, 0/255),      # maygreen
    (204/255, 7/255, 30/255),       # red
    (122/255, 111/255, 172/255),    # purple
    (97/255, 33/255, 88/255),       # violet
    (161/255, 16/255, 53/255),      # bordeaux
    (0/255, 97/255, 101/255),       # petrol
    (255/255, 237/255, 0/255),      # yellow
]
_RWTH_COLORS = OrderedDict(zip(_color_names, _color_tuples))


def _to_corner_coords(index: pd.Index) -> np.ndarray:
    """Helper function to transform N coordinates pointing at centers of bins to N+1 coords pointing to the edges"""
    coords = index.values

    delta = coords[-1] - coords[-2]

    return np.concatenate((coords, [coords[-1] + delta])) - delta / 2


def _data_hash(*args: np.ndarray) -> int:
    return hash(tuple(arg.tobytes() for arg in args))


@contextmanager
def changed_plotting_backend(backend='agg'):
    """ This decorator/context manager wraps a function to temporarily use the agg backend for matplotlib.

    This class wraps functions to use the agg backend for matplotlib plots. It saves the previously chosen backend,
    sets agg as the backend, runs the wrapped function, and then sets the backend back to what it was previously. The
    standard backend leaks memory, thus switching to agg is advantageous if one only want to savefig things.
    """
    original_backend = mpl.get_backend()
    plt.switch_backend(backend)
    try:
        yield
    finally:
        plt.switch_backend(original_backend)


def plot_2d_dataframe(df: pd.DataFrame,
                      ax: plt.Axes = None, square=True,
                      column=None, index_is_y=True,
                      update_mode: str = 'auto') -> plt.Axes:
    """Plot pandas data frames using pcolormesh. This function expects numeric labels and it can update an existing
    plot. Have a look at seaborn.heatmap if you need something else.

    'auto': 'rescale' if x-label, y-label, and title are the same else 'clear'
    'clear': Clear axis before drawing
    'overwrite': Just plot new data frame on top (no colorbar is drawn)
    'rescale': Recalculate and redraw the colorbar

    Details:
     - plotted meshes are stored in ax.meshes
     - The colorbar is stored in ax.custom_colorbar (DO NOT RELY ON THIS)
     - If the plotted data is already present we just shift it to the top using set_zorder
     - Uses _data_hash(x, y, c) to identify previously plotted data

    :param df: pandas dataframe to plot
    :param ax: Axes object
    :param square:
    :param column: Select this column from the dataframe and unstack the index
    :param index_is_y: If true the index are on the y-axis and the columns on the x-axis
    :param update_mode: 'auto',  'overwrite' or 'rescale'
    :return:
    """
    if ax is None:
        ax = plt.gca()

    if square:
        ax.set_aspect("equal")

    if column is None and len(df.columns) == 1 and len(df.index.levshape) == 2:
        column = df.columns[0]

    if column is not None:
        title = column
        series = df[column]
        df = series.unstack()

    else:
        title = None

    c = df.values
    x_idx = df.columns
    y_idx = df.index

    if not index_is_y:
        c = np.transpose(c)
        x_idx, y_idx = y_idx, x_idx

    x_label = x_idx.name
    y_label = y_idx.name

    if update_mode == 'auto':
        if (x_label, y_label, title) == (ax.get_xlabel(), ax.get_ylabel(), ax.get_title()):
            update_mode = 'rescale'
        else:
            update_mode = 'clear'
    if update_mode not in ('clear', 'rescale', 'overwrite'):
        raise ValueError('%s is an invalid value for update_mode' % update_mode)

    if update_mode == 'clear':
        if hasattr(ax, 'custom_colorbar'):
            # clear colorbar axis
            ax.custom_colorbar.ax.clear()
        ax.clear()
        ax.meshes = WeakValueDictionary()

    y = _to_corner_coords(y_idx)
    x = _to_corner_coords(x_idx)

    if not hasattr(ax, 'meshes'):
        ax.meshes = WeakValueDictionary()

    df_hash = _data_hash(x, y, c)
    current_mesh = ax.meshes.get(df_hash, None)

    if current_mesh is None:
        # data not yet drawn -> draw it
        current_mesh = ax.pcolormesh(x, y, c)
        ax.meshes[df_hash] = current_mesh

    # push to foreground
    max_z = max(mesh.get_zorder() for mesh in ax.meshes.values()) if ax.meshes else 0
    current_mesh.set_zorder(max_z + 1)

    if update_mode != 'overwrite':
        all_data = [mesh.get_array()
                    for mesh in ax.meshes.values()]
        vmin = min(map(np.min, all_data))
        vmax = max(map(np.max, all_data))

        if not hasattr(ax, 'custom_colorbar'):
            ax.custom_colorbar = plt.colorbar(ax=ax, mappable=current_mesh)

        for mesh in ax.meshes.values():
            mesh.set_clim(vmin, vmax)

        try:
            ax.custom_colorbar.set_clim(vmin, vmax)
        except AttributeError:
            ax.custom_colorbar.mappable.set_clim(vmin, vmax)

    else:
        # TODO: fix
        warnings.warn("for update_mode='overwrite' the colorbar code is stupid")

    ax.set(ylabel=y_label, xlabel=x_label, title=title)

    return ax


def update_plot(handle, data):
    """Update a plot.

    Parameters
    ----------
    handle: matplotlib data handle
        The plot object that is updated. For instance, a lines.Line2D or
        image.AxesImage object.
    *data: Sequence
        New data to plot.
            - for line plots: [xdata, ydata]
            - for image plots: imdata (m x n array)

    """
    handle.set_data(data)
    if hasattr(handle, 'colorbar'):
        handle.colorbar.set_array(data)
        handle.colorbar.changed()
        handle.colorbar.autoscale()
        handle.colorbar.draw_all()

    # Rescale
    handle.axes.relim()
    handle.axes.autoscale_view()
    # We need to draw *and* flush
    handle.figure.canvas.draw()
    handle.figure.canvas.flush_events()


def cycle_plots(plot_callback, *args,
                fig: plt.Figure = None, ax: plt.Axes = None, **kwargs) -> Tuple[plt.Figure, plt.Axes]:
    """Call plot_callback(fig, ax, curr_pos, *args, **kwargs) on each left/right arrow key press.
    Initially curr_pos = 0. The right arrow increases and the left arrow decreases the current position.
    There is no limit so you need to do the wraparound yourself if needed:

    >>> plot_data = [(x1, y1), (x2, y2), ...]
    >>> def example_plot_callback(fig, ax, pos):
    >>>     idx = pos % len(plot_data)
    >>>     ax.plot(*plot_data[idx])
    """
    def key_event(e):
        if e.key == "right":
            key_event.curr_pos += 1
        elif e.key == "left":
            key_event.curr_pos -= 1
        else:
            return
        plot_callback(fig, ax, key_event.curr_pos, *args, **kwargs)
        plt.draw_all()

    key_event.curr_pos = 0

    if fig is None:
        if ax is None:
            fig = plt.figure()
        else:
            fig = ax.get_figure()
    if ax is None:
        ax = fig.add_subplot(111)

    if isinstance(ax, np.ndarray):
        assert all(a in fig.axes for a in ax.flat)
    else:
        assert ax in fig.axes, "axes not in figure"

    fig.canvas.mpl_connect('key_press_event', key_event)

    plot_callback(fig, ax, key_event.curr_pos, *args, **kwargs)
    plt.draw_all()

    return fig, ax


def get_rwth_color_cycle(alpha: float = 1, exclude: Sequence[str] = None):
    """Get the default RWTH color cycle with an alpha channel.

    Parameters
    ----------
    alpha: float
        The alpha (transparency) value for the color cycle.
    exclude: sequence of str
        Exclude these colors. See _RWTH_COLORS for all available keys.
        Yellow is a good choice to exclude.

    Example
    -------
    >>> cycle_100 = get_rwth_color_cycle(1.)
    >>> cycle_50 = get_rwth_color_cycle(.5)
    >>> fig, ax = plt.subplots()
    >>> x = np.linspace(0, 2*np.pi, 51)
    >>> for i, (v100, v50) in enumerate(zip(cycle_100, cycle_50)):
    >>>     ax.plot(x, np.sin(x) + i / len(cycle_100), lw=2, **v100)
    >>>     ax.plot(x, -np.sin(x) + i / len(cycle_50), lw=2, **v50)

    See Also
    --------
    https://matplotlib.org/3.3.3/tutorials/intermediate/color_cycle.html

    https://matplotlib.org/cycler/
    """
    if alpha < 0 or alpha > 1:
        raise ValueError('alpha should be in the range [0, 1].')

    exclude = exclude or []
    return cycler(color=[tup + (alpha,) for name, tup in _RWTH_COLORS.items()
                         if name not in exclude])


rwth_color_cycle_25 = get_rwth_color_cycle(.25)
rwth_color_cycle_50 = get_rwth_color_cycle(.5)
rwth_color_cycle_75 = get_rwth_color_cycle(.75)
rwth_color_cycle_100 = get_rwth_color_cycle(1)
rwth_color_cycle = rwth_color_cycle_100
