# pysetwindowpos

Python wrapper for setwindowpos Windows API. MS Windows only.

Currently, this supports only setting a window as topmost (i.e., always on top).
Other invocations of SetWindowPos should be relatively
easy to add.

A tkinter example is built in and can by run by executing

```
py -m pysetwindowpos.setwindowpos
```

## Hacking

To use a development copy of the package as a dependency, navigate to the directory where the `pyproject.toml` file is and run:

```
pip install -e .
```

The blank `setup.cfg` is needed for this to work.

## TODO
1. Prevent `RuntimeWarning` when running `py -m pysetwindowpos.setwindowpos` (use `__main__`?). 

