from modules.databases.airtable_client.airtable_client import AirtableClient
import sys
import logging
from modules.utils.utils import get_methods
import config
from modules.llm_interface.chat_gpt.chat_gpt import ChatGPT
from datetime import datetime
import importlib

sys.path.append('/home/tank/kami')  # Use the actual path to the 'kami' directory

# Initialize logging
logging.basicConfig(filename='llm_switcher.log', level=logging.DEBUG)

class LLMSwitcher:
    def __init__(self):
        """
        Initialize the LLMSwitcher with registered modules.
        This serves as the main controller for managing different language models and modules.
        ---
        Debug Tag: DT.1-LLMSwitcher-Initialization
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.1-LLMSwitcher-Initialization | Time: {timestamp}")

        try:
            # Initialize AirtableClient
            self.AirtableClient = AirtableClient(config.AIRTABLE_PERSONAL_ACCESS_TOKEN)
            
            # Initialize modules dictionary
            self.modules = {
                "LLMSwitcher": self,
                "AirtableClient": self.AirtableClient  # Note the comma at the end
            }
            
            # Load sub-classes
            self.modules["AirtableClient.Read"] = self.modules["AirtableClient"].Read
            
            # Initialize ChatGPT with the modules
            self.modules["chat_gpt"] = ChatGPT(modules=self.modules, llm_switcher=self)

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.1-Exception in LLMSwitcher-Initialization | Time: {timestamp}")
            logging.error(f"Error in LLMSwitcher __init__: {e}")

 


    def get_methods(self):
        """
        Get methods and their docstrings for the LLMSwitcher class.
        This function provides an overview of the methods available in the LLMSwitcher class.
        ---
        Debug Tag: DT.2-LLMSwitcher-get_methods
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.2-LLMSwitcher-get_methods | Time: {timestamp}")

        try:
            return get_methods(self)
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.2-Exception in LLMSwitcher-get_methods | Time: {timestamp}")
            logging.error(f"Error in LLMSwitcher get_methods: {e}")
            return {}


    def register_module(self, module_name, module_instance):
        """
        Register a module with the LLMSwitcher.
        This function adds a new module to the LLMSwitcher's list of registered modules.
        ---
        Debug Tag: DT.3-LLMSwitcher-register_module
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.3-LLMSwitcher-register_module | Time: {timestamp}")

        try:
            self.modules[module_name] = module_instance
            print(f"DT.3-Module {module_name} successfully registered | Time: {timestamp}")
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.3-Exception in LLMSwitcher-register_module | Time: {timestamp}")
            logging.error(f"Error in LLMSwitcher register_module: {e}")

    def execute_module_method(self, module_name, code, *args, **kwargs):
        """
        Execute a method from a registered module dynamically.
        This function allows you to call a method in a module by its name and pass arguments to it.
        ---
        Debug Tag: DT.4-LLMSwitcher-execute_module_method
        Debug Focus Log Tag: Executing method from module
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4-LLMSwitcher-execute_module_method | Time: {timestamp}")
        
        try:
            # Debugging information
            print(f"DT.4-Executing Module Method {module_name}.{code} | Time: {timestamp}")
            print(f"DT.4-Executed Args: {args} | Time: {timestamp}")
            print(f"DT.4-Executed Kwargs: {kwargs} | Time: {timestamp}")

            # Actual functionality
            components = code.split('.')
            module_instance = self.modules.get(module_name)

            if not module_instance:
                error_msg = f"No module named {module_name} found."
                logging.error(error_msg)
                return error_msg

            current_instance = module_instance
            for component in components:
                if "(" in component and ")" in component:
                    method_name, method_args_str = component.split('(')
                    method_args_str = method_args_str.rstrip(')')
                    method_args = eval(f"[{method_args_str}]")
                    current_instance = getattr(current_instance, method_name)(*method_args)
                else:
                    current_instance = getattr(current_instance, component)

            if callable(current_instance):
                print(f"DT.4-Executing function: {module_name}.{code} with args: {args} and kwargs: {kwargs} | Time: {timestamp}")
                return current_instance(*args, **kwargs)
            else:
                return current_instance

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4-Exception in LLMSwitcher-execute_module_method | Time: {timestamp}")
            logging.error(f"Error executing method {code} in module {module_name}: {str(e)}")
            return str(e)


    def get_registered_module_methods(self, module_name):
        """
        Return the methods of a registered module.
        This function queries the list of methods available in a given module.
        ---
        Debug Tag: DT.5-LLMSwitcher-get_registered_module_methods
        Debug Focus Log Tag: Fetching registered module methods
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.5-LLMSwitcher-get_registered_module_methods | Time: {timestamp}")

        try:
            # Debugging information
            print(f"DT.5-Fetching registered module methods for {module_name} | Time: {timestamp}")

            # Actual functionality
            module = self.modules.get(module_name)
            if not module:
                error_msg = f"No module named {module_name} found."
                logging.error(error_msg)
                return error_msg

            return get_methods(module)

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.5-Exception in LLMSwitcher-get_registered_module_methods | Time: {timestamp}")
            logging.error(f"Error fetching methods for module {module_name}: {str(e)}")
            return str(e)

    def get_model_for_task(self, task_name):
        """
        Determine the best Large Language Model (LLM) for a given task.
        This function is responsible for deciding which model to use based on the task name provided.
        ---
        Debug Tag: DT.6-LLMSwitcher-get_model_for_task
        Debug Focus Log Tag: Fetching model for task
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.6-LLMSwitcher-get_model_for_task | Time: {timestamp}")

        try:
            # Debugging information
            print(f"DT.6-Fetching model for task: {task_name} | Time: {timestamp}")

            # Actual functionality
            if task_name in ["chat", "generate_text"]:
                return self.gpt
            return None

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.6-Exception in LLMSwitcher-get_model_for_task | Time: {timestamp}")
            logging.error(f"Error determining model for task {task_name}: {str(e)}")
            return None

    def perform_task(self, task_name, *args, **kwargs):
        """
        Perform a task using the best-suited Large Language Model (LLM).
        This function will use get_model_for_task to determine the best-suited model and then
        call the model's perform method with the provided arguments and keyword arguments.
        ---
        Debug Tag: DT.7-LLMSwitcher-perform_task
        Debug Focus Log Tag: Executing task
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.7-LLMSwitcher-perform_task | Time: {timestamp}")

        try:
            # Debugging information
            print(f"DT.7-Executing task: {task_name} | Time: {timestamp}")

            # Determine the best-suited LLM for the given task
            model = self.get_model_for_task(task_name)

            # Execute the task if a suitable model is found
            if model:
                return model.perform(task_name, *args, **kwargs)

            # Handle the case where no suitable model is found
            return "No suitable model found for the task."

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.7-Exception in LLMSwitcher-perform_task | Time: {timestamp}")
            logging.error(f"Error executing task {task_name}: {str(e)}")
            return f"Error executing task: {str(e)}"

    def load_module_class(self, full_class_string):
        """
        Dynamically load a class from a string representation.
        This function takes the fully qualified name of the class and returns the loaded class object.
        ---
        Debug Tag: DT.8-LLMSwitcher-load_module_class
        Debug Focus Log Tag: Loading module class
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.8-LLMSwitcher-load_module_class | Time: {timestamp}")

        try:
            # Debugging information
            print(f"DT.8-Loading module class: {full_class_string} | Time: {timestamp}")

            # Parse the string to extract module name and class name
            module_name, class_name = full_class_string.rsplit(".", 1)

            # Import the module dynamically
            module = importlib.import_module(module_name)

            # Retrieve the class object from the module
            _class = getattr(module, class_name)

            # Return the class object
            return _class

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.8-Exception in LLMSwitcher-load_module_class | Time: {timestamp}")
            logging.error(f"Error in load_module_class: {e}")
            return None

    def use_module(self, module_name, method_name, *args, **kwargs):
        """
        Use a specific method from a registered module.
        This function dynamically calls a method from a registered module, passing in provided arguments and keyword arguments.
        ---
        Debug Tag: DT.9-LLMSwitcher-use_module
        Debug Focus Log Tag: Using module method
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.9-LLMSwitcher-use_module | Time: {timestamp}")

        # Debugging information
        print(f"DT.9-Using method {method_name} from module {module_name} | Time: {timestamp}")

        module_instance = self.modules.get(module_name)
        if not module_instance:
            error_msg = f"Module {module_name} not registered."
            logging.error(error_msg)
            return error_msg

        try:
            # Retrieve the method from the module instance
            method = getattr(module_instance, method_name)

            # Check if the method is callable
            if not callable(method):
                error_msg = f"{method_name} is not a callable method in module {module_name}."
                logging.error(error_msg)
                return error_msg

            # Execute and return the method's output
            return method(*args, **kwargs)

        except AttributeError:
            error_msg = f"Method {method_name} not found in module {module_name}."
            logging.error(error_msg)
            return error_msg

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.9-Exception in LLMSwitcher-use_module | Time: {timestamp}")
            logging.error(f"Error using method {method_name} from module {module_name}: {str(e)}")
            return f"Error while using {method_name} from {module_name}: {str(e)}"

if __name__ == "__main__":
    """
    Main entry point for the LLMSwitcher application.
    This will initialize the LLMSwitcher class, retrieve the ChatGPT module, and enter a while loop for chat.
    ---
    Debug Tag: DT.10-main
    Debug Focus Log Tag: Main loop for chat
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"DT.10-main | Time: {timestamp}")

    try:
        # Initialize LLMSwitcher
        print(f"DT.10-Initializing LLMSwitcher | Time: {timestamp}")
        switcher = LLMSwitcher()

        # Get the ChatGPT instance
        print(f"DT.10-Getting ChatGPT instance | Time: {timestamp}")
        chat_gpt = switcher.modules["chat_gpt"]

        while True:
            # Input message from user
            user_input = input("You: ")

            # Check for exit commands
            if user_input.lower() in ["exit", "quit"]:
                break

            # Get response from ChatGPT
            print(f"DT.10-Getting response from ChatGPT | Time: {timestamp}")
            response = chat_gpt.ask_gpt(user_input)

            # Print the response
            print(f"ChatGPT: {response}")

    except Exception as e:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.10-Exception in main | Time: {timestamp}")
        logging.error(f"Error in main: {str(e)}")








