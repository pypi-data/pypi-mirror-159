# hy-ipython: a Hy magic for IPython

Currently requires _exactly_ Hy 0.24.

Installation:

```sh
pip install hy-ipython
```

Developer things (requires [Flit](https://flit.pypa.io/)):

```sh
# Create a venv (or use virtualenv)
python -m venv ./project.venv
flit install --symlink --python ./project.venv/bin/python

# Build wheel and sdist
flit build --format wheel --setup-py
flit build --format sdist --setup-py

# Publish to PyPI
flit publish --format wheel --setup-py
flit publish --format sdist --setup-py
```
