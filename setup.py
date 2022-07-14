__author__ = "Maicon Domingues"
__email__ = "dominguesm@outlook.com"

from setuptools import find_packages, setup

with open("./README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="respunct",
    version="1.0.0",
    author="Maicon Domingues",
    author_email="dominguesm@outlook.com",
    description="An easy-to-use package to restore punctuation of portuguese texts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DominguesM/respunct",
    packages=find_packages(),
    license="Apache Software License",
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.7",
    install_requires=["simpletransformers==0.63.7", "torch==1.12.0"],
)