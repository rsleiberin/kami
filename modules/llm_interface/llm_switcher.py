from modules.databases.airtable_client.airtable_client import AirtableClient
from modules.utils.error_handler import handle_error  # Make sure to import handle_error
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
            error_message, http_status = handle_error('LLM001')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")

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
            error_message, http_status = handle_error('LLM002')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
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
            error_message, http_status = handle_error('LLM003')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")


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
                error_message, http_status = handle_error('LLM004')
                logging.error(f"{error_message} | HTTP Status: {http_status}")
                return error_message

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
            error_message, http_status = handle_error('LLM005')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4-Exception in LLMSwitcher-execute_module_method | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
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
                error_message, http_status = handle_error('LLM004')
                logging.error(f"{error_message} | HTTP Status: {http_status}")
                return error_message

            return get_methods(module)

        except Exception as e:
            error_message, http_status = handle_error('LLM006')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.5-Exception in LLMSwitcher-get_registered_module_methods | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return error_message


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
                if hasattr(self, 'gpt'):
                    return self.gpt
                else:
                    error_message, http_status = handle_error('LLM007') 
                    logging.error(f"{error_message} | HTTP Status: {http_status}")
                    return None
            return None

        except Exception as e:
            error_message, http_status = handle_error('GEN001')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.6-Exception in LLMSwitcher-get_model_for_task | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return None

    def perform_task(self, task_name, *args, **kwargs):
        """
        Perform a task using the best-suited Large Language Model (LLM).
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
                if hasattr(model, 'perform'):
                    return model.perform(task_name, *args, **kwargs)
                else:
                    error_message, http_status = handle_error('LLM008')
                    logging.error(f"{error_message} | HTTP Status: {http_status}")
                    return error_message
            else:
                error_message, http_status = handle_error('LLM009')
                logging.error(f"{error_message} | HTTP Status: {http_status}")
                return error_message

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.7-Exception in LLMSwitcher-perform_task | Time: {timestamp}")
            error_message, http_status = handle_error('GEN001')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return str(e)


    def load_module_class(self, full_class_string):
        """
        Dynamically load a class from a string representation.
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

            # Check if the module was successfully imported
            if module:
                # Retrieve the class object from the module
                _class = getattr(module, class_name, None)

                # Check if the class object was successfully retrieved
                if _class:
                    return _class
                else:
                    error_message, http_status = handle_error('LLM010')
                    logging.error(f"{error_message} | HTTP Status: {http_status}")
                    return None
            else:
                error_message, http_status = handle_error('LLM011')
                logging.error(f"{error_message} | HTTP Status: {http_status}")
                return None

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.8-Exception in LLMSwitcher-load_module_class | Time: {timestamp}")
            error_message, http_status = handle_error('GEN001')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return None


    def use_module(self, module_name, method_name, *args, **kwargs):
        """
        Use a specific method from a registered module.
        ---
        Debug Tag: DT.9-LLMSwitcher-use_module
        Debug Focus Log Tag: Using module method
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.9-LLMSwitcher-use_module | Time: {timestamp}")

        try:
            # Debugging information
            print(f"DT.9-Using method {method_name} from module {module_name} | Time: {timestamp}")

            module_instance = self.modules.get(module_name)
            if not module_instance:
                error_message, http_status = handle_error('LLM012')
                logging.error(f"{error_message} | HTTP Status: {http_status}")
                return error_message

            # Retrieve the method from the module instance
            method = getattr(module_instance, method_name, None)

            # Check if the method is callable
            if not callable(method):
                error_message, http_status = handle_error('LLM013')
                logging.error(f"{error_message} | HTTP Status: {http_status}")
                return error_message

            # Execute and return the method's output
            return method(*args, **kwargs)

        except AttributeError:
            error_message, http_status = handle_error('LLM014')
            logging.error(f"{error_message} | HTTP Status: {http_status}")
            return error_message

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.9-Exception in LLMSwitcher-use_module | Time: {timestamp}")
            error_message, http_status = handle_error('GEN001')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return error_message


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








