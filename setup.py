"""Setup for the isolator."""

from setuptools import setup

version = "0.1.0"

setup(
    name="isolator",
    version=version,
    description="Isolate a python class into a separate process",
    packages=["isolator"],
    python_requires=">=3.6",
    install_requires=[]
)
