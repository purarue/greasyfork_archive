import io
from setuptools import setup

with io.open("requirements.txt", "r", encoding="utf-8") as req_file:
    requirements = req_file.read().splitlines()

# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fo:
    long_description = fo.read()

setup(
    name="greasyfork_archive",
    version="0.1.4",
    url="https://github.com/purarue/greasyfork_archive",
    author="purarue",
    description=("""Scrape data from a users Greasyfork account"""),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    py_modules=["greasyfork_archive"],
    test_suite="tests",
    requires_python=">=3.9",
    install_requires=requirements,
    entry_points={"console_scripts": ["greasyfork_archive = greasyfork_archive:main"]},
    keywords="",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
