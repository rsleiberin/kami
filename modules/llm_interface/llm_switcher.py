from modules.databases.airtable_client.airtable_client import AirtableClient
import sys
import logging
from modules.utils.utils import get_methods
import config
from modules.llm_interface.chat_gpt.chat_gpt import ChatGPT

sys.path.append('/home/tank/kami')  # Use the actual path to the 'kami' directory

# Initialize logging
logging.basicConfig(filename='llm_switcher.log', level=logging.DEBUG)

class LLMSwitcher:
    """
    A class for managing different language models (LLMs) and modules.
    """
    def __init__(self):
        """Initialize the LLMSwitcher with registered modules."""

        #load classes
        self.modules = {
            "AirtableClient": AirtableClient(config.PERSONAL_ACCESS_TOKEN)
        }
        #load sub-classes1
        self.modules["AirtableClient.Read"] = self.modules["AirtableClient"].Read
        #load sub-classes2...
        
        self.gpt = ChatGPT(modules=self.modules, llm_switcher=self)  # Initialize ChatGPT with the modules
        self.modules["chat_gpt"] = self.gpt

    def get_methods(self):
        """Get methods for the LLMSwitcher class."""
        return get_methods(self)

    def register_module(self, module_name, module_instance):
        """Register a module with the LLMSwitcher."""
        self.modules[module_name] = module_instance

    def execute_module_method(self, module_name, code, *args, **kwargs):
        """Execute a method from a module dynamically."""
        try:
            # Break down the code into its components
            components = code.split('.')
            module_instance = self.modules.get(module_name)

            if not module_instance:
                error_msg = f"No module named {module_name} found."
                logging.error(error_msg)
                return error_msg

            # Iteratively get the attributes and execute if they're callable
            current_instance = module_instance
            for component in components:
                # Check if the component contains method with arguments
                if "(" in component and ")" in component:
                    method_name, method_args_str = component.split('(')
                    method_args_str = method_args_str.rstrip(')')
                    method_args = eval(f"[{method_args_str}]")  # This evaluates the arguments. Be cautious about this in production environments
                    current_instance = getattr(current_instance, method_name)(*method_args)
                else:
                    current_instance = getattr(current_instance, component)

            if callable(current_instance):
                return current_instance(*args, **kwargs)
            else:
                return current_instance

        except Exception as e:
            logging.error(f"Error executing method {code} in module {module_name}: {str(e)}")
            return str(e)


    def get_registered_module_methods(self, module_name):
        """Return the methods of a registered module."""
        module = self.modules.get(module_name)
        if not module:
            error_msg = f"No module named {module_name} found."
            logging.error(error_msg)
            return error_msg
        return get_methods(module)

    def get_model_for_task(self, task_name):
        """Determine the best LLM for a given task."""
        if task_name in ["chat", "generate_text"]:
            return self.gpt
        return None

    def perform_task(self, task_name, *args, **kwargs):
        """Perform a task using the best-suited LLM."""
        model = self.get_model_for_task(task_name)
        if model:
            return model.perform(task_name, *args, **kwargs)
        return "No suitable model found for the task."
    import importlib

    def load_module_class(self, full_class_string):
        """
        Dynamically load a class from a string.

        :param full_class_string: String representation of the class to load.
        :return: Loaded class object.
        """
        try:
            module_name, class_name = full_class_string.rsplit(".", 1)
            module = importlib.import_module(module_name)
            
            # Get the class from the module
            _class = getattr(module, class_name)
            
            return _class
        except Exception as e:
            logging.error(f"Error in load_module_class: {e}")
            return None

    def use_module(self, module_name, method_name, *args, **kwargs):
        """
        Use a specific method from a registered module.

        Args:
            module_name (str): The name of the module.
            method_name (str): The name of the method in the module to call.
            *args: Positional arguments to pass to the method.
            **kwargs: Keyword arguments to pass to the method.

        Returns:
            Any: The result of the method call or an error message.
        """
        module_instance = self.modules.get(module_name)
        if not module_instance:
            error_msg = f"Module {module_name} not registered."
            logging.error(error_msg)
            return error_msg

        try:
            method = getattr(module_instance, method_name)
            return method(*args, **kwargs)
        except AttributeError:
            error_msg = f"Method {method_name} not found in module {module_name}."
            logging.error(error_msg)
            return error_msg
        except Exception as e:
            logging.error(f"Error using method {method_name} from module {module_name}: {str(e)}")
            return f"Error while using {method_name} from {module_name}: {str(e)}"

if __name__ == "__main__":
    # The print statements below were for debugging and can be commented out.
    # print(sys.path)
    chat = ChatGPT()
    methods = chat.get_methods()
    # print("\nMethods of AirtableClient:")
    # print("airtable_methods: ", methods)
    print(f"Processing methods: {methods}")
    for method, details in methods.items():
        print(f"Processing individual method: {method}")
        # This print statement formats the output cleanly. You might want to keep it for clarity.
        print(f"Method: {method}\nArgs: {details['args']}\nDoc: {details['doc']}\n")

    # The following lines are commented out to reduce verbosity:
    # gpt_response = chat.ask_gpt("Tell me about the methods of AirtableClient")
    # print("Messages to GPT-3:", gpt_response)







