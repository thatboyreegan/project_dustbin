"""trashify setup"""

from setuptools import setup, find_packages

VERSION = "1.0.0"


# Setting up
setup(
    # the name must match the folder name 'trashify'
    name="trashify",
    version=VERSION,
    author="Brian Kimathi",
    author_email="<bryo.kim1@gmail.com>",
    # description=DESCRIPTION,
    # long_description=LONG_DESCRIPTION,
    packages=find_packages(exclude=["test*"]),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=["python", "documentation"],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
