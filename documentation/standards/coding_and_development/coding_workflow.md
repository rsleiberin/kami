# Project Kami Coding Workflow Guidelines

## Introduction
This document outlines the standardized coding workflow for Project Kami. It is intended to serve as a blueprint for both human developers and AI agents to ensure efficient, modular, and maintainable code.

## Workflow Overview
The coding workflow in Project Kami is structured into distinct phases to manage the development process effectively.

### 1. Ideation and Planning
- Define high-level tasks in the README files.
- Use the `README_template` in `documentation/templates`
- Conduct interviews to gather architectural insights and decompose tasks into smaller units.

### 2. Directory and File Initialization
- Initialize necessary directories and files based on the high-level task README.
- Use the `class_structure.md` from this directory as a guide for initializing new directories.
- Update the README to mark the status of each task as "In Progress".

### 3. Code Development
- Begin with a high-level pseudo-code outline in each file.
- In iterative passes, transition from pseudo-code to functional code, marking incomplete sections with TODO comments.

### 4. Standards Adherence
- After completing a class or module, perform a standards check using the criteria in `standards_checklist.md` located in the `templates` directory.
- Revise the code according to the checklist and recheck until it aligns with Project Kami standards.

### 5. Version Control
- Commit changes to version control after each significant modification.
- Utilize clear, descriptive commit messages to document the purpose of each change.

## Human-AI Collaboration
- The human defines high-level tasks and sets the overall direction.
- The AI conducts interviews for more context and proposes mid-level and low-level tasks.
- The AI is responsible for code development, while the human reviews and approves or refines the changes.

## Advantages of Unique Method File Structure
- The unique method file structure offers maximum modularity by isolating each method in its own file.
- This isolation simplifies debugging, testing, and allows AI agents to grasp their operational context better.

## Conclusion
Adhering to this workflow will streamline the development process, reduce errors, and facilitate seamless collaboration between human developers and AI agents. Following these guidelines is crucial for achieving the goals of Project Kami.
