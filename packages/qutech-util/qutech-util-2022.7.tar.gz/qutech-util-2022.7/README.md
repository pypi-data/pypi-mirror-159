# qutil
Long term goal is to gather utility functions here. It is not meant as a lightweight package. If you just want to use it you can install it via
```
pip install git+https://git.rwth-aachen.de/qutech/qutil.git
```
However, this package profits from everybody's work so please make a development install and contribute your changes. You can do this via
```
pip install -e git+https://git.rwth-aachen.de/qutech/qutil.git#egg=qutil
```
This will download the source code (i.e. clone the git repository) into a subdirectory of the `./src` argument and link the files into your environment instead of copying them. If you are on windows you can use [SourceTree](https://www.sourcetreeapp.com/) which is a nice GUI for git.
You can specify the source code directory with the `--src` argument (which needs to be BEFORE `-e`):
```
pip install --src some_directory/my_python_source -e git+https://git.rwth-aachen.de/qutech/qutil.git#egg=qutil
```
If you have already downloaded/cloned the package yourself you can use `python setup.py develop` or `python -m pip install . -e`.

## qutil.plotting
`cycle_plots` helps you cycling through many plots with the arrow keys (there are probably much better functions for this out there)
`plot_2d_dataframe` helps you plot 2d data frames with numeric indices
`get_rwth_color_cycle` and the predefined `rwth_color_cycle` are cycler instances with the official RWTH corporate design colors:

![cycler example](./doc/source/_static/cycles.png)

## qutil.matlab
In this module there are functions that are helpful for reading `.mat` files, especially those created with special measure.
If you simply want to open a random `.mat` file you can use `hdf5storage.loadmat`.

Loading matlab files with "newer" MATLAB classes like `table` requires connecting (and starting) MATLAB instance.
The function `load_special_measure_with_matlab_engine` can load most special measure scans by utilizing the MATLAB engine interface. To use it you require a "sufficiently new" version of MATLAB and then navigate to `C:\Program Files\MATLAB\$VERSION\extern\engines\python` and call `python setup.py install`. 

## qutil.const
This module defines all the constants you could wish for as well as functions to convert temperatures (`convert_temperature`) or between wavelengths and frequencies (`lambda2nu`, `nu2lambda`). For an overview, see the module docstring.

## qutil.linalg
This module provides several handy linear algebra functions. While some are implemented elsewhere, the implementation here is typically speedier for large arrays. For example, `pauli_expm` exploits the fact that a matrix exponential of Pauli matrices can be written as a cosine times the identity matrix plus a sine times the Paulis to speed up the calculation.

For an overview of the included functions, see the module docstring.

## qutil.ui
This module collects UI helpers, such as a progress bar for loops that can be used like so:
```python
for i in qutil.ui.progressbar(range(n)):
    do_something()
```

## qutil.qi
In this module there are some quantities and functions related to quantum information, like the Pauli matrices in different data types.

## qutil.random
Here we collect functions for random numbers like `random_hermitian` to generate random Hermitian matrices.

## qutil.itertools
This module contains a everything from `itertools`, `more_itertools` and custom functions.

## qutil.caching
Here you find decorators, functions and classes that help you implement caching like `file_cache` and `lru_cache`. This is helpful if you need to call computationally expensive functions with the same arguments repeatedly.

## qutil.io
User input related functions like `query_yes_no` or a `CsvLogger` interface (for reading use pandas.read_csv).

## qutil.parallel
Functions and classes related to parallel execution i.e. multi-threading, multi-processing and asyncio.
There is a class for periodic callbacks from another thread `ThreadedPeriodicCallback`.

## qutil.hardware
This package contains little scripts to talk to various hardware devices. For example reading the leak tester via serial interface.

## qutil.qcodes
Functions to convert from and to qcodes data sets. Currently only
from `pandas.DataFrame` to `qcodes.data.data_set.DataSet`
