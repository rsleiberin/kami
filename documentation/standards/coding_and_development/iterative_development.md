# Project Kami Iterative Development Guidelines

## Introduction
This document aims to guide both human developers and AI agents through the iterative development process within Project Kami. It outlines the stages involved in the development of any new feature, class, or module.

## Iterative Development Phases

### 1. Plan and Define Scope
- Clearly outline the high-level tasks and objectives.
- Use README files to capture these tasks and their current status.

### 2. First Pass: High-Level Pseudo-Code
- Create a high-level pseudo-code representation of the solution.
- This should be done within the respective files in a directory dedicated to the new feature, class, or module.

### 3. Second Pass: Low-Level Pseudo-Code
- Transform the high-level pseudo-code into more detailed, low-level pseudo-code.
- Identify any utility functions, classes, or modules that need to be created or updated.

### 4. Third Pass: Initial Code
- Translate the low-level pseudo-code into initial functional code.
- Mark incomplete or uncertain sections with TODO comments.

### 5. Subsequent Passes
- Refine the code in iterative passes, each time improving clarity, efficiency, and completeness.
- Perform unit tests and update TODO comments as sections get completed.

### 6. Standards and Review
- Once a feature, class, or module is functionally complete, perform a standards check using `standards_checklist.md`.
- Revise according to checklist and recheck until it aligns with Project Kami standards.

## Human-AI Collaboration
- The human sets high-level tasks and directions.
- The AI assists in breaking down these tasks and performs the coding, adhering to the guidelines set forth in this document.

## Conclusion
The iterative development approach allows for flexibility and adaptability, making it easier to incorporate changes and improvements during the development process. Following these guidelines will ensure a more streamlined, efficient, and effective development process in Project Kami.
