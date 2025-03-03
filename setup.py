from setuptools import setup, Extension

import os
import sys
import setuptools
import glob

__version__ = '0.0.4'

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

extra_compile_args_dict = {
    'linux': ['-w', '-std=c++17', '-O3', '-fopenmp', '-s', '-ffunction-sections', '-fdata-sections',
              '-Wl,--gc-sections', '-flto','-fuse-ld=lld'],
    'linux2': ['-w', '-std=c++17', '-O3', '-fopenmp'],
    'darwin': ['-w', '-std=c++17', '-stdlib=libc++', '-O3', '-fopenmp'],
    'win32': ['/w', '/std:c++17', '/Ox', '/openmp', '/GL', '/MP', '/MT'],

}

ext_modules = [
    Extension(
        "_phashmap",
        glob.glob('src/*.cpp'),
        include_dirs=['lib/parallel_hashmap', 'lib/pybind11/include'],
        language='c++',
        extra_compile_args=extra_compile_args_dict[sys.platform],
        extra_link_args=[],
        define_macros=[('DOCTEST_CONFIG_DISABLE', None)]
    )
]

setup(
    name='phashmap',
    version=__version__,
    author='yojeep',
    author_email='1379690602@qq.com',
    description='A Vectorized Dictionary for Python',
    packages=['phashmap'],
    package_dir={'phashmap': 'phashmap'},
    package_data={},
    ext_modules=ext_modules,
    # install_requires = ['numpy', 'pybind11'],
    include_package_data=True,
    zip_safe=False,
    long_description=readme,
    long_description_content_type='text/markdown',
    url="https://github.com/atom-moyer/getpy",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: C++',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        # 'Operating System :: Unix'
    ],
)
