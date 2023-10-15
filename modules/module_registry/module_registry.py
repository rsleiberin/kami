from datetime import datetime
import logging
from modules.utils.error_handler import handle_error
from modules.utils.utils import get_methods
from modules.databases.airtable_client.airtable_client import AirtableClient
import config
from importlib import import_module

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')

class ModuleRegistry:
    def __init__(self):
        """
        Initialize the ModuleRegistry with registered modules.
        ---
        Debug Tag: DT.1-ModuleRegistry-Initialization
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.1-ModuleRegistry-Initialization | Time: {timestamp}")

        try:
            # Initialize AirtableClient
            self.AirtableClient = AirtableClient(config.AIRTABLE_PERSONAL_ACCESS_TOKEN)
            
            # Initialize modules dictionary
            self.modules = {
                "ModuleRegistry": self,
                "AirtableClient": self.AirtableClient
            }
            
            print(f"DT.1-ModuleRegistry successfully initialized | Time: {timestamp}")

        except Exception as e:
            error_message, http_status = handle_error('MR001')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")

    def execute_module_method(self, module_name, code, *args, **kwargs):
        """
        Execute a method from a registered module dynamically.
        This function allows you to call a method in a module by its name and pass arguments to it.
        ---
        Debug Tag: DT.4-ModuleRegistry-execute_module_method
        Debug Focus Log Tag: Executing method from module
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4-ModuleRegistry-execute_module_method | Time: {timestamp}")
        
        try:
            # Debugging information
            print(f"DT.4-Executing Module Method {module_name}.{code} | Time: {timestamp}")
            print(f"DT.4-Executed Args: {args} | Time: {timestamp}")
            print(f"DT.4-Executed Kwargs: {kwargs} | Time: {timestamp}")

            # Actual functionality
            components = code.split('.')
            module_instance = self.modules.get(module_name)  # Changed to self.module_dict

            if not module_instance:
                error_message, http_status = handle_error('MR004')  # Error codes should also be updated
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
            error_message, http_status = handle_error('MR005')  # Error codes should also be updated
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4-Exception in ModuleRegistry-execute_module_method | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return str(e)
    
    def get_methods(self):
        """
        Get methods and their docstrings for the Module Registery class.
        This function provides an overview of the methods available in the Module Registery class.
        ---
        Debug Tag: DT.4-ModuleRegistry-get_methods
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4-ModuleRegistry-get_methods | Time: {timestamp}")

        try:
            return get_methods(self)
        except Exception as e:
            error_message, http_status = handle_error('MR006')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return {}
    
    def get_model_for_task(self, task_name):
        """
        Determine the best Large Language Model (LLM) for a given task.
        This function is responsible for deciding which model to use based on the task name provided.
        ---
        Debug Tag: DT.6-ModuleRegistry-get_model_for_task
        Debug Focus Log Tag: Fetching model for task
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.6-ModuleRegistry-get_model_for_task | Time: {timestamp}")

        try:
            # Debugging information
            print(f"DT.6-Fetching model for task: {task_name} | Time: {timestamp}")

            # Actual functionality
            if task_name in ["chat", "generate_text"]:
                if 'gpt' in self.modules:
                    return self.modules['gpt']
                else:
                    error_message, http_status = handle_error('MR007')  # Updated error code
                    logging.error(f"{error_message} | HTTP Status: {http_status}")
                    return None
            return None

        except Exception as e:
            error_message, http_status = handle_error('MR008')  # Updated error code
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.6-Exception in ModuleRegistry-get_model_for_task | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return str(e)
        
    def get_registered_module_methods(self, module_name):
        """
        Return the methods of a registered module.
        This function queries the list of methods available in a given module.
        ---
        Debug Tag: DT.5-ModuleRegistry-get_registered_module_methods
        Debug Focus Log Tag: Fetching registered module methods
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.5-ModuleRegistry-get_registered_module_methods | Time: {timestamp}")

        try:
            # Debugging information
            print(f"DT.5-Fetching registered module methods for {module_name} | Time: {timestamp}")

            # Actual functionality
            module = self.modules.get(module_name)
            if not module:
                error_message, http_status = handle_error('MR010')  # Update error code accordingly
                logging.error(f"{error_message} | HTTP Status: {http_status}")
                return error_message

            return get_methods(module)

        except Exception as e:
            error_message, http_status = handle_error('MR011')  # Update error code accordingly
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.5-Exception in ModuleRegistry-get_registered_module_methods | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return error_message
    
    def load_module_class(self, full_class_string):
        """
        Dynamically load a class from a string representation.
        ---
        Debug Tag: DT.8-ModuleRegistry-load_module_class
        Debug Focus Log Tag: Loading module class
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.8-ModuleRegistry-load_module_class | Time: {timestamp}")

        try:
            # Debugging information
            print(f"DT.8-Loading module class: {full_class_string} | Time: {timestamp}")

            # Actual functionality
            module_path, class_name = full_class_string.rsplit('.', 1)
            module = import_module(module_path)
            return getattr(module, class_name)

        except Exception as e:
            error_message, http_status = handle_error('MR007')  # Update error code accordingly
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.8-Exception in ModuleRegistry-load_module_class | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return error_message
    
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
                    error_message, http_status = handle_error('MR013')  # Updated error code
                    logging.error(f"{error_message} | HTTP Status: {http_status}")
                    return error_message
            else:
                error_message, http_status = handle_error('MR014')  # Updated error code
                logging.error(f"{error_message} | HTTP Status: {http_status}")
                return error_message

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.7-Exception in LLMSwitcher-perform_task | Time: {timestamp}")
            error_message, http_status = handle_error('GEN001')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return str(e)
    
    def register_module(self, module_name, module_instance, module_context={}):
        """
        Register a module with the ModuleRegistry.
        This function adds a new module to the ModuleRegistry's list of registered modules.
        Also attaches any relevant context data to the module.
        ---
        Debug Tag: DT.4-ModuleRegistry-register_module
        Debug Focus Log Tag: Registering module
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4-ModuleRegistry-register_module | Time: {timestamp}")
        
        try:
            # Storing module instance and context in a dictionary
            self.modules[module_name] = {
                "instance": module_instance,
                "context": module_context
            }
            print(f"DT.4-Module {module_name} successfully registered | Time: {timestamp}")
        except Exception as e:
            error_message, http_status = handle_error('MR015')  # Error code updated for ModuleRegistry
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
    
    def use_module(self, module_name, method_name, *args, **kwargs):
        """
        Use a specific method from a registered module.
        ---
        Debug Tag: DT.5-ModuleRegistry-use_module
        Debug Focus Log Tag: Using module method
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.5-ModuleRegistry-use_module | Time: {timestamp}")

        try:
            # Debugging information
            print(f"DT.5-Using method {method_name} from module {module_name} | Time: {timestamp}")

            module_instance = self.modules.get(module_name)
            if not module_instance:
                error_message, http_status = handle_error('MR016')  # Error code updated for ModuleRegistry
                logging.error(f"{error_message} | HTTP Status: {http_status}")
                return error_message

            # Retrieve the method from the module instance
            method = getattr(module_instance, method_name, None)

            # Check if the method is callable
            if not callable(method):
                error_message, http_status = handle_error('MR017')  # Error code updated for ModuleRegistry
                logging.error(f"{error_message} | HTTP Status: {http_status}")
                return error_message

            # Execute and return the method's output
            return method(*args, **kwargs)

        except AttributeError:
            error_message, http_status = handle_error('MR018')  # Error code updated for ModuleRegistry
            logging.error(f"{error_message} | HTTP Status: {http_status}")
            return error_message

        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.5-Exception in ModuleRegistry-use_module | Time: {timestamp}")
            error_message, http_status = handle_error('GEN001')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return error_message
    
if __name__ == "__main__":
    instance = ModuleRegistry()
    print(instance)
    print(instance.get_methods())
