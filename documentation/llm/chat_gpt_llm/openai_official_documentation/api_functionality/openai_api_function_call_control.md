# OpenAI Chat Completions API: Controlling Function Calls

When interacting with the Chat completions API and leveraging function calling, it's essential to understand how to control and mitigate undesired behaviors. This document outlines strategies to prevent hallucinated outputs and guide the model's decision-making during function calls.

## Handling Hallucinated Outputs

Hallucinations can occur when the model generates outputs that aren't aligned with the provided functions or expected results. To mitigate this:

1. **System Messages**: Use a system message to guide the model's behavior. For example, if the model uses functions not provided, instruct it with: "Only use the functions you have been provided with."
2. **Review Function Definitions**: Ensure that the functions you provide to the model are clearly defined, with concise descriptions and parameters.

## Guiding Model Decisions

The model's behavior during function calls can be influenced in several ways:

1. **Send Function Response**: After calling a function, send its response back to the model. The model can then decide the next steps, whether it's generating a user-facing message or making another function call.
2. **Chained Function Calls**: The model can chain multiple function calls based on a single user query. For instance, a query like “Find the weather and book dinner” might lead the model to call both the weather and booking functions consecutively.
3. **Forcing a Function Call**: If you want the model to specifically call a function, set `function_call` to `{"name": "<insert-function-name>"}`.
4. **User-Facing Message**: To make the model generate a direct response without calling a function, set `function_call` to `"none"`.
5. **Default Behavior**: By default (`function_call: "auto"`), the model decides whether to call a function and which one to call.

## Conclusion

Controlling the model's behavior during function calls ensures more accurate and desired outputs. By understanding and leveraging these strategies, developers can create more reliable and user-friendly applications with the Chat completions API.

