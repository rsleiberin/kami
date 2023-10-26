### Python Commenting and Documentation Standards

## Introduction
Commenting and documentation are vital for understanding the flow and functionality of code, both for humans and for AI agents like the LLM in Project Kami. This document outlines the standards for commenting and documentation within Python code in the project.

## Inline Comments
- Use inline comments sparingly.
- Comments should be complete sentences.
- Use two spaces after a line of code for inline comments.
  
\```python
x = 5  # This is an inline comment explaining what x represents.
\```

## Block Comments
- Indent block comments to the same level as the code they describe.
- Use complete sentences with proper punctuation.
  
\```python
# This block comment describes what the following block of code does.
# Make sure to explain any complex operations to maintain readability.
for i in range(10):
    print(i)
\```

## Docstrings
- Always include a docstring at the start of a new Python file, class, or function.
- Use triple quotes for docstrings and align the closing quotes with the opening quotes.
- Docstrings must be immediately below the `def` or `class` line.

\```python
def example_function(param1, param2):
    """
    This docstring explains what the example_function does.
    Args:
        param1: Explain what param1 represents.
        param2: Explain what param2 represents.
    Returns:
        Explain what the function returns.
    """
    pass
\```

## Special Considerations for Project Kami
- In Project Kami, comments also serve to provide contextual information to the LLM. Therefore, comments may be more detailed than what is typical.
- Ensure comments are up-to-date with the code, especially after code refactoring.

## Best Practices
- Do not over-comment; it can make the code hard to read.
- Do not under-comment; it can make the code hard to understand.
- Always keep the target audience in mind while commenting. In the case of Project Kami, this includes both human developers and AI agents.
