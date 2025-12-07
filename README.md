# Python Packaging

📚 **[View Documentation](https://deburky.github.io/python-packaging/)**

> [!NOTE]  
> This repo is based on the book [Publishing Python Packages: Test, Share, and Automate Your Projects](https://pypackages.com/).   
> The code examples from the book are available here: [GitHub](https://github.com/PacktPublishing/Python-Project-Setup-Guide/tree/main/Chapter03/examples).

## Package Features

- **Build system**: `setuptools` with `setup.cfg` configuration
- **Cython extension**: Includes compiled `harmonic_mean` module for performance
- **Dependencies**: Uses `numpy` for numerical operations and `termcolor` for colored output
- **Entry point**: Provides `harmony` CLI command

> [!IMPORTANT]
> This package uses **Cython extensions** that compile to platform-specific binaries. We use `cibuildwheel` in CI/CD to build wheels for Linux, Windows, and macOS (Intel + Apple Silicon). Without pre-built wheels, users would need a C compiler and build tools installed.

**Alternative build backends**: 
- `hatchling` - Modern, pure Python build backend (default in `uv`)
- `poetry-core` - Used by Poetry projects
- `maturin` - For Rust-based packages (see below)

### Why Maturin for Rust?

**Maturin** is specifically designed for building Python packages with **Rust extensions** using PyO3 bindings:

**Key differences from Cython:**
- **Cython**: Python → C → compiled binary (what this project uses)
- **Maturin/Rust**: Rust → compiled binary via PyO3 bindings

**How Rust bindings work:**
1. Write performance-critical code in Rust
2. Use **PyO3** to create Python bindings (exposes Rust functions to Python)
3. Maturin handles compilation and wheel building automatically
4. Result: Fast Rust code callable from Python

**Advantages of Rust + Maturin:**
- Memory safety without garbage collection
- Better performance than Cython in many cases
- Modern tooling (Cargo, rustfmt, clippy)
- Cross-compilation support built-in

**When to use:**
- Use **Cython** (this project): Optimize Python code, gradual performance improvements
- Use **Rust + Maturin**: Writing new high-performance code from scratch, need memory safety guarantees

## Project Configuration Files

### `setup.py`
Handles the **Cython extension build**. Defines the `harmonic_mean` extension module with numpy includes and compiler directives for coverage tracing.

### `setup.cfg`
Contains **package metadata and configuration** for all tools:
- Package metadata (name, version, author, dependencies)
- Tool configurations (mypy, flake8, black, pytest, coverage)
- Tox environments (test, lint, typecheck, format)
- Entry points (the `harmony` CLI command)

### `pyproject.toml`
Specifies the **build system requirements**: `setuptools`, `wheel`, `cython`, and `numpy` needed to build the package.

### `MANIFEST.in`
Controls which **non-Python files** are included in the source distribution:
- `graft src` - includes all files in the src directory (like `data.json`)
- `recursive-exclude` - excludes Python cache files

> [!TIP]
> Modern Python packages can use `pyproject.toml` for everything, but this project uses the traditional `setup.cfg` + `setup.py` approach, which is still widely used and well-supported.

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

<img src="https://repository-images.githubusercontent.com/68465360/5e2a7100-65b0-11e9-9207-2ac66c4446ee" alt="tox" width="200"><br>

tox is a tool for running tests in multiple environments.

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

<img src="https://avatars.githubusercontent.com/u/44036562?s=200&v=4" alt="github action logo" width="100"><br>

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

## Modern Python Tooling with `uv`

<img src="https://www.kdnuggets.com/wp-content/uploads/awan_uv_new_python_package_manager_3-1024x614.png" alt="uv" width="500"><br>

[`uv`](https://github.com/astral-sh/uv) is a next-generation Python package manager written in Rust, designed to replace multiple tools with a single, fast solution.

### What is `uv`?

`uv` is an **extremely fast** Python package and project manager that aims to replace:
- `pip` (package installation)
- `pip-tools` (dependency management)
- `virtualenv` / `venv` (virtual environments)
- `poetry` / `pipenv` (project management)
- `twine` (package publishing)

**Key advantages:**
- ⚡ **10-100x faster** than pip (written in Rust)
- 🔒 **Built-in lockfiles** for reproducible builds
- 📦 **Unified tooling** - one tool for everything
- 🎯 **Drop-in replacement** - compatible with existing workflows

### Publishing with `uv`

Instead of using `twine` or GitHub Actions, you can publish directly with `uv`:

```bash
# Build the package
uv build

# Publish to PyPI
uv publish

# Publish to Test PyPI
uv publish --publish-url https://test.pypi.org/legacy/
```

**Authentication:**
```bash
# Set PyPI token
export UV_PUBLISH_TOKEN="pypi-..."

# Or use keyring
uv publish --keyring-provider subprocess
```

### `uv` vs Traditional Workflow

**Traditional (this project):**
```bash
python -m build                    # Build package
python -m twine upload dist/*      # Upload to PyPI
pip install -r requirements.txt    # Install dependencies
```

**With `uv`:**
```bash
uv build                          # Build package
uv publish                        # Upload to PyPI
uv sync                           # Install dependencies (from lockfile)
```

### Why `uv` is the Future

1. **Speed**: Resolves and installs dependencies 10-100x faster than pip
2. **Reliability**: Lockfiles ensure reproducible environments across machines
3. **Simplicity**: One tool instead of pip, venv, pip-tools, twine, etc.
4. **Modern**: Built with Rust, designed for today's Python ecosystem
5. **Compatible**: Works with existing `pyproject.toml` and `requirements.txt`

### Migrating to `uv`

This project could be simplified with `uv`:

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create project
uv init

# Add dependencies
uv add numpy termcolor

# Add dev dependencies
uv add --dev pytest black flake8 mypy

# Run commands
uv run pytest
uv run black .

# Build and publish
uv build
uv publish
```

> [!TIP]
> While this project uses traditional tools (setuptools, pip, twine), **`uv` represents the future** of Python packaging. It's production-ready and actively maintained by Astral (creators of Ruff). Consider using `uv` for new projects!

## Type Checking with `mypy`

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRF18mjS57iuxVMTwwChBsAHKOeqApqn0EsiQ&s" alt="mypy logo" width="200">

**mypy** is a static type checker for Python that helps catch bugs before runtime:

```bash
tox -e typecheck  # Run mypy on this project
```

**Configuration** (in `setup.cfg`):
```ini
[mypy]
python_version = 3.10
warn_unused_configs = True
check_untyped_defs = True
```

**Why use type checking?**
- 🐛 **Catch bugs early** - Find type errors before running code
- 📝 **Better documentation** - Type hints serve as inline documentation
- 🔧 **IDE support** - Better autocomplete and refactoring
- 🛡️ **Safer refactoring** - Confidence when changing code

**Example from this project:**
```python
def harmonic_mean(numbers: list[float]) -> float:
    """Calculate harmonic mean with type hints."""
    return len(numbers) / sum(1/x for x in numbers)
```

mypy verifies that you pass a list of floats and get a float back, catching type mismatches at development time.

> [!TIP]
> Modern Python projects should use type hints and mypy. They're optional but highly recommended for maintainability and catching bugs early.

## Notes
### Other Tools

- `black` doesn't support configuration with `setup.cfg` (uses `pyproject.toml` instead).
- `mccabe` package measures the complexity of the code, another alternative is `radon`.
- For local wheel builds: `python -m cibuildwheel --output-dir wheels`

### About `.egg` and `.egg-info` files

**`.egg-info` directories** (like `src/first_python_package.egg-info/`) are created during package installation and contain metadata about the installed package. They're still used today.

**`.egg` files** were the predecessor to wheels (`.whl`):
- Used by `easy_install` (now deprecated)
- Essentially ZIP files with package code + metadata
- **Replaced by wheels** which are faster, more reliable, and don't execute code during installation

> [!NOTE]
> You may see `.egg-info` directories in your project - this is normal! They're created by `pip install -e .` and contain package metadata. Modern Python uses **wheels** (`.whl`) for distribution, not `.egg` files.