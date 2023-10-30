# OpenAI Chat Completions API Response Format

When making a request to the Chat completions API, the API returns a structured response. This document outlines the format of that response and how to interpret it.

## Example Response

An example of a Chat completions API response is shown below:

\```json
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
        "role": "assistant"
      }
    }
  ],
  "created": 1677664795,
  "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
  "model": "gpt-3.5-turbo-0613",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 17,
    "prompt_tokens": 57,
    "total_tokens": 74
  }
}
\```

(Note: Remove the extra backslashes before the backticks to render correctly in markdown.)

## Extracting the Assistant’s Reply

To extract the content of the assistant's response from the API reply, you can use the following Python code:

\```python
response_content = response['choices'][0]['message']['content']
\```

## Finish Reasons

Every response will include a `finish_reason`. The possible values for `finish_reason` are:

- `stop`: API returned a complete message or terminated by one of the stop sequences provided via the stop parameter.
- `length`: Incomplete model output due to the `max_tokens` parameter or token limit.
- `function_call`: The model decided to call a function.
- `content_filter`: Content omitted due to a flag from OpenAI's content filters.
- `null`: API response is still in progress or incomplete.

## Additional Notes

Depending on the input parameters (like if functions are provided), the model response may contain different fields or information.

