Class Name: ChatGPTAssistant
Purpose: To serve as the central connector for ChatGPT logic, managing the context and facilitating communication between the user and ChatGPT.
Methods: 
    - loop: Manages the main interaction loop between the user and ChatGPT.
    - send_to_chat_gpt: Sends user input to ChatGPT and fetches the response.
    - receive_from_chat_gpt: Handles the response received from ChatGPT.
Attributes:
    - api_key: Holds the API key for authenticating with OpenAI.
    - system_message: A system message to be sent to ChatGPT.
    - context_manager: Manages the context for the ChatGPT Assistant.
Pseudo Code:
    Constructor:
        1. Set the API key from the configuration.
        2. Initialize the system message with a standard instruction.
        3. Instantiate the ContextManager for managing the context.
    loop:
        1. Start an infinite loop to continuously interact with the user.
        2. Capture user input.
        3. If the user input is not empty, fetch the current context.
        4. Send the user input along with the context to ChatGPT via send_to_chat_gpt method.
        5. Handle the response from ChatGPT using the receive_from_chat_gpt method.
        6. If an error occurs or a KeyboardInterrupt is detected, exit the loop.
    send_to_chat_gpt:
        1. Set the OpenAI API key.
        2. Prepare the messages and function call structure for sending to ChatGPT.
        3. Send the prepared messages and function call structure to ChatGPT.
        4. Parse the response from ChatGPT to extract either the message content or function call.
        5. Return the extracted message content or function call JSON string.
        6. Handle any exceptions that occur during this process.
    receive_from_chat_gpt:
        1. Check if the ChatGPT response is not empty.
        2. Parse the ChatGPT response JSON string.
        3. Extract the function call from the parsed JSON.
        4. If a function call exists, extract the function name and arguments.
        5. Call the handle_function_call method to process the function call.
        6. Handle any exceptions that occur during this process.
