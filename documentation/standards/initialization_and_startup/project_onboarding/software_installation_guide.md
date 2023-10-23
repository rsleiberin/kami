# Software Installation Guide

## Introduction
This guide is intended to help both human developers and AI agents set up the necessary software environment for working on Project Kami. Follow these instructions to ensure that your local machine is correctly configured.

## Prerequisites
- A computer running Ubuntu (Other operating systems will be covered soon)
- Internet access (for downloading software packages)
- Basic knowledge of command-line operations

## Software Requirements
- Python 3.x
- Git
- Virtualenv for Python environment isolation

## Installation Steps

### Python
1. Run `sudo apt update` and `sudo apt upgrade` to update package lists and installed packages.
2. Install Python by running `sudo apt install python3`.
3. Verify the installation by running `python3 --version` in the terminal.

### Git
1. Install Git by running `sudo apt install git` in the terminal.
2. Verify the installation by running `git --version` in the terminal.

### Virtualenv
1. Install virtualenv by running `pip3 install virtualenv` in the terminal.
2. Verify the installation by running `virtualenv --version` in the terminal.

## Environment Setup
To activate the Project Kami environment:
1. Navigate to the project directory.
2. Run `source kami/bin/activate`.

## Installing Dependencies
1. Make sure you are in the root project directory where `requirements.txt` is located.
2. Run `pip install -r requirements.txt` to install the required Python packages.

## Verification
To ensure that all software has been correctly installed and the environment is set up:
1. Open a new terminal window.
2. Run the following commands:
   - `python3 --version`
   - `git --version`
   - `virtualenv --version`

If all commands return a version number, your environment is set up correctly.

## Next Steps
After successfully setting up your environment and installing dependencies, proceed to `project_workflow.md` to understand how to effectively contribute to Project Kami.
