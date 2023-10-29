# OpenAI API Essentials for Project Kami

## Introduction
OpenAI offers a suite of models that utilize advanced natural language processing capabilities. This document encapsulates the fundamental concepts and features of OpenAI's API tailored for Project Kami's requirements.

## Core Concepts

### Generative Pre-trained Transformers (GPTs)
GPTs are neural network models designed to understand and generate text, including natural language and code. They operate based on prompts, which instruct them on the desired task. These models are versatile and can be employed for diverse tasks ranging from generating content to engaging in conversation.

### Data Embeddings
Embeddings are mathematical representations of data, typically text, in vector form. They capture and preserve the essence or meaning of the data, making them invaluable for tasks that require understanding context, such as search functions, recommendations, or categorization.

### Text Tokens
Tokens are the building blocks GPT models use to process and understand text. In essence, they break down text into manageable chunks. On average, a token represents a sequence equating to approximately 4 characters or 0.75 English words.

## Constraints and Limitations
- GPT models are bound by a maximum context length, which determines the amount of text (prompts and outputs) they can handle in a single interaction.
- Similarly, embedding models are also constrained by a maximum input length.

## Deterministic Behavior
It's essential to note that OpenAI models exhibit non-deterministic behavior by default. This means that even with identical input prompts, the model might generate different responses on separate occasions. However, adjusting the temperature setting to 0 can make the model's outputs primarily deterministic, with minimal variability.
