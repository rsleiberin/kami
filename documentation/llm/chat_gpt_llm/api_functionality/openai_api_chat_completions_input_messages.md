# OpenAI Chat Completions API: Understanding the `messages` Parameter

The `messages` parameter is central to the Chat completions API. It dictates the flow of conversation and instructs the model on how to behave and respond.

## Structure of Messages

The `messages` parameter must be an array of message objects. Each message object consists of:

- `role`: Can be "system", "user", or "assistant".
- `content`: The actual content of the message from the respective role.

## Typical Conversation Format

Typically, conversations start with a system message, followed by alternating user and assistant messages. The order is significant:

1. **System Message**: Sets the behavior of the assistant. It's optional but can be used to modify the personality or provide specific behavior instructions. Without it, the model behaves as if given a generic instruction like "You are a helpful assistant."
2. **User Messages**: These are the requests or comments from the user which the assistant responds to.
3. **Assistant Messages**: Primarily store previous assistant responses but can also be given by the developer to guide the model towards desired behavior.

## Importance of Conversation History

It's essential to include the conversation history, especially when user instructions or questions refer to prior messages. Since models don't retain past requests' memory, the conversation's context needs to be present in the history. If the conversation exceeds the model's token limit, it must be abbreviated.

## Mimicking Iterative Responses

To achieve a progressive or iterative response effect, similar to how ChatGPT operates, you can use the `stream` parameter and set it to `true`.

