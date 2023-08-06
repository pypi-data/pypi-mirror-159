import pathlib
from setuptools import setup, find_packages
from distutils.spawn import find_executable
import platform


def readme():
    with open('README.md') as f:
        return f.read()


dependencies = ['pyperclip', 'click', 'appdirs', 'daemonize']
if find_executable("fswatch") is None:
    if platform.system() == "Linux":
        dependencies.append("inotify")
    else:
        raise ValueError(
                "inkscape-figures needs fswatch to run on MacOS. You "
                "can install it using `brew install fswatch`"
                )

setup(
    name="inkscape-figures-vscode",
    version="1.0.7",
    description="Script for managing inkscape figures (VsCode version created by gillescastel, modified by sleepymalc)",
    long_description="Original package: https://github.com/gillescastel/inkscape-figures \n modified main.py file: https://github.com/sleepymalc/VSCode-LaTeX-Inkscape/tree/main/Inkscape-setting/Inkscape-figure-manager ",
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=['inkscapefigures'],
    scripts=['bin/inkscape-figures'],
    install_requires=dependencies,
    include_package_data=True
)
