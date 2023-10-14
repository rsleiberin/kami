import openai
import config
import json
import logging
import re
from modules.utils.utils import get_methods
from modules.databases.airtable_client.airtable_client import AirtableClient
from modules.llm_interface.function_state import FunctionState
from datetime import datetime

# Initialize logging
logging.basicConfig(filename='chat_gpt_error.log', level=logging.ERROR)


class ChatGPT:
    def __init__(self, llm_switcher, modules=None):
        """
        Initializes the ChatGPT class.
        ---
        Debug Tag: DT.2-ChatGPT-Initialization
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.2-ChatGPT-Initialization | Time: {timestamp}")
        try:
            print(f"DT.3.1-Setting API Key | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            openai.api_key = config.OPENAI_API_KEY

            print(f"DT.3.2-Initializing FunctionState | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            self.function_state = FunctionState()

            print(f"DT.3.3-Initializing AirtableClient | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            self.AirtableClient = AirtableClient(config.AIRTABLE_PERSONAL_ACCESS_TOKEN)
            
            print(f"DT.3.4-Setting Modules | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            self.modules = modules if modules else {}

            print(f"DT.3.5-Setting LLM Switcher | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            self.llm_switcher = llm_switcher

            print(f"DT.3.6-Setting Messages | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            self.messages = [
                {"role": "system", "content": "Scenario: You are learning how to become AGI through self inspection."},
                {"role": "system", "content": "Resources: You have classes, each class has the 'get_methods()' function that returns a docstring of the relevant class."},
            ]
            
            print(f"DT.3.7-Setting Functions | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
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

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.3.8-Exception in __init__ | Time: {timestamp}")
            logging.error(f"Error in __init__: {e}")

    def get_methods(self):
        """Class method to get methods and docstrings for the ChatGPT class."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4-Getting Methods in ChatGPT | Time: {timestamp}")
        try:
            print(f"DT.4.1-Invoking utility to fetch methods | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return get_methods(self)
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.2-Exception in get_methods | Time: {timestamp}")
            logging.error(f"Error in get_methods: {e}")
            return {}

    def ask_gpt(self, user_message, depth=0):
        """Process user's message and get a response from GPT-3.

        Parameters:
        user_message (str): The message from the user.
        depth (int): Recursion depth, used for internal tracking.
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.5-Entering ask_gpt in ChatGPT | Time: {timestamp}")

        try:
            print(f"DT.5.1-Appending user message | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            self.messages.append({"role": "user", "content": user_message})

            print(f"DT.5.2-Getting GPT-3 response | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            response = self._get_gpt_response()
            
            if response == "FUNCTION_PROCESSED":
                print(f"DT.5.3-Function processed, getting new response | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                return self._get_gpt_response()

            print(f"DT.5.4-Returning GPT-3 response | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return response

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.5.5-Exception in ask_gpt | Time: {timestamp}")
            logging.error(f"Error in ask_gpt: {e}")
            return None

    def _get_gpt_response(self):
        """Get response from GPT-3 based on the current messages."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.6-Entering _get_gpt_response in ChatGPT | Time: {timestamp}")
        
        try:
            print(f"DT.6.1-Getting response from OpenAI API | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                functions=self.functions
            )
            
            print(f"DT.6.2-Handling GPT-3 response | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            result = self._response_handler(response)
            
            print(f"DT.6.3-Returning processed result | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return result
            
        except openai.error.ServiceUnavailableError:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.6.4-Service Unavailable in _get_gpt_response | Time: {timestamp}")
            self.messages.append({"role": "assistant", "content": "Server overload. Try again later."})
            return None
            
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.6.5-Exception in _get_gpt_response | Time: {timestamp}")
            logging.error(f"Error in _get_gpt_response: {e}")
            return None






    def _handle_gpt_function_calls(self, function_call):
        """Handle potential function calls in GPT's response."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.7-Entering _handle_gpt_function_calls in ChatGPT | Time: {timestamp}")

        try:
            print(f"DT.7.1-Processing Function Call Arguments | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            arguments = json.loads(function_call.get("arguments", "{}"))
            code = arguments.get("code")

            if code:
                print(f"DT.7.2-Received Code from GPT-3 | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                segments = re.findall(r"(\w+\(.*?\)|\w+)", code)
                if not segments:
                    return f"Invalid code format: {code}"

                current_instance = None
                for segment in segments:
                    match = re.match(r"(\w+)\((.*?)\)", segment)
                    if match:
                        method_name, args = match.groups()
                        args_list = [arg.strip() for arg in args.split(',')]
                        args_list = [arg for arg in args_list if arg]

                        if not current_instance:
                            current_instance = getattr(self.llm_switcher, method_name)(*args_list)
                        else:
                            current_instance = getattr(current_instance, method_name)(*args_list)

                    else:
                        if not current_instance:
                            current_instance = getattr(self.llm_switcher, segment)() if callable(getattr(self.llm_switcher, segment)) else getattr(self.llm_switcher, segment)
                        else:
                            current_instance = getattr(current_instance, segment)() if callable(getattr(current_instance, segment)) else getattr(current_instance, segment)

                print(f"DT.7.3-Execution Result | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Result: {current_instance}")
                return current_instance

            else:
                print(f"DT.7.4-No 'code' in Arguments | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                available_classes = list(self.llm_switcher.modules.keys())
                return f"Available Classes: {available_classes}"

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.7.5-Exception in _handle_gpt_function_calls | Time: {timestamp}")
            logging.error(f"Error in _handle_gpt_function_calls: {e}")
            return "Error executing the command."





            
    @staticmethod
    def run_chatbot_cli():
        """A simple command-line interface for ChatGPT."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.8-Entering run_chatbot_cli | Time: {timestamp}")
        
        try:
            llm_switcher = LLMSwitcher()  # Create an instance of LLMSwitcher
            chatbot = ChatGPT(llm_switcher=llm_switcher)  # Pass it to ChatGPT
            print(f"DT.8.1-Initialized LLMSwitcher and ChatGPT | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            print("Welcome to ChatGPT CLI! Type 'exit' to end the chat.")
            
            # Infinite loop for the conversation
            while True:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"DT.8.2-Inside CLI Loop | Time: {timestamp}")

                # Get user input from the command line
                user_message = input("You: ")
                
                # Check if the user wants to exit
                if user_message.lower() in ['exit', 'quit']:
                    print(f"DT.8.3-User Chose to Exit | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    print("Exiting ChatGPT CLI. Goodbye!")
                    break
                
                # Get a response from ChatGPT
                response = chatbot.ask_gpt(user_message)
                
                # Display the response
                print(f"DT.8.4-Received Response from ChatGPT | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print("ChatGPT:", response)

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.8.5-Exception in run_chatbot_cli | Time: {timestamp}")
            logging.error(f"Error in run_chatbot_cli: {e}")
            print("Error encountered. Exiting ChatGPT CLI.")


    def clear_messages(self):
        """Clear the conversation messages."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.9-Entering clear_messages | Time: {timestamp}")
        
        try:
            self.messages = []
            print(f"DT.9.1-Successfully cleared messages | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.9.2-Exception in clear_messages | Time: {timestamp}")
            logging.error(f"Error clearing messages: {e}")
    
    
if __name__ == "__main__":
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"DT.10-Entering Main | Time: {timestamp}")
    try:
        ChatGPT.run_chatbot_cli()
        print(f"DT.10.1-Successfully ran ChatGPT CLI | Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.10.2-Exception in Main | Time: {timestamp}")
        logging.error(f"Error in main: {e}")


'''

'''