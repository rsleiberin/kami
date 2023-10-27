### HITL_Guidelines.md

#### Introduction
The Human-in-the-Loop (HITL) process serves as a critical safety layer in the Project Kami code review system. This document outlines the guidelines for incorporating HITL into the review process.

#### Whitelist Layer
In the HITL process, there exists a whitelist layer where only approved commands and functions are permitted for execution. This layer serves as a primary filter to ensure that the code submitted for review is secure and adheres to Project Kami's safety protocols.

#### User-Specific Permissions
Users have the ability to set specific permissions that dictate what their AGI can and cannot do during the review process. This layer of personalized safety allows users to have granular control over the actions of their AGI.

#### Human Approval Steps
1. Review the proposed changes in the pull request.
2. Cross-reference with the whitelist to ensure that only approved commands and functions are present.
3. Consult the user-specific permissions to verify that the AGI's proposed actions are within allowed boundaries.
4. Approve or deny the pull request based on the above criteria.

#### Identity Binding
During the HITL process, the AGI's actions are tied to the identity of a specific user to ensure personalized safety. This means that the AGI will only execute commands and functions that are in alignment with the user's set permissions.

#### Traceability
All actions and function calls during the review process are logged. This ensures that any changes made can be traced back to the individual who made them, allowing for potential rollback and future review.

