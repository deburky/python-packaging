# first-python-package

This package does amazing things.

## Package Features

- **Build system**: `setuptools` with `setup.cfg` configuration
- **Cython extension**: Includes compiled `harmonic_mean` module for performance
- **Dependencies**: Uses `numpy` for numerical operations and `termcolor` for colored output
- **Entry point**: Provides `harmony` CLI command

**Alternative build backends**: `maturin` (for Rust-based packages), `hatchling` (default in `uv`), or `poetry-core`.

This repo is based on the book [Publishing Python Packages: Test, Share, and Automate Your Projects](https://pypackages.com/).   
The code examples from the book are available here: [GitHub](https://github.com/PacktPublishing/Python-Project-Setup-Guide/tree/main/Chapter03/examples).

## Building the Package

To build the package, run the following command:

```shell
pyproject-build
```

To install the package locally, use:

```shell
python -m pip install -e .  # Editable install for development
```

After installation, the `harmony` command is available:

```shell
harmony  # Runs the harmonic mean calculator
```

### Available Tox Commands

Run tests on specific Python versions:
```shell
tox -e py39          # Test on Python 3.9
tox -e py310         # Test on Python 3.10
```

Run quality checks:
```shell
tox -e format        # Format code with black
tox -e lint          # Lint with flake8
tox -e typecheck     # Type check with mypy
tox -e isort         # Sort imports
```

Run everything in parallel:
```shell
tox -p -e py39,py310,typecheck,format,lint
```

## CI/CD with GitHub Actions

The workflow automatically builds wheels for Linux, Windows, and macOS (Intel + Apple Silicon) using `cibuildwheel`.

**Configuration:**
```yaml
env:
  CIBW_ARCHS_MACOS: "x86_64 arm64"  # Separate wheels for Intel and Apple Silicon
  CIBW_BUILD: "cp39-* cp310-*"       # Python 3.9 and 3.10 only
```

**Publishing to Test PyPI:**
```shell
git tag v0.1.0
git push origin v0.1.0
```

**Install from Test PyPI:**
```shell
pip install --index-url https://test.pypi.org/simple/ first-python-package
```

## Notes

- `black` doesn't support configuration with `setup.cfg`.
- `mccabe` package measures the complexity of the code, another alternative is `radon`.
- For local wheel builds: `python -m cibuildwheel --output-dir wheels`