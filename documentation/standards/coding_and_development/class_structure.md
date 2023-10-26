# Project Kami Class Structure Guidelines

## Introduction
This document outlines the standard structure for classes in Project Kami. Following this structure ensures consistency and readability across the codebase, thereby facilitating collaboration among both human developers and AI agents.

## Structure Overview

### Base Class File
- The base class file, named `<classname>_base.py`, should contain the class definition and basic constructor.
- It should import all the methods from the separate method files.

### Method Files
- Each method should be in its own file named `<classname>_<method_name>.py`.
- The method files should reside in the same directory as the base class file.

### README
- Each class directory should contain a README that lists all the methods, their statuses, and other relevant information.

### Subclasses
- If a class has subclasses, each subclass should have its own directory within the parent class directory.
  
### Class Constraints
- To adhere to context limitations, each class directory should contain no more than 10 files or sub-directories combined.

## Versioning and Standards Adherence
- After completing a class, adhere to the guidelines in `standards_checklist.md` for a final standards check.

## Special Considerations

### For Humans
- Stick rigorously to the structure.
- Make use of descriptive file and method names.
- Comment generously for clarity.

### For AIs
- AI agents should consult the class README to understand the scope of their operations.
- Adhere strictly to the class structure guidelines for code consistency.

## Conclusion
By adhering to these class structure guidelines, we can ensure that the codebase remains consistent, modular, and easy to navigate for both human developers and AI agents.

