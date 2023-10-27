# Commenting Guidelines for Project Kami

## Introduction
This document outlines the guidelines for adding comments to the codebase of Project Kami. Comments are essential for understanding the functionality, purpose, and quirks of the code. Both human developers and AI agents are expected to adhere to these guidelines.

## General Principles

### Clarity Over Redundancy
Comments should clarify code; they should never restate what is already obvious from the code itself.

### Be Concise
Comments should be short and to the point, conveying essential information without unnecessary verbosity.

### Keep Up-to-Date
Comments should be updated alongside the code they describe. Outdated comments can be more harmful than no comments at all.

## Types of Comments

### Single-Line Comments
Use single-line comments for brief explanations or for code that is easy to understand. In Python, single-line comments start with `#`.

\`\`\`python
# This is a single-line comment
\`\`\`

### Multi-Line Comments
Use multi-line comments for detailed explanations or for complex blocks of code. In Python, multi-line comments can be created using triple quotes.

\`\`\`python
"""
This is a multi-line comment
that spans multiple lines.
"""
\`\`\`

### Inline Comments
Use inline comments sparingly and only when needed to explain a complex line of code. Place inline comments at the end of the line they describe.

\`\`\`python
result = perform_calculation(x, y)  # This comment explains what perform_calculation does
\`\`\`

## Special Comments

### TODOs
Use `TODO` comments for code that is temporary, a short-term solution, or good enough but not perfect. Always include the name of the person who can provide more details.

\`\`\`python
# TODO: Replace this algorithm with a more efficient one (Author Name)
\`\`\`

### FIXMEs
Use `FIXME` comments for code that is broken and needs to be fixed immediately.

\`\`\`python
# FIXME: This function sometimes returns None (Author Name)
\`\`\`

## Conclusion
Adhering to these commenting guidelines will ensure that the codebase remains understandable and maintainable. This is crucial for the long-term success and scalability of Project Kami.
