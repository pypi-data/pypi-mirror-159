from struct import pack
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="QrPypi",
    version="0.0.4",
    author="AcnSoft",
    description="QrPypi is a python package for creating a qrcode",
    long_description=long_description,
    long_description_content_type='text/markdown',
    package="qrpypi"
)