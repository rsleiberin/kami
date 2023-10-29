# OpenAI Chat Completions API

The Chat completions API allows users to interact with OpenAI models in a conversational format. The API is designed to handle both single-turn tasks and multi-turn conversations, making it versatile for a range of applications.

## Overview

- The API uses chat models which take a list of messages as input and return a model-generated message as output.
- While designed for multi-turn conversations, it's equally efficient for single-turn tasks without conversation.

## Example Usage

Here's a sample API call demonstrating how to use the Chat completions API with the `gpt-3.5-turbo` model:

```python
import openai

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```


The `messages` parameter is a list of message objects. Each message object has a `role` (which can be `system`, `user`, or `assistant`) and a `content` which contains the text of the message from that role. The system role is typically used to set the behavior of the assistant.

The model responds based on the conversation history provided in the `messages` parameter. In the above example, the model would generate an appropriate response to the question "Where was it played?".

