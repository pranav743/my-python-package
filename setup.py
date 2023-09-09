from setuptools import setup, find_packages

setup(
    name="pranav",
    version="0.1.0",
    description="A package for colorized printing and list printing",
    author="Pranav Patil",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "colorama",
    ],
)