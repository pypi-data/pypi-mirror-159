from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.1'
DESCRIPTION = 'An image recognition package.'

# Setting up
setup(
    name="pyrecog",
    version=VERSION,
    author="FullStackJosh",
    author_email="joshuafxs@yahoo.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pyautogui'],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)