#!/usr/bin/python
# -*- coding: UTF-8 -*-
from operator import attrgetter
from os import path

from pip.req import parse_requirements
from setuptools import setup


def from_here(relative_path):
    here = path.dirname(__file__)
    return path.join(here, relative_path)


requirements_txt = list(map(str, map(
    attrgetter("req"),
    parse_requirements(from_here("requirements.txt"), session="")
)))

setup(
    name="win10toast",
    version="0.0.1",
    install_requires=requirements_txt,
    packages=["win10toast"],
    license="Unknown",
    url="https://github.com/sakurai-youhei/Windows-10-Toast-Notifications",
    description=(
        "An easy-to-use Python library for displaying "
        "Windows 10 Toast Notifications"
    ),
    author="Jithu R Jacob",
    author_email="jithurjacob@gmail.com",
    maintainer="Youhei Sakurai",
    maintainer_email="sakurai.youhei@gmail.com",
)
