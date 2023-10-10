import openai
import config
import json  # We use the json module to work with JSON data
from modules.databases.airtable_client.airtable_client import AirtableClient  # Adjust the import path accordingly

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
    def get_available_tables(self):
        """Fetches available tables using AirtableClient's Read functions."""
        try:
            return self.airtable.Read().get_tables()
        except Exception as e:
            return f"Error fetching tables: {str(e)}"
    
    def explore_class_methods(self,class_name):
        """
        Fetches methods' docstrings for a specified class using the get_methods() function.

        Args:
            class_name (str): The name of the class to explore.

        Returns:
            dict: A dictionary containing method names and their respective docstrings.
        """
        try:
            # Assuming all your classes are in a dictionary called 'all_classes'
            target_class = self.all_classes.get(class_name)
            methods_info = target_class.get_methods()
            return methods_info
        except Exception as e:
            return {"error": str(e)}
    def ask_gpt(self, user_message):
        # Appending the user's message to the conversation
        self.messages.append({"role": "user", "content": user_message})
        
        if user_message.lower() == "get available tables":
            tables = self.get_available_tables()
            assistant_message_content = f"Available tables: {', '.join(tables)}"
        else:
            # Asking the GPT-3.5-turbo model to generate a response
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                functions=self.functions
            )
            
            # Extracting the content of the message from the model's response
            assistant_message_content = response.choices[0].message['content']
            
            # Checking if the assistant's message is in a JSON format (it might be a function call)
            try:
                if assistant_message_content:  # Check if content exists
                    try:
                        # Trying to convert the assistant message into a dictionary (JSON format)
                        try:
                            function_call = json.loads(assistant_message_content)
                            function_name = function_call.get("name")
                            
                            if function_name == "explore_class_methods":
                                class_name = function_call["args"]["class_name"]
                                methods_info = self.explore_class_methods(class_name)
                                assistant_message_content = str(methods_info)
                                
                        except json.JSONDecodeError:
                            # This will handle cases where the response isn't a function call
                            pass
                        
                        # If it has a "function_name" key, it's likely a function call (just an example, you can define your own structure)
                        if "function_name" in function_call:
                            # Printing the detected function and its arguments
                            print(f"Function to call: {function_call['function_name']}")
                            print(f"Arguments: {function_call['args']}")  # Again, this is just an example structure

                            # Appending a record of the function call to the conversation context
                            function_call_string = f"Called function: {function_call['function_name']} with arguments: {function_call['args']}"
                            self.messages.append({"role": "assistant", "content": function_call_string})
            except json.JSONDecodeError:  # This will happen if the assistant_message is not in a JSON format
                # Appending the regular message from the assistant to the conversation
                self.messages.append({"role": "assistant", "content": assistant_message_content})
            
            # Returning the assistant's message
            return assistant_message_content
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