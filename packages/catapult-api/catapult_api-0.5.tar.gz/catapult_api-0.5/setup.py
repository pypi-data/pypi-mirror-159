from setuptools import setup, find_packages

VERSION = "0.5"
DESCRIPTION = "Python API wrapper for Catapult GPS tracking system"

setup(
    name="catapult_api",
    version=VERSION,
    description=DESCRIPTION,
    packages=find_packages(),
)
