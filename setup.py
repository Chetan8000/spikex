#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "jsonschema",
    "regex",
    "spacy==2.3.1",
    "wasabi",
    "typer",
]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

setup(
    author="Paolo Arduin",
    author_email="paolo.arduin@errequadrosrl.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="SPIKE - SpaCy Pipes for Knowldge Extraction",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="spike",
    name="spike",
    packages=find_packages(include=["spike", "spike.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/erre-quadro/spike",
    version="0.2.2-dev1",
    zip_safe=False,
)
