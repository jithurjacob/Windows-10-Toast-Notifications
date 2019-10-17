
from operator import attrgetter
from os import path

from setuptools import setup


def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()


def from_here(relative_path):
    return path.join(path.dirname(__file__), relative_path)


setup(
    name="win10toast-persist",
    version="0.10",
    install_requires=[
        "pypiwin32",
        "setuptools"
    ],
    packages=["win10toast_persist"],
    license="BSD",
    url="https://github.com/tnthieding/Windows-10-Toast-Notifications",
    download_url='',
    description=(
        "An easy-to-use Python library for displaying "
        "Windows 10 Toast Notifications with support for "
        "persisting notifications."
    ),
    include_package_data=True,
    package_data={
        '': ['*.txt'],
        'win10toast_persist': ['data/*.ico'],
    },
    long_description=read('README.rst'),
    author="Jithu R. Jacob and Tyler N. Thieding",
    author_email="python@thieding.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        'Operating System :: Microsoft',
        'Environment :: Win32 (MS Windows)',
        "License :: OSI Approved :: MIT License",
    ],
)
