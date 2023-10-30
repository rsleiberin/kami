# OpenAI Completions API: Response Format

The legacy Completions API of OpenAI provides structured responses which can be easily interpreted and utilized. 

## Understanding the Response Format

### Basic Response Structure

An illustrative completions API response is as shown:

\```json
{
  "choices": [
    {
      "finish_reason": "length",
      "index": 0,
      "logprobs": null,
      "text": "\n\n\"Let Your Sweet Tooth Run Wild at Our Creamy Ice Cream Shack"
    }
  ],
  "created": 1683130927,
  "id": "cmpl-7C9Wxi9Du4j1lQjdjhxBlO22M61LD",
  "model": "gpt-3.5-turbo-instruct",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 16,
    "prompt_tokens": 10,
    "total_tokens": 26
  }
}
\```

To extract the output in Python, use: \```python response['choices'][0]['text'] \```.

This format bears similarities to the Chat completions API's response. However, it also includes the optionally available `logprobs` field.

### Differentiating Between Chat Completions and Completions

Though similar, there are subtle differences between the Chat completions and Completions API:

1. **Format of Requests**: Chat completions typically involve a list of messages, while Completions use a simple prompt.
2. **Translation Example**:
   - Completions: `Translate the following English text to French: "{text}"`
   - Chat completions: \```json [ {"role": "user", "content": 'Translate the following English text to French: "{text}"'}] \```
3. **Flexibility**: While the Completions API can simulate a chat format by adjusting the input, the Chat completions API is inherently designed for conversational exchanges.
4. **Underlying Models**: The main distinction comes from the GPT models available for each endpoint. The Chat completions API provides access to the highly capable `gpt-4` and cost-efficient `gpt-3.5-turbo`.

