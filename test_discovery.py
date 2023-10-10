import os
import logging
import unittest
import importlib
from modules.utils.utils import get_module_info

def find_untested_modules(modules_dir, tests_dir):
    untested_modules = []

    try:
        # Get the list of all module subdirectories
        module_subdirs = [d for d in os.listdir(modules_dir) if os.path.isdir(os.path.join(modules_dir, d))]
        print(f'Module Subdirectories: {module_subdirs}')  # Debugging output
    except Exception as e:
        logging.error(f'Error listing subdirectories in {modules_dir}: {e}')
        return untested_modules  # Return empty list on error

    for module_subdir in module_subdirs:
        module_dir = os.path.join(modules_dir, module_subdir)
        try:
            # Get the list of all Python files in the module subdirectory
            module_files = [f for f in os.listdir(module_dir) if f.endswith('.py')]
            print(f'Processing {module_dir}: {module_files}')  # Debugging output
        except Exception as e:
            logging.error(f'Error listing files in {module_dir}: {e}')
            continue  # Skip to the next subdirectory on error

        for module_file in module_files:
            # Create the name of the corresponding test file
            test_file_name = f'test_{module_file}'

            # Debugging output
            print(f'Generated test file name: {test_file_name}')

            # Check if the test file exists in the tests directory
            test_file_path = os.path.join(tests_dir, test_file_name)

            # Debugging output
            print(f'Checking for test file at: {test_file_path}')
            print(f'Test file exists: {os.path.exists(test_file_path)}')

            if not os.path.exists(test_file_path):
                untested_modules.append(os.path.join(module_subdir, module_file))

    return untested_modules

def get_module_info_from_path(module_path):
    # Convert the module file path to a module name
    module_name = module_path.replace('/', '.').rstrip('.py')
    # Import the module
    module = importlib.import_module(module_name)
    # Get the module info
    return get_module_info(module)

def print_untested_modules_info(untested_modules, modules_dir):
    """Prints the information of untested modules to the console.

    Args:
        untested_modules (list): List of untested module files.
        modules_dir (str): Path to the directory containing module files.
    """
    for untested_module in untested_modules:
        try:
            module_info = get_module_info_from_path(untested_module)
            print(f'{untested_module}: {module_info}')  # Print the module info to the console for now
        except Exception as e:
            logging.error(f'Error getting module info for {untested_module}: {e}')

def generate_test_file(module_path, modules_dir, tests_dir):
    module_name = module_path.split('/')[-1].replace('.py', '')  # Extract the module name from the module path
    test_file_name = f'test_{module_name}.py'
    test_file_path = os.path.join(tests_dir, test_file_name)
    test_class_name = f'Test{module_name.capitalize()}'
    
    test_file_content = f"""import unittest
from {modules_dir.replace('./', '').replace('/', '.')}.{module_name} import {module_name}

class {test_class_name}(unittest.TestCase):

    def test_example(self):
        pass

if __name__ == '__main__':
    unittest.main()
"""
    with open(test_file_path, 'w') as test_file:
        test_file.write(test_file_content)
    print(f'Test file generated: {test_file_path}')

if __name__ == "__main__":
    modules_dir = './modules'
    tests_dir = './tests'
    
    try:
        untested_modules = find_untested_modules(modules_dir, tests_dir)
        print(untested_modules)  # Prints a list of module files that do not have corresponding test files
        
        for untested_module in untested_modules:
            generate_test_file(untested_module, modules_dir, tests_dir)
    except Exception as e:
        logging.error(f'Error in main: {e}')