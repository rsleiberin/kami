# Project Kami Debugging Practices

## Introduction
This document focuses on the specialized debugging approach of Project Kami, emphasizing real-time error tracking via print tracers. 

## Real-Time Debugging with Print Tracers
Project Kami employs print tracers for immediate error tracking and logging. For detailed guidelines on print tracers, refer to the document located at `documentatino/standards/coding_and_development/utility_functions/print_tracer.md`.

### For Humans
- Enable and monitor print tracers for real-time error tracking.
- Immediate feedback allows for swift issue resolution.

### For AIs
- Use real-time logs from print tracers for contextual understanding and error correction.

## Workflow
1. **Initialize Print Tracers**: Start print tracers in any function or method.
2. **Real-Time Monitoring**: Errors are logged automatically.
3. **Immediate Action**: Use real-time logs for quick corrections.

### Special Considerations
- Real-time logs serve as immediate feedback, facilitating quick iterations and self-improvement for both humans and AIs.
