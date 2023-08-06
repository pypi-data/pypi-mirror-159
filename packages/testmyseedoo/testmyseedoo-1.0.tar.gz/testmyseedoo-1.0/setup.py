from setuptools import setup, find_namespace_packages, find_packages

setup(
    name="testmyseedoo",
    version="1.0",
    description='this package contains tools for conversion model to engine and get inference with it',
    packages=find_namespace_packages(include=['seedoo*']) + find_packages()
)
