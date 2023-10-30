# Strategies for Optimized Use of GPT

## Provide Reference Text

GPT models have a known tendency to fabricate or invent answers, especially when confronted with niche topics or when asked to provide citations and URLs. However, just as a student can perform better in an examination with some notes, providing GPT with reference text can help it produce more accurate and less fabricated answers.

**Tactics**:
- **Use a Reference Text**: Instruct the model to base its answers on a given reference text.
  
- **Cite from the Reference Text**: Ask the model to provide citations or sources from the reference text to support its answers.

## Split Complex Tasks into Simpler Subtasks

Breaking down a complex system into modular components is a standard best practice in software engineering. Similarly, GPT models can more accurately handle complex tasks when they are broken down into simpler, more manageable subtasks. By redefining a complex task into a series of simpler tasks, the outputs from earlier tasks can be used as inputs for subsequent tasks, resulting in a more accurate overall output.

**Tactics**:
- **Intent Classification**: Identify the most relevant instructions for a user query.
  
- **Manage Long Dialogues**: For applications that involve extended dialogues, consider summarizing or filtering previous interactions.
  
- **Recursive Summarization**: Summarize lengthy documents in segments, then create a complete summary by piecing together the individual summaries.

## Give GPTs Time to "Think"

Similar to humans who may need a moment to solve a complex mathematical operation, GPT models also benefit from having some "thinking" time. When forced to produce an immediate answer, the models are more prone to making errors. However, if they are given some time or are instructed to follow a reasoning chain before producing an answer, the results are more reliable.

**Tactics**:
- **Work Out the Answer**: Ask the model to reason out its solution rather than jump to conclusions.
  
- **Inner Monologue**: Use an inner monologue or a sequence of queries to guide the model's thought process.
  
- **Review and Revise**: After providing an answer, ask the model to review its response and check if it missed anything on prior passes.
