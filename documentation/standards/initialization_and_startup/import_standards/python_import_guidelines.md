# Python Import Guidelines for Project Kami

## Introduction
This document outlines the standards for importing modules and packages in Python code for Project Kami. Following these guidelines will ensure consistency, readability, and maintainability across the codebase.

## Basic Guidelines

### Absolute vs Relative Imports
- Use absolute imports over relative imports for clarity.
  \```python
  # Good
  import project_kami.module
  
  # Not Recommended
  from . import module
  \```

### Import Ordering
- Follow the PEP 8 guidelines for import ordering:
  1. Standard library imports
  2. Related third-party imports
  3. Local application/library-specific imports
  
  \```python
  # Example
  import os
  import sys
  
  import pandas as pd
  
  from project_kami import my_module
  \```

### Import Grouping
- Group imports in the following order and separate them by a blank line:
  1. `import` statements
  2. `from ... import ...` statements
  
  \```python
  # Example
  import os
  import sys
  
  from project_kami import my_module
  \```

### Aliasing
- Only use aliasing if the original name is too long or if the alias is widely recognized.
  \```python
  # Good
  import numpy as np
  
  # Not Recommended
  import my_very_long_module_name as m
  \```

## Advanced Guidelines

### Dynamic Imports
- Use dynamic imports (`importlib.import_module()`) only when absolutely necessary and document the reason.

### Circular Dependencies
- Avoid circular dependencies by restructuring your code or using `import ... as ...` within functions or methods.

## Special Considerations for AI Agents

- AI agents should be programmed to recognize and adhere to these import guidelines during code generation and refactoring tasks.
