# Project Kami - LLM (Large Language Model) Directory

## Introduction
The LLM directory houses the logic and infrastructure for various Large Language Models. This module is essential for routing and processing requests to different LLMs, ensuring concurrency and simultaneous interactions. It serves as the backbone for Project Kami's modular AGI system, catering to both human developers and AI agents.

## Status
- `In Progress`

## Tasks
- [ ] Read and adhere to the guidelines in `documentation/standards/coding_and_development/coding_workflow.md`.
- [ ] Design the architecture for the LLM switcher and instance management.
- [ ] Implement asynchronous programming for overlapping API calls.
- [ ] Define the API structure and functionalities for each LLM.
- [ ] Develop methods for concurrent processing and request routing.
- [ ] Establish protocols for dynamic allocation of resources to specific LLMs.
- [ ] Populate all sub-directories with `documentation/templates/README_template.md`, adding any relevant information at the time of population.
- [ ] Implement class structures as specified in `class_structure.md` from the `coding_and_development` standards.
- [ ] Update the README to mark the status of each task as "In Progress", "COMPLETED", or "PENDING".
- [ ] Start each code file with high-level pseudo-code and iterate until complete, following `documentation/standards/coding_and_development/iterative_development.md`.
- [ ] After coding, perform unit tests as specified in `documentation/standards/coding_and_development/testing_procedure.md`.
- [ ] Check code for standards adherence using `standards_checklist.md` from the `documentation/templates` directory.
- [ ] If all tasks are completed, update the README status to "COMPLETED" here and in the parent directory as instructed by `documentation/standards/coding_and_development/README_updates`.

## Files
- `In Progress`: [LLM Switcher](./llm_switcher.py) - Logic for routing and managing different LLM instances.
- `PENDING`: [API Structure](./api_structure.py) - Defines the API functionalities for each LLM.

## Directories
- `In Progress`: [ChatGPT](./chat_gpt_llm) - Houses the functionalities and logic for the ChatGPT LLM.
- `PENDING`: [Other LLMs](./other_llms) - Directory for other LLMs as they get integrated.

## Special Considerations
### For Humans
Ensure that the LLMs are modular and can be seamlessly interchanged. Maintain a clear distinction between functionalities of each LLM.

### For AIs
Adhere strictly to the specified directory structure and design guidelines. Make sure to consult the README for context and task prioritization. Ensure asynchronous operations for overlapping tasks.
