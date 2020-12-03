#!/usr/bin/env python3


import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()
    
    
setuptools.setup(
    name="sbash",
    version="0.0.1",
    author="glozanoa",
    author_email="glozanoa@uni.pe",
    description="Simple Python interprete for bash.",
    long_description=long_description,
    #long_description_content_type="text/markdown",
    url="https://github.com/wtchdog/pybash",
    install_requires = [
        'cement',
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
