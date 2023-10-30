# OpenAI Chat Completions API: Function Calling Sequence

Function calling within the Chat completions API allows developers to trigger custom functions based on model interactions. The sequence provides a structured approach to handle user queries, execute functions, and relay the results back to the user.

## Function Calling Sequence

1. **Initial Model Call**: Send the user query to the model along with a set of defined functions.
2. **Model Function Choice**: The model may decide to invoke a function, generating a stringified JSON object adhering to your defined schema.
3. **Parse & Execute Function**: In your code, parse the string into JSON and execute the function with the provided arguments.
4. **Model Summarization**: Append the function's response as a new message and call the model again, letting the model relay the results to the user.

## Example Implementation

Below is a Python code example demonstrating the function calling sequence:

```python
import openai
import json

def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather for a location."""
    # ... [Code truncated for brevity]

def run_conversation():
    # ... [Code truncated for brevity]
    # The sequence involves:
    # 1. Sending the conversation and available functions to GPT.
    # 2. Checking if GPT opted to call a function.
    # 3. Executing the function.
    # 4. Sending the function response to GPT for summarization.

print(run_conversation())
```
This example demonstrates the integration of a simple get_current_weather function with the Chat completions API. Developers can adapt this sequence for more complex functions and applications.