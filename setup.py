
from operator import attrgetter
from os import path
from setuptools import setup

try:
    # pip >=20
    from pip._internal.req import parse_requirements
except ImportError:
    try:
        # 10.0.0 <= pip <= 19.3.1
        from pip._internal.req import parse_requirements
    except ImportError:
        # pip <= 9.0.3
        from pip.req import parse_requirements



def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()


def from_here(relative_path):
    return path.join(path.dirname(__file__), relative_path)


requirements_txt = list(map(str, map(
    attrgetter("requirement"),
    parse_requirements(from_here("requirements.txt"), session="")
)))

setup(
    name="win10toast",
    version="0.9",
    install_requires=requirements_txt,
    packages=["win10toast"],
    license="BSD",
    url="https://github.com/jithurjacob/Windows-10-Toast-Notifications",
    download_url = 'https://github.com/jithurjacob/Windows-10-Toast-Notifications/tarball/0.9',
    description=(
        "An easy-to-use Python library for displaying "
        "Windows 10 Toast Notifications"
    ),
    include_package_data=True,
    package_data={
        '': ['*.txt'],
        'win10toast': ['data/*.ico'],
    },
    long_description=read('README.md'),
    author="Jithu R Jacob",
    author_email="jithurjacob@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        'Operating System :: Microsoft',
        'Environment :: Win32 (MS Windows)',
        "License :: OSI Approved :: MIT License",
    ],
)
