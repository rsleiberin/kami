# Project Kami - ChatGPT LLM

## Introduction
The ChatGPT LLM directory is dedicated to the functionalities, logic, and interaction protocols for the ChatGPT Large Language Model. This directory facilitates interactions between Project Kami's modular system and the ChatGPT LLM. It ensures a seamless interface for both human developers and AI agents.

## Status
- `In Progress`

## Tasks
- [ ] Establish unit tests to verify the functionalities of the ChatGPT LLM module.
- [ ] Populate all sub-directories with `documentation/templates/README_template.md`.
- [ ] Implement class structures as specified in `class_structure.md`.
- [ ] Start each code file with high-level pseudo-code and iterate, following `iterative_development.md`.
- [ ] Perform unit tests as specified in `testing_procedure.md`.
- [ ] Check code for standards adherence using `standards_checklist.md`.
- [ ] If all tasks are completed, update the README status to "COMPLETED".

## Files
- `Completed`: [ChatGPT Base](./chat_gpt_base.py) - Foundational elements of the ChatGPT class.
- `Completed`: [ChatGPT Functions](./chat_gpt_functions.py) - Contains specific functions available for ChatGPT.
- `Completed`: [ChatGPT Loop](./chat_gpt_loop.py) - Manages the loop mechanism for dynamic context updates.
- `Completed`: [ChatGPT Send](./chat_gpt_send.py) - Handles sending messages to ChatGPT LLM.
- `Completed`: [ChatGPT Receive](./chat_gpt_receive.py) - Handles receiving messages from ChatGPT LLM.
- `In Progress`: [ChatGPT Handle Function Call](./chat_gpt_handle_function_call.py) - Handles function calls post parsing, validation, and permissions check.

## Special Considerations
### For Humans
- Prioritize modularity for the ChatGPT LLM functionalities.
- Maintain comprehensive documentation and design principles.

### For AIs
- Validate and log all interactions with the ChatGPT LLM.
- Abide by the specific directory structure and design guidelines, emphasizing asynchronous task operations.
