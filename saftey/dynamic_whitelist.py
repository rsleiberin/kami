# Import required modules
import json

class DynamicWhitelist:
    def __init__(self):
        # Load the existing whitelist from a file or initialize an empty one
        try:
            with open('whitelist.json', 'r') as f:
                self.whitelist = json.load(f)
        except FileNotFoundError:
            self.whitelist = {}

    def add_to_whitelist(self, class_name, module_name):
        # Add a class to the whitelist
        self.whitelist[class_name] = module_name
        self._save()

    def remove_from_whitelist(self, class_name):
        # Remove a class from the whitelist
        if class_name in self.whitelist:
            del self.whitelist[class_name]
            self._save()

    def is_whitelisted(self, class_name):
        # Check if a class is in the whitelist
        return class_name in self.whitelist

    def _save(self):
        # Save the current state of the whitelist to a file
        with open('whitelist.json', 'w') as f:
            json.dump(self.whitelist, f)

# Example usage:
# whitelist = DynamicWhitelist()
# whitelist.add_to_whitelist("SomeClass", "some_module")
