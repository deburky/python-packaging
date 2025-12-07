---
layout: default
title: First Python Package
---

# First Python Package

A Python package demonstrating modern packaging practices with Cython extensions.

## Features

- **Cython Extensions**: High-performance `harmonic_mean` module compiled to native code
- **Cross-Platform Wheels**: Automated builds for Linux, Windows, and macOS (Intel + Apple Silicon)
- **CLI Tool**: Provides `harmony` command-line utility
- **Full CI/CD**: GitHub Actions workflow with testing, linting, and automated publishing

## Installation

```bash
pip install first-python-package
```

### From Test PyPI

```bash
pip install --index-url https://test.pypi.org/simple/ first-python-package
```

## Quick Start

After installation, use the `harmony` command:

```bash
harmony
```

## Development

### Local Setup

```bash
git clone https://github.com/deburky/python-packaging.git
cd python-packaging
pip install -e .
```

### Running Tests

```bash
# Run all tests
tox -e py39,py310

# Run specific checks
tox -e lint        # Linting with flake8
tox -e typecheck   # Type checking with mypy
tox -e format      # Format code with black
```

## Building

### Source Distribution

```bash
python -m build --sdist
```

### Platform Wheels

```bash
python -m cibuildwheel --output-dir wheels
```

## Architecture

### Build System

- **setuptools**: Package build backend
- **Cython**: Compiles Python code to C for performance
- **cibuildwheel**: Builds wheels for multiple platforms automatically

### Configuration Files

- `setup.py` - Cython extension configuration
- `setup.cfg` - Package metadata and tool configurations
- `pyproject.toml` - Build system requirements
- `MANIFEST.in` - Source distribution file inclusion rules

### CI/CD Pipeline

GitHub Actions workflow includes:
1. **Quality Checks**: Format, lint, type checking
2. **Testing**: Python 3.9 and 3.10
3. **Building**: Wheels for all major platforms
4. **Publishing**: Automated deployment to Test PyPI on version tags

## Resources

- [GitHub Repository](https://github.com/deburky/python-packaging)
- [Publishing Python Packages Book](https://pypackages.com/)
- [Package on Test PyPI](https://test.pypi.org/project/first-python-package/)

## License

MIT License - see [LICENSE](https://github.com/deburky/python-packaging/blob/main/LICENSE) file for details.


