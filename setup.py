"""The license of each required packages is shown in the comments.
The information is from PYPI or its github site.
"""

import os
from pathlib import Path

import setuptools

_LONG_DESCRIPTION = Path(os.path.dirname(__file__)).joinpath("README.md").read_text()
_REQUIREMENTS = Path(os.path.dirname(__file__)).joinpath("requirements.txt").read_text()

setuptools.setup(
    name="sisa",
    version="1.0",
    author="Lei Wu",
    author_email="energynode@outlook.com",
    description="SISO Impedance-Based Stability Analysis",
    long_description=_LONG_DESCRIPTION,
    packages=setuptools.find_packages(),
    install_requires=_REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
