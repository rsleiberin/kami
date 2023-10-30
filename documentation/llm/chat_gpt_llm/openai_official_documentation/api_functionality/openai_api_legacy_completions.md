# OpenAI Completions API: Legacy Version

The legacy Completions API endpoint of OpenAI, updated last in July 2023, offers functionalities that differ from the more modern chat completions endpoint. Instead of structured message-based input, the legacy endpoint takes a simpler, freeform text string termed as a prompt.

## Using the Completions API

### Making a Basic API Call

The standard way to use the legacy Completions API is by providing a prompt to the model and receiving a completion in return. For instance:

\```python
response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Write a tagline for an ice cream shop."
)
\```

For a more detailed understanding, refer to the official API reference documentation.

### Token Log Probabilities

A notable feature of the Completions API is its ability to return log probabilities for the output tokens. This is particularly useful when trying to gauge the model's confidence in its own output. The number of log probabilities can be controlled using the `logprobs` field.

### Text Insertion

A unique advantage of the Completions endpoint is the support for text insertion. Instead of just providing a prefix (the standard prompt), users can also give a suffix. This is incredibly useful for:

- Drafting long-form content.
- Smooth transitions between paragraphs.
- Guiding the model through an outline or towards a specific conclusion.
- Code-related tasks, such as inserting content within a function or a file.

## Conclusion

Though succeeded by the Chat completions API, the legacy Completions API retains its unique features and advantages. It caters to specific use cases, especially when freeform prompts or text insertion capabilities are required.

