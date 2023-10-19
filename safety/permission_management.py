# Import required modules
import os
import json
from utils.utils import print_tracer  # Import print_tracer for debugging and context

# Function to load the whitelist
def load_whitelist() -> dict:
    """
    Loads the whitelist from 'whitelist.json'.
    
    Returns:
        dict: The whitelist dictionary.
    """
    print_tracer("permission_management", "load_whitelist", "Start")
    try:
        with open('whitelist.json', 'r') as f:
            whitelist = json.load(f)
    except FileNotFoundError:
        print_tracer("permission_management", "load_whitelist", "Error", "whitelist.json not found")
        whitelist = {}
    
    print_tracer("permission_management", "load_whitelist", "End")
    return whitelist

# Function to load user permissions
def load_user_permissions() -> dict:
    """
    Loads the user permissions from 'user_permissions.json'.
    
    Returns:
        dict: The user permissions dictionary.
    """
    print_tracer("permission_management", "load_user_permissions", "Start")
    user_permissions_file = "user_permissions.json"
    
    try:
        if os.path.exists(user_permissions_file):
            with open(user_permissions_file, 'r') as f:
                user_permissions = json.load(f)
        else:
            print_tracer("permission_management", "load_user_permissions", "Error", "user_permissions.json not found. Creating a new one.")
            with open(user_permissions_file, 'w') as f:
                json.dump({}, f)
            user_permissions = {}
    except Exception as e:
        print_tracer("permission_management", "load_user_permissions", "Error", str(e))
        user_permissions = {}
    
    print_tracer("permission_management", "load_user_permissions", "End")
    return user_permissions
