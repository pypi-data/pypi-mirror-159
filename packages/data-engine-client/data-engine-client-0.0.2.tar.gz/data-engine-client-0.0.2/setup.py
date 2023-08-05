import os

from setuptools import setup


class InstallError(Exception):
    pass


if not os.getenv("PIP_IGNORE_INSTALL_PACKAGE_ERROR"):
    raise InstallError("Error: you are pip installing the wrong package, check config")

setup(
    name="data-engine-client",
    version="0.0.2",
)
