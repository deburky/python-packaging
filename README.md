# first-python-package

This package does amazing things.

We use `setuptools` to build the package.

Alternatives are `maturin` (for rust-based packages) and `hatchling` (default in `uv`).

This repo is based on the book [Publishing Python Packages: Test, Share, and Automate Your Projects](https://pypackages.com/).   
The code examples from the book are available here: [GitHub](https://github.com/PacktPublishing/Python-Project-Setup-Guide/tree/main/Chapter03/examples).

## Building the Package

To build the package, run the following command:

```shell
pyproject-build
```

To install the package locally, use:

```shell
python -m pip install first-python-package
```

To run all commands, use:

```shell
tox -p -e py39,py310,typecheck,format,lint
```

## Notes

`black` doesn't support configuration with `setup.cfg`.

`mccabe` package measures the complexity of the code, another alternative is `radon`.