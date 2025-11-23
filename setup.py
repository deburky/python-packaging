import numpy
from setuptools import setup, Extension

from Cython.Build import cythonize


extensions = [
    Extension(
        "imppkg.harmonic_mean",
        ["src/imppkg/harmonic_mean.pyx"],
        include_dirs=[numpy.get_include()],
        define_macros=[("CYTHON_TRACE", "1")],
    ),
]

setup(
    ext_modules=cythonize(extensions, compiler_directives={"linetrace": True}),
)