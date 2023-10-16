import inspect
from utils.utils import print_tracer, handle_error, get_methods, add_error_codes

MODULE_REGISTRY_ERROR_CODES = {
    "MR001": {
        'message': 'Module already registered.',
        'http_status': 409,  # Conflict
        'severity': 'ERROR',
        'description': 'The module being registered is already present in the module registry.',
        'resolution': 'Ensure the module is not already added or use a unique name for registration.',
    },
    "MR002": {
        'message': 'Module not found in registry.',
        'http_status': 404,  # Not Found
        'severity': 'ERROR',
        'description': 'The module being removed is not present in the module registry.',
        'resolution': 'Ensure the module name is correct and has been registered.',
    },
    "MR003": {
        'message': 'Module not found in registry.',
        'http_status': 404,  # Not Found
        'severity': 'ERROR',
        'description': 'Attempted to execute a method from a module that is not registered.',
        'resolution': 'Ensure the module is registered before executing methods from it.',
    },
    "MR004": {
        'message': 'Method not found in the specified module.',
        'http_status': 404,  # Not Found
        'severity': 'ERROR',
        'description': 'Attempted to execute a method that does not exist in the specified module.',
        'resolution': 'Check the method name and ensure it exists in the module.',
    },
    "MR005": {
        'message': 'Error while executing the method.',
        'http_status': 500,  # Internal Server Error
        'severity': 'ERROR',
        'description': 'An unexpected error occurred while executing the method from the module.',
        'resolution': 'Check the arguments and method implementation for potential issues.',
    },
    "MR006": {
        'message': 'Failed to fetch registered modules.',
        'http_status': 500,  # Internal Server Error
        'severity': 'ERROR',
        'description': 'An unexpected error occurred while fetching the list of registered modules.',
        'resolution': 'Check the module registry implementation and storage.',
    },
    "MR007": {
        'message': 'Module not found in registry.',
        'http_status': 404,  # Not Found
        'severity': 'ERROR',
        'description': 'The module whose methods are being fetched is not present in the module registry.',
        'resolution': 'Ensure the module name is correct and has been registered.',
    },
    "MR008": {
        'message': 'Unable to fetch methods for the module.',
        'http_status': 500,  # Internal Server Error
        'severity': 'ERROR',
        'description': 'An unexpected error occurred while trying to fetch methods for a registered module.',
        'resolution': 'Ensure the module and its methods are correctly implemented.',
    },
    "MR009": {
        'message': 'Module already exists in the registry.',
        'http_status': 409,  # Conflict
        'severity': 'ERROR',
        'description': 'The module being registered is already present in the module registry.',
        'resolution': 'Ensure the module is not already added or use a unique name for registration.',
    },
    "MR010": {
        'message': 'Error while registering module.',
        'http_status': 500,  # Internal Server Error
        'severity': 'ERROR',
        'description': 'An unexpected error occurred while trying to register a module.',
        'resolution': 'Check the module implementation and ensure it is compatible with the registry.',
    }
}

add_error_codes(MODULE_REGISTRY_ERROR_CODES)

class ModuleRegistry:
    def __init__(self):
        self.modules = {}  # Dictionary to store registered modules
        print_tracer("ModuleRegistry", "__init__", "Initialization", "ModuleRegistry initialized.")



    def remove_module(self, module_name: str) -> bool:
        """
        Remove a module from the registry.
        Args:
        - module_name (str): Name of the module to be removed.

        Returns:
        - bool: True if the module was successfully removed, False otherwise.
        """
        print_tracer("ModuleRegistry", "remove_module", "Start", f"Attempting to remove {module_name}.")
        
        # Check if module exists in the registry
        if module_name not in self.modules:
            error_details = MODULE_REGISTRY_ERROR_CODES["MR002"]
            print_tracer("ModuleRegistry", "remove_module", "Error", error_details['message'])
            return False
        
        # Remove module from the registry
        del self.modules[module_name]
        print_tracer("ModuleRegistry", "remove_module", "End", f"{module_name} successfully removed.")
        return True


    def execute_module_method(self, module_name: str, method_name: str, *args, **kwargs):
        """
        Execute a method from a registered module.
        Args:
        - module_name (str): Name of the module.
        - method_name (str): Name of the method to be executed.
        - *args, **kwargs: Arguments to pass to the method.

        Returns:
        - Result of the executed method or None if an error occurs.
        """
        print_tracer("ModuleRegistry", "execute_module_method", "Start")

        module_instance = self.modules.get(module_name)
        if not module_instance:
            error_details = MODULE_REGISTRY_ERROR_CODES["MR003"]
            print_tracer("ModuleRegistry", "execute_module_method", "Error", error_details['message'])
            return error_details

        try:
            method = getattr(module_instance, method_name)
            result = method(*args, **kwargs)
            print_tracer("ModuleRegistry", "execute_module_method", "End", f"{method_name} executed successfully.")
            return result
        except AttributeError:
            error_details = MODULE_REGISTRY_ERROR_CODES["MR004"]
            print_tracer("ModuleRegistry", "execute_module_method", "Error", error_details['message'])
            return error_details
        except Exception as e:
            error_details = MODULE_REGISTRY_ERROR_CODES["MR005"]
            print_tracer("ModuleRegistry", "execute_module_method", "Error", f"{error_details['message']}. Exception: {str(e)}")
            return error_details

    def get_registered_modules(self):
        """
        Fetch the list of registered modules.
        Returns:
        - List of registered module names.
        """
        print_tracer("ModuleRegistry", "get_registered_modules", "Start")
        
        try:
            module_list = list(self.modules.keys())
            print_tracer("ModuleRegistry", "get_registered_modules", "End")
            return module_list
        except Exception as e:
            error_details = MODULE_REGISTRY_ERROR_CODES["MR006"]
            print_tracer("ModuleRegistry", "get_registered_modules", "Error", f"{error_details['message']}. Exception: {str(e)}")
            return error_details

    def get_module_methods(self, module_name: str):
        """
        Fetch the methods of a specific registered module.
        Args:
        - module_name (str): Name of the module.

        Returns:
        - List of method names from the module or None if module not found.
        """
        print_tracer("ModuleRegistry", "get_module_methods", "Start", f"Fetching methods for {module_name}.")
        
        module_instance = self.modules.get(module_name)
        if not module_instance:
            error_details = handle_error("MR004")  # Assuming MR004 corresponds to "Module not found in registry"
            print_tracer("ModuleRegistry", "get_module_methods", "Error", error_details['message'])
            return None

        methods = get_methods(module_instance)
        if not methods:
            error_details = handle_error("MR005")  # Assuming MR005 corresponds to "Unable to fetch methods for the module"
            print_tracer("ModuleRegistry", "get_module_methods", "Error", error_details['message'])
            return None

        print_tracer("ModuleRegistry", "get_module_methods", "End", f"Methods fetched for {module_name}.")
        return methods
    
    def register_module(self, module_name: str, module_instance):
        """
        Register a new module into the ModuleRegistry.
        
        Args:
        - module_name (str): Name of the module.
        - module_instance: Instance of the module to be registered.

        Returns:
        - dict: A dictionary containing status (success/error), message, and any additional data.
        """
        print_tracer("ModuleRegistry", "register_module", "Start")

        if module_name in self.modules:
            print_tracer("ModuleRegistry", "register_module", "Error", f"Module {module_name} already exists in the registry.")
            return {
                'status': 'error',
                'message': f"Module {module_name} already exists in the registry."
            }

        try:
            self.modules[module_name] = module_instance
            print_tracer("ModuleRegistry", "register_module", "End", f"Module {module_name} registered successfully.")
            return {
                'status': 'success',
                'message': f"Module {module_name} registered successfully."
            }
        except Exception as e:
            error_details = handle_error("MR004")  # Assuming MR003 corresponds to "Error while registering module"
            print_tracer("ModuleRegistry", "register_module", "Error", f"{error_details['message']}. Exception: {str(e)}")
            return {
                'status': 'error',
                'message': error_details['message'],
                'exception': str(e)
            }
    def register_module(self, module_name: str, module_instance):
        """
        Register a new module into the ModuleRegistry.
        
        Args:
        - module_name (str): Name of the module.
        - module_instance: Instance of the module to be registered.

        Returns:
        - dict: A dictionary containing status (success/error), message, and any additional data.
        """
        print_tracer("ModuleRegistry", "register_module", "Start")

        if module_name in self.modules:
            print_tracer("ModuleRegistry", "register_module", "Error", f"Module {module_name} already exists in the registry.")
            return {
                'status': 'error',
                'message': f"Module {module_name} already exists in the registry."
            }

        try:
            self.modules[module_name] = module_instance
            print_tracer("ModuleRegistry", "register_module", "End", f"Module {module_name} registered successfully.")
            return {
                'status': 'success',
                'message': f"Module {module_name} registered successfully."
            }
        except Exception as e:
            error_details = handle_error("MR004")
            print_tracer("ModuleRegistry", "register_module", "Error", f"{error_details['message']}. Exception: {str(e)}")
            return {
                'status': 'error',
                'message': error_details['message'],
                'exception': str(e)
            }
if __name__=="__main__":
    instance = ModuleRegistry()
    get_methods(instance)