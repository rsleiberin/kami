Method Name: loop
Class: ChatGPTAssistant
Purpose: To manage the main interaction loop between the user and ChatGPT, facilitating continuous communication and handling user inputs and ChatGPT responses.
Pseudo Code:
    1. Output a message indicating the ChatGPT Assistant is ready to assist.
    2. Enter an infinite loop to allow continuous interaction with the user.
        a. Await user input and trim any leading/trailing whitespaces.
        b. If the user input is empty, output an error message and return to step 2a.
        c. Fetch the current context from the context manager.
        d. Call the send_to_chat_gpt method, passing the current context and user input as arguments.
        e. If a response is received from ChatGPT (non-None value), output the response and call the receive_from_chat_gpt method, passing the ChatGPT response as an argument. If no response is received, output an error message.
        f. If a KeyboardInterrupt exception is caught (e.g., user hits Ctrl+C), output a message indicating the exit of the loop, and break out of the infinite loop.
        g. If any other exception is caught, output an error message along with the exception details, and return to step 2a.
    3. Output a message indicating the exit of the main loop.
