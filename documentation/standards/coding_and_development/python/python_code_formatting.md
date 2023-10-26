# Python Code Formatting Guidelines

## Introduction
Proper code formatting is crucial for readability and maintainability of code. This document outlines the standard code formatting guidelines for Python development in Project Kami. Following these guidelines ensures that the codebase remains clean, consistent, and easy to read.

## Code Style
- Follow the PEP 8 style guide for Python code, unless otherwise specified.
- Use 4 spaces for indentation.

## Naming Conventions
- Use snake_case for variable names, function names, and filenames.
- Use PascalCase for class names.
- Constants should be in ALL_CAPS.

## Whitespace and Operators
- Use whitespace around operators and after commas for readability.
- Avoid extraneous whitespace in parentheses, brackets, or braces.

## Comments
- Inline comments should be used sparingly and must be relevant.
- Use docstrings for modules, classes, and functions.

## Line Length
- Limit lines to 79 characters for code.
- Exceptions can be made for comments and docstrings if longer lines are necessary for context, especially for AI readability. 

## Special Considerations for AI
Due to the AI's specific requirements for context, the following exceptions to standard guidelines apply:
- Comments and docstrings can exceed the standard PEP 8 line lengths if required for contextual understanding by the AI.

## Future Improvements
- [ ] Add examples demonstrating each formatting guideline.
- [ ] Provide a `.pylintrc` or similar configuration file for automated linting.
