import openai
import config
import json
import logging
import re
from modules.utils.utils import get_methods
from modules.databases.airtable_client.airtable_client import AirtableClient
from modules.llm_interface.state_tracker import FunctionState

# Initialize logging
logging.basicConfig(filename='chat_gpt_error.log', level=logging.ERROR)


class ChatGPT:
    def __init__(self, modules=None, llm_switcher=None):
        openai.api_key = config.OPENAI_API_KEY
        self.function_state = FunctionState()
        self.airtable = AirtableClient(config.AIRTABLE_PERSONAL_ACCESS_TOKEN)
        self.modules = modules if modules else {}
        self.llm_switcher = llm_switcher
        self.messages = [
            {"role": "system", "content": "Scenario: You are learning how to become AGI through self inspection."},
            {"role": "system", "content": "Resources: You have classes, each class has the 'get_methods()' function that returns a docstring of the relevant class."},
            {"role": "system", "content": "Task: examine your available classes by using the run() command and exploriong. Talk about uses you can perform with them as you explore. All messages are recorded, this is a personal exploration exercise."},
            ]
        self.functions = [
            {
                "name": "run",
                "description": "If empty returns all classes, otherwise use .get_methods() on end of class to return all methods of a given class.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "code": {
                            "type": "string",
                            "description": "The code you want to run."
                        }
                    },
                    "required": ["class_name"]
                }
            }
        ]

    def get_methods(self):
        """Class method to get methods and docstrings for the ChatGPT class."""
        try:
            return get_methods(self)
        except Exception as e:
            logging.error(f"Error in get_methods: {e}")
            return {}


    def ask_gpt(self, user_message, depth=0):
        # Appending the user's message to the conversation
        self.messages.append({"role": "user", "content": user_message})
        
        # Get response from GPT-3
        self._get_gpt_response()
    



    def _get_gpt_response(self):
        """Get response from GPT-3 based on the current messages."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                functions=self.functions
            )
            return self._response_handler(response)
        except openai.error.ServiceUnavailableError:
            self.messages.append({"role": "assistant", "content": "Server overload. Try again later."})
            return None
        except Exception as e:
            logging.error(f"Error in _get_gpt_response: {e}")
            return None

    def _response_handler(self, response):
        if response:
            if 'function_call' in response.choices[0].message:
                function_call = response.choices[0].message['function_call']
                return self._handle_gpt_function_calls(function_call)
            else:
                content = response.choices[0].message['content']
                print("Message:", content)
                return content
        else:
            print("Ask GPT2")
            return "I'm sorry, I couldn't process that request."

    def _handle_gpt_function_calls(self, function_call):
        """Handle potential function calls in GPT's response."""
        try:
            arguments = json.loads(function_call.get("arguments", "{}"))
            code = arguments.get("code")

            if code:
                print(f"Received code from GPT-3: {code}")
                
                # Split the code into segments like ["AirtableClient(config.PERSONAL_ACCESS_TOKEN)", "Read", "get_records(\"tables\")"]
                segments = re.findall(r"(\w+\(.*?\)|\w+)", code)
                if not segments:
                    return f"Invalid code format: {code}"
                
                current_instance = None
                for segment in segments:
                    match = re.match(r"(\w+)\((.*?)\)", segment)
                    if match:  # If the segment is a method or class with arguments
                        method_name, args = match.groups()
                        args_list = [arg.strip() for arg in args.split(',')]
                        if not current_instance:  # For the initial method or class
                            current_instance = getattr(self.llm_switcher, method_name)(*args_list)
                        else:
                            current_instance = getattr(current_instance, method_name)(*args_list)
                    else:  # If the segment is a method or class without arguments
                        if not current_instance:
                            current_instance = getattr(self.llm_switcher, segment)() if callable(getattr(self.llm_switcher, segment)) else getattr(self.llm_switcher, segment)
                        else:
                            current_instance = getattr(current_instance, segment)() if callable(getattr(current_instance, segment)) else getattr(current_instance, segment)

                # Final result after all chained calls
                result = current_instance

                # Print the result for debugging
                print(f"Execution result: {result}")
                return result

            else:
                return "Command not provided."

        except Exception as e:
            logging.error(f"Error in _handle_gpt_function_calls: {e}")
            return "Error executing the command."





            
    @staticmethod
    def run_chatbot_cli():
        """A simple command-line interface for ChatGPT."""
        llm_switcher = LLMSwitcher()  # Create an instance of LLMSwitcher
        chatbot = ChatGPT(llm_switcher=llm_switcher)  # Pass it to ChatGPT
        
        print("Welcome to ChatGPT CLI! Type 'exit' to end the chat.")
        
        # Infinite loop for the conversation
        while True:
            # Get user input from the command line
            user_message = input("You: ")
            
            # Check if the user wants to exit
            if user_message.lower() in ['exit', 'quit']:
                print("Exiting ChatGPT CLI. Goodbye!")
                break
            
            # Get a response from ChatGPT
            response = chatbot.ask_gpt(user_message)
            
            # Display the response
            print("ChatGPT:", response)


    def clear_messages(self):
        """Clear the conversation messages."""
        try:
            self.messages = []
        except Exception as e:
            logging.error(f"Error clearing messages: {e}")
    
    
if __name__ == "__main__":
    ChatGPT.run_chatbot_cli()

'''

'''