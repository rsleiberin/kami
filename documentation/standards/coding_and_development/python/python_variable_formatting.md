# Python Variable Naming Conventions

## Introduction
This document outlines the standards for naming variables in Python for Project Kami.

## General Guidelines
### Use Descriptive Names
Variable names should be descriptive enough to indicate the variable's purpose.

### Follow Pythonic Naming Conventions
Use `snake_case` for variable names, `PascalCase` for class names, and `UPPER_SNAKE_CASE` for constants.

### Avoid Single-Character Names
Except for loop indices or mathematical algorithms where the variable's purpose is clear.

### Use Prefixes Wisely
For example, use `is_`, `has_`, `num_`, etc., to make the variable's purpose clearer.

### Be Consistent
Use the same variable name for the same kind of data across different parts of the project.

### Avoid Names that Overlap with Built-in Types and Functions
For example, don't use `list`, `dict`, or `input` as variable names.

### Type Hints
Make use of Python's type hints to indicate the expected type of the variable.

### Global Variables
Should be avoided if possible, but if necessary, should be documented clearly.

### Immutable vs Mutable
Make it clear whether the variable should be mutable or immutable.
