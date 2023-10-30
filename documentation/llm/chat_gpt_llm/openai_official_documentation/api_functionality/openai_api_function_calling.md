# OpenAI Chat Completions API: Function Calling

Function calling with the Chat completions API allows for a structured interaction with models, enabling developers to define functions and retrieve JSON objects in response, suitable for direct application in code.

## Introduction

- The models `gpt-3.5-turbo-0613` and `gpt-4-0613` are adept at detecting when a function should be invoked based on input and can respond with JSON adhering to the function's signature.
- The API does not execute the function, but rather the model generates JSON which developers can use to implement the function in their code.

## Key Considerations

- **Potential Risks**: Given the capability to generate structured responses, there's potential for actions that have real-world implications. Developers are urged to have user confirmation flows before executing impactful actions.
- **Billing & Context Limit**: Function definitions and documentation count towards the model's context limit and are billed as input tokens. To manage context limits, consider limiting the number of functions or shortening documentation.

## Function Calling Advantages

Function calling can be leveraged to:

1. **Create Chatbots**: Develop bots that answer questions by interfacing with external APIs. Examples include functions like `send_email(to: string, body: string)` or `get_current_weather(location: string, unit: 'celsius' | 'fahrenheit')`.
2. **Convert Natural Language into API Calls**: Transform questions like "Who are my top customers?" into structured calls like `get_customers(min_revenue: int, created_before: string, limit: int)`.
3. **Extract Structured Data**: Extract specific data from text using functions like `extract_data(name: string, birthday: string)` or `sql_query(query: string)`.

Function calling provides a structured and efficient means to interact with the model, enabling a wide range of applications.

