# Unique Method File Structure Guidelines

## Introduction
This document standardizes the unique method file structure employed in Project Kami. It serves as a comprehensive guide for both human developers and AI agents, aiming to facilitate modularity, ease of debugging, and scalability.

## Why Unique Method File Structure?
This approach allows for the highest level of modularity. Each method is isolated in its own file, making it easier for debugging, testing, and for AI agents to understand their operational context.

## Basic Structure
### Class Directories
Each class will reside in its own directory. The directory will contain:
- A base file named `<classname>_base` which includes the class definition.
- Separate files for each method in the class, named `<classname>_<method_name>` using snake_case.

### File Contents
Each method file should contain:
1. Import statements
2. A constant for the method's unique error code
3. The method itself
4. Any auxiliary functions or classes that support the method

### README
Each directory should contain a README file that follows a template located in `documentation/templates`. The README is essential for code consistency and completion.

### File and Directory Limitations
To adhere to context limitations, each directory should contain no more than 10 files or sub-directories combined.

### Standard Requirements
Every method should follow the standard requirements outlined in the utility functions and their respective language documentation.

## Version Control
Version control is managed through Git, with routine pushes to maintain the codebase.

## Special Considerations

### For Humans
- Stick to the structure rigorously.
- Make use of descriptive file and method names.
- Comment generously.

### For AIs
- AI agents should read the method file to understand the scope of their operations.
- Error codes are crucial for AIs to understand the failure points.

## Future Tasks
- Periodically review this document and the actual structure to ensure they are aligned.
- Include real-world examples to facilitate understanding.
