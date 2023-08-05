# tkdialog-wrapper

A wrapper library to use tkinter dialogs easily.

[![PyPI version](https://badge.fury.io/py/tkdialog-wrapper.svg)](https://badge.fury.io/py/tkdialog-wrapper) [![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)

## Usage

`pip install tkdialog-wrapper`

```python
import tkdialog

# make open dialog
filename = tkdialog.open_dialog()

# Extensions can be assigned.
## for numpy savez files
dat = np.load(tkdialog.open_dialog('.npz'))
## for csv files
df = pd.read_csv(tkdialog.open_dialog('.csv'))

# make saveas dialog
filename = tkdialog.open_dialog(ext='pkl')


# open a directory selector
dirname = tkdialog.open_dir_dialog()

# change current working directory with a selector dialog
tkdialog.chdir_with_dialog()


# open a pickled file (*.pkl) with a dialog
obj = tkdialog.load_pickle_with_dialog()

# open a pickled file (*.dat) with a dialog
obj = tkdialog.load_pickle_with_dialog(ext='.dat')

# pickle an object with a dialog
dat = {'x': 100, 'y': '01234'}
tkdialog.dump_pickle_with_dialog(dat)
```

## Change log
### [2.1.0]
- add functions:
  - `chdir_with_dialog`, `open_dir_dialog`

### [2.0.0]
- breaking changes:
  - supported python version >= 3.5
  - argument of all functions
  - add docstring
  - add typehint

### [1.x]
