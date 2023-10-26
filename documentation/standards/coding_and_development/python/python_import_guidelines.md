# Python Import Guidelines for Project Kami

## Order of Imports
Follow PEP 8 standards for the order of imports:
  - Standard library imports
  - Related third-party imports
  - Local application/library-specific imports

You should also sort the imports lexicographically within these groups.

\```python
import os  # Standard library
import sys  # Standard library
import numpy as np  # Third-party library
from my_module import my_function  # Local application
\```

## Import Specificity
Always import only what you need. Instead of importing an entire module, import only the specific functions or classes you'll use.

\```python
from os.path import join  # Good
import os  # Not specific
\```

## Alias Naming
If you are using an alias for an import, make sure it's a widely-accepted alias or makes the code clearer.

\```python
import numpy as np  # Widely-accepted alias
\```

## Circular Dependencies
Be cautious of circular dependencies. If two modules are dependent on each other, consider refactoring.

## Commenting Imports
If an import is not self-explanatory, include a comment explaining what it's used for.

\```python
from sklearn.tree import DecisionTreeClassifier  # For decision tree algorithm
\```

## Import Statements Length
If an import statement exceeds the maximum line length, break it down into multiple lines.

\```python
from my_module import (function_one,
                       function_two,
                       function_three)
\```

## Dynamic Imports
Use dynamic imports only if absolutely necessary and ensure they are handled safely.

\```python
# Avoid
module = __import__('module_name')

# Prefer
import importlib
module = importlib.import_module('module_name')
\```

## Deprecation and Future Updates
Periodically check for deprecated modules or functions and update them.

## Versioning
Make sure to note the version of third-party libraries if your code is tightly coupled with it.

## Special Considerations for AIs
For AI agents parsing these guidelines, focus on understanding the import types and their sequence, as this will aid in determining dependencies and module relationships.
