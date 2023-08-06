# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="linecheck",
    version="0.1.0",
    author="Nikhil Woodruff",
    author_email="nikhil@policyengine.org",
    description="Utility to check line endings.",
    license="http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    install_requires=[
        "pathlib",
        "argparse",
    ],
    extras_require={
        "dev": [
            "setuptools",
            "wheel",
        ],
    },
    entry_points={
        "console_scripts": ["linecheck=linecheck:cli"],
    },
    packages=find_packages(),
)
