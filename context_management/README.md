# Project Kami - Context Management

## Introduction
The Context Management module in Project Kami is pivotal in establishing and maintaining the cognitive loops of agents, providing them with dynamic context windows to guide their thoughts and actions. This system is designed with the foresight to accommodate multiple types of agents, including Kami, which are persistent agents in continuous loops, and sub-agents which may have specific tasks and may or may not control their own contexts. It's a foundational block that ensures the evolution of agents and their interactions in a multi-agent environment, catering both to humans and AIs.

## Status
- `In Progress`

## Tasks
- [ ] Read and adhere to the guidelines in `documentation/standards/coding_and_development/coding_workflow.md`.
- [ ] Research and design the structure for handling multiple types of agents.
- [ ] Develop a system to establish and control the cognitive loop of agents.
- [ ] Design the database structure for agent memories and context handling.
- [ ] Initialize necessary directories and files based on the parent README's specification.
- [ ] Populate all sub-directories with `documentation/templates/README_template.md`, adding any relevant information at the time of population.
- [ ] Implement class structures as specified in `class_structure.md` from the `coding_and_development` standards.
- [ ] Update the README to mark the status of each task as "In Progress", "COMPLETED", or "PENDING".
- [ ] Start each code file with high-level pseudo-code and iterate until complete, following `documentation/standards/coding_and_development/iterative_development.md`.
- [ ] After coding, perform unit tests as specified in `documentation/standards/coding_and_development/testing_procedure.md`.
- [ ] Check code for standards adherence using `standards_checklist.md` from the `documentation/templates` directory.
- [ ] If all tasks are completed, update the README status to "COMPLETED" here and in the parent directory as instructed by `documentation/standards/coding_and_development/README_updates`.

## Files
- `In Progress`: [context_window.py](./path/to/context_window.py) - Manages the active cognitive loop for agents.
- `In Progress`: [agent_types.py](./path/to/agent_types.py) - Defines different types of agents and their functionalities.

(Additional files will be added as the module progresses.)

## Directories
- `In Progress`: [kami_agents](./path/to/kami_agents) - Houses the logic and functionalities for Kami agents.
- `In Progress`: [sub_agents](./path/to/sub_agents) - Contains the functionalities for sub-agents.

## Special Considerations
### For Humans
Ensure to keep the flexibility and scalability in mind while developing, as the system is designed to accommodate an evolving number of agents and functionalities.

### For AIs
Remember the distinction between different agent types and ensure the correct context window is applied for each type.
