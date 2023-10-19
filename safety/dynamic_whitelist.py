import json
from utils.utils import print_tracer  # application libraries

class DynamicWhitelist:
    """
    Manages a dynamic whitelist for function execution.
    """

    def __init__(self):
        """
        Initializes the whitelist by loading it from a JSON file.
        """
        print_tracer("DynamicWhitelist", "__init__", "Start")
        try:
            with open('whitelist.json', 'r') as f:
                self.whitelist = json.load(f)
        except FileNotFoundError:
            print_tracer("DynamicWhitelist", "__init__", "Error", "whitelist.json not found")
            self.whitelist = {}
        print_tracer("DynamicWhitelist", "__init__", "End")

    def add_to_whitelist(self, class_name, module_name):
        """
        Adds a given class to the whitelist and saves the updated whitelist.
        """
        print_tracer("DynamicWhitelist", "add_to_whitelist", "Start")
        self.whitelist[class_name] = module_name
        self._save()
        print_tracer("DynamicWhitelist", "add_to_whitelist", "End")

    def remove_from_whitelist(self, class_name):
        """
        Removes a given class from the whitelist and saves the updated whitelist.
        """
        print_tracer("DynamicWhitelist", "remove_from_whitelist", "Start")
        if class_name in self.whitelist:
            del self.whitelist[class_name]
            self._save()
        else:
            raise KeyError(f"{class_name} not found in whitelist.")
        print_tracer("DynamicWhitelist", "remove_from_whitelist", "End")

    def is_whitelisted(self, class_name):
        """
        Checks if a given class is in the whitelist.
        """
        print_tracer("DynamicWhitelist", "is_whitelisted", "Start")
        result = class_name in self.whitelist
        print_tracer("DynamicWhitelist", "is_whitelisted", "End")
        return result

    def _save(self):
        """
        Saves the current whitelist to a JSON file.
        """
        print_tracer("DynamicWhitelist", "_save", "Start")
        with open('whitelist.json', 'w') as f:
            json.dump(self.whitelist, f)
        print_tracer("DynamicWhitelist", "_save", "End")
