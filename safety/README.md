# Project Kami - Safety & Permissions System

## Introduction
The Safety & Permissions System ensures the security and robustness of Project Kami's operations. It incorporates various layers of protection, including a whitelist layer, user-specific permissions, human-in-the-loop checks, identity binding, traceability, and dynamic risk assessment. This directory oversees every operation, vetting each action against the established safety protocols, and ensures the secure execution of all functions.

## Status
- `In Progress`

## Tasks
- [ ] Read and adhere to the guidelines in `documentation/standards/coding_and_development/coding_workflow.md`.
- [ ] Document and maintain the Whitelist Layer for universally approved operations.
- [ ] Implement the User-Specific Permissions Layer allowing customization of AGI boundaries.
- [ ] Develop the Human-in-the-Loop Layer as a fail-safe for specific actions.
- [ ] Ensure AGI's core-level Identity Binding for personalized safety.
- [ ] Establish a logging system for Traceability of all actions and function calls.
- [ ] Build a Dynamic Risk Assessment mechanism for real-time evaluation based on risk scores.
- [ ] Review, digest, and integrate requirements from the deprecated files.
- [ ] Regularly review and update all safety protocols.
- [ ] Test the system against potential edge cases for robustness.
- [ ] Plan documentation requirements for the `documentation` directory.
- [ ] Update the README as tasks progress.

## Files
- `Depreciated`: [audit_and_rollback.py](./audit_and_rollback.py)
- `Depreciated`: [dynamic_whitelist.py](./dynamic_whitelist.py)
- `Depreciated`: [function_execution.py](./function_execution.py)
- `Depreciated`: [human_in_the_loop.py](./human_in_the_loop.py)
- `Depreciated`: [permission_management.py](./permission_management.py)
- `Depreciated`: [user_permissions.json](./user_permissions.json)

## Directories
- `In Progress`: [pseudos](./pseudos) - Contains the logic behind each function for the safety system.

## Special Considerations
### For Humans
Prioritize safety at all times. Ensure that every new feature, change, or operation undergoes rigorous safety checks before implementation.

### For AIs
Strictly adhere to the established safety layers. Always report any anomalies or suspicious requests and never bypass safety protocols.
