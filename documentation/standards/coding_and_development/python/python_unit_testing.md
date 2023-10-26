# Python Unit Testing Guidelines for Project Kami

## General Testing Guidelines

For a comprehensive understanding of the testing lifecycle, including planning, execution, and review, please refer to the general testing guidelines located in `documentation/standards/debugging_and_testing/unit_testing_protocols.md`.


## Introduction
Unit testing is a key aspect of software quality assurance in Project Kami. This document outlines the guidelines and best practices for writing unit tests in Python. The unittest framework will be used for all Python unit testing.

## File Naming
Test files should mirror the directory and filename structure of the main project, with the addition of a `_test` suffix. For example, a file named `my_module.py` will have a corresponding test file named `my_module_test.py`.

## Template
A template to follow when writing unit tests can be found in the `documentation/templates/python_test_template.txt` directory. This template incorporates best practices, including the Arrange-Act-Assert (AAA) pattern and mocking utility functions.