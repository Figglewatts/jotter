"""setup.py

The setup script of jotter.

Author:
    Figglewatts <me@figglewatts.co.uk>
"""

from os import path
from setuptools import setup, find_packages

here = path.join(path.dirname(__file__))


def get_repo_file_content(filename: str) -> str:
    with open(path.join(here, filename), encoding="utf-8") as f:
        return f.read()


setup(
    name="jotter",
    version="0.1.3",
    description="Note taking and syncing utility.",
    long_description=get_repo_file_content("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/Figglewatts/jotter",
    author="Figglewatts",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha", "Operating System :: OS Independent"
    ],
    keywords="note taking syncing",
    packages=find_packages("."),
    entry_points="""
        [console_scripts]
        jotter=jotter.cli:jotter
    """,
    python_requires=">=3.7",
    install_requires=[
        "click~=7.1.2", "appdirs~=1.4.4", "marshmallow~=3.7.1", "pyyaml>=5.3.1,<5.5.0"
    ],
)
