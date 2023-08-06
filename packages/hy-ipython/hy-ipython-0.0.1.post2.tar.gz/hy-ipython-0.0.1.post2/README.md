# Hy-IPython: a Hy magic for IPython

Currently requires _exactly_ [Hy 0.24](https://pypi.org/project/hy/0.24.0/).

Based on a [snippet by Ben Denham](https://github.com/hylang/hy/issues/1665#issuecomment-696561661).

## Installation

```sh
pip install hy-ipython
```

## Development

Requires [Flit](https://flit.pypa.io/).

```sh
# Create a venv (or use virtualenv)
python -m venv ./project.venv

# Install into the venv
flit install --symlink --python ./project.venv/bin/python

# Build wheel and sdist
flit build --format wheel --setup-py
flit build --format sdist --setup-py

# Publish to PyPI
flit publish --format wheel --setup-py
flit publish --format sdist --setup-py
```

Don't forget to set up your `pypirc` file: <https://packaging.python.org/en/latest/specifications/pypirc/>.
