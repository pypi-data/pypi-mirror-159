from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="extraspaceremover",
    version="0.0.1",
    author="Hassane Abida",
    author_email="abidahass.uca@gmail.com",
    url="https://github.com/has-abi",
    description="Remove extra spaces from a text",
    py_modules=["spaceremover"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent"
        ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
)