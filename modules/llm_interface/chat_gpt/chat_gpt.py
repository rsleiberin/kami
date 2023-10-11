import openai
import config
import json  

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.utils.utils import get_methods

import inspect
from modules.databases.airtable_client.airtable_client import AirtableClient

class ChatGPT:
    def __init__(self):
        # Setting up the API key for OpenAI
        openai.api_key = config.OPENAI_API_KEY
        self.airtable = AirtableClient(config.AIRTABLE_PERSONAL_ACCESS_TOKEN)  # Assuming you've set this in config
        # Initializing the conversation with a system message
        self.all_classes = {
            "AirtableClient": self.airtable,
        }
        self.messages = [
            {"role": "system", "content": "Scenario: You are learning how to become AGI through self inspection."},
            {"role": "system", "content": "Resources: You have classes, each class has the 'get_methods()' function that returns a docstring of the relevant class."},
            {"role": "system", "content": "Task: examine your available classes and talk about uses you can perform with them as you explore. All messages are recorded, this is a personal exploration exercise."},
            ]
        self.functions = [
            {
                "name": "explore_class_methods",
                "description": "Explore methods of a given class.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "class_name": {
                            "type": "string",
                            "description": "The name of the class to explore."
                        }
                    },
                    "required": ["class_name"]
                }
            }
        ]
    @classmethod
    def get_methods(cls):
        """Class method to get methods and docstrings for the ChatGPT class."""
        return get_methods(cls)

    def explore_environment(self):
        """
        Explores the ChatGPT environment, listing down all available methods and properties.

        Returns:
            dict: A structured dictionary detailing methods, properties, and their docstrings and args.
        """
        chat_gpt_structure = get_methods(self)

        for class_name, class_instance in self.all_classes.items():
            chat_gpt_structure[class_name] = get_methods(class_instance)

        return chat_gpt_structure

    
    def get_available_tables(self):
        """Fetches available tables using AirtableClient's Read functions."""
        try:
            return self.airtable.Read().get_tables()
        except Exception as e:
            return f"Error fetching tables: {str(e)}"
    
    def explore_class_methods(self, class_name):
        """
        Fetches methods' docstrings for a specified class using the get_methods() function.

        Args:
            class_name (str): The name of the class to explore.

        Returns:
            dict or str: A dictionary containing method names and their respective docstrings 
                        or an error message.
        """
        print(f"Function 'explore_class_methods' called with class_name: {class_name}")

        if class_name == "functions":
            # Return the available functions
            functions_list = [func["name"] for func in self.functions]
            print("Detected 'functions' as class_name. Available functions:", functions_list)
            return {"available_functions": functions_list}

        try:
            # Assuming all your classes are in a dictionary called 'all_classes'
            target_class = self.all_classes.get(class_name)
            if not target_class:
                return_msg = f"No class named {class_name} found."
                print(return_msg)  # Debug print statement
                return return_msg

                        # First, get the methods of the class itself
            methods_info = target_class.get_methods()

            # Then, for each method, check if it's a class and get its methods too
            for method_name, method_details in methods_info.items():
                method_instance = getattr(target_class, method_name, None)
                if inspect.isclass(method_instance):
                    methods_info[method_name]['sub_methods'] = method_instance.get_methods()

            if methods_info:
                return methods_info
            else:
                return_msg = f"No methods found for the class {class_name}."
                print(return_msg)  # Debug print statement
                return return_msg
        except Exception as e:
            return {"error": str(e)}


    def ask_gpt(self, user_message, depth=0):
        # Appending the user's message to the conversation
        self.messages.append({"role": "user", "content": user_message})

        
        # Direct user command
        if user_message.lower() == "get available tables":
            tables = self.get_available_tables()
            return f"Available tables: {', '.join(tables)}"
        
        # Request response from GPT
        print("Sending the following messages to GPT-3:", self.messages)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                functions=self.functions
            )
        except openai.error.ServiceUnavailableError:
            return "I apologize, but the server seems to be overloaded right now. Please try again later."

        #print response object
        print("Response object from OpenAI:", response)
        
        # Extracting the content of the message from the model's response
        print("Sending the following messages to GPT-3:", self.messages)
        assistant_message_content = response.choices[0].message['content']
        print("GPT Response:", assistant_message_content)
        if not assistant_message_content:
            assistant_message_content = "I'm sorry, I couldn't process that request."
        self.messages.append({"role": "assistant", "content": assistant_message_content})
        
        # Checking for a function call in GPT's response
        function_call = response.choices[0].message.get('function_call', {})
        function_name = function_call.get("name")

        if function_name == "explore_class_methods":
            arguments = json.loads(function_call["arguments"])
            class_name = arguments.get("class_name")
                    
            methods_info = self.explore_class_methods(class_name)
            if methods_info:
                # Convert the dictionary to a more human-readable string
                print(methods_info)
                result_string = '\n'.join(methods_info['available_functions'])

                # Now, send this result back to GPT-3 for further instructions
                if depth > 5:
                    return "Depth limit has reached 5, increase limit."
                return self.ask_gpt(result_string, depth+1)  # Recursive call


            else:
                return "No methods found for this class."


        elif "function_name" in function_call:
            function_call_string = f"Called function: {function_call['function_name']} with arguments: {function_call['args']}"
            self.messages.append({"role": "assistant", "content": function_call_string})

        else:
            self.messages.append({"role": "assistant", "content": assistant_message_content})
            return assistant_message_content
        # Default return, in case none of the above conditions were met.
        return "I'm not sure how to handle that request."

    @staticmethod
    def run_chatbot_cli():
        """A simple command-line interface for ChatGPT."""
        
        # Create an instance of the ChatGPT class
        chatbot = ChatGPT()
        
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
        # Clearing the conversation
        #The forgeting funciton, we deal with memory storage here.
        #What RANK SHOULD THE MESSAGE RETURN?!?!?
        self.messages = []
    
if __name__ == "__main__":
    ChatGPT.run_chatbot_cli()

'''

'''