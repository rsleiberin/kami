import sys
import logging
from modules.utils.utils import get_methods
import config

sys.path.append('/home/tank/kami')  # Use the actual path to the 'kami' directory
from modules.databases.airtable_client.airtable_client import AirtableClient

# Initialize logging
logging.basicConfig(filename='llm_switcher.log', level=logging.DEBUG)

class LLMSwitcher:
    """
    A class for managing different language models (LLMs) and modules.
    """
    def __init__(self):
        """Initialize the LLMSwitcher with registered modules."""
        from modules.llm_interface.chat_gpt.chat_gpt import ChatGPT  # Local import to prevent circular dependencies

        self.modules = {
            "airtable_client": AirtableClient(config.AIRTABLE_PERSONAL_ACCESS_TOKEN)
        }
        self.gpt = ChatGPT(modules=self.modules, llm_switcher=self)  # Initialize ChatGPT with the modules
        self.modules["chat_gpt"] = self.gpt

    def get_methods(self):
        """Get methods for the LLMSwitcher class."""
        return get_methods(self)

    def register_module(self, module_name, module_instance):
        """Register a module with the LLMSwitcher."""
        self.modules[module_name] = module_instance

    def execute_module_method(self, module_name, method_name, *args, **kwargs):
        # Fetch the module instance (not a submodule or class)
        module_instance = self.modules.get(module_name)

        if not module_instance:
            error_msg = f"No module named {module_name} found."
            logging.error(error_msg)
            return error_msg

        # Now, execute the method on the module instance.
        method_to_call = getattr(module_instance, method_name, None)
        if not method_to_call:
            error_msg = f"Method {method_name} not found in module {module_name}."
            logging.error(error_msg)
            return error_msg

        try:
            return method_to_call(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error executing method {method_name} in module {module_name}: {str(e)}")
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
    switcher = LLMSwitcher()
    response = switcher.execute_module_method("chat_gpt", "ask_gpt", "Tell me about airtable_client methods")
    print(response)
    airtable_module = switcher.modules["airtable_client"]
    methods = airtable_module.get_methods()
    print(methods)



