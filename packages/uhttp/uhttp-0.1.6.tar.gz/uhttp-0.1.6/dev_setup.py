from setuptools import setup
from pathlib import Path

"""
For testing packages...
    - copy this file to root of project folder
    - adjust <> parameters below
    - run ``python dev_setup.py install``
"""

def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [str(path.parent) for path in Path(package).glob("**/__init__.py")]

setup(
    name="uhttp",
    python_requires=">=3.8",
    version="0.0.2",
    license="MIT",
    description="",
    author="Chris Newville",
    author_email="chrisnewville1396@gmail.com",
    packages=get_packages("uhttp"),
    zip_safe=False,
    install_requires=[
    ],
)