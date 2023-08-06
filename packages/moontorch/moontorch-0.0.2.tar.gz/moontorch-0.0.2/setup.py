from setuptools import setup, find_packages

base_packages = ["torch"]

setup(
    name="moontorch",
    version="0.0.2",
    packages=find_packages(),
    install_requires=base_packages,
)
