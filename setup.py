
from operator import attrgetter
from os import path

from pip.req import parse_requirements
from setuptools import setup

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()


def from_here(relative_path):
    return path.join(path.dirname(__file__), relative_path)


requirements_txt = list(map(str, map(
    attrgetter("req"),
    parse_requirements(from_here("requirements.txt"), session="")
)))

setup(
    name="win10toast",
    version="0.1",
    install_requires=requirements_txt,
    packages=["win10toast"],
    license="BSD",
    url="https://github.com/jithurjacob/Windows-10-Toast-Notifications",
    download_url = 'https://github.com/jithurjacob/Windows-10-Toast-Notifications/tarball/0.1',
    description=(
        "An easy-to-use Python library for displaying "
        "Windows 10 Toast Notifications"
    ),
    long_description=read('README.md'),
    author="Jithu R Jacob",
    author_email="jithurjacob@gmail.com",
    maintainer="Youhei Sakurai",
    maintainer_email="sakurai.youhei@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        'Operating System :: Microsoft',
        'Environment :: Win32 (MS Windows)',
        "License :: OSI Approved :: BSD License",
    ],
)
