# error_codes.py

ERROR_CODES = {
    # General Errors
    'GEN001': {
        'message': 'Unknown error occurred',
        'http_status': 500,
    },
    'GEN002': {
        'message': 'Invalid request',
        'http_status': 400,
    },
    # Airtable Client Errors
    'AIR001': {
        'message': 'Failed to fetch data from Airtable',
        'http_status': 503,
    },
    'AIR002': {
        'message': 'Invalid Airtable configuration',
        'http_status': 400,
    },
    # LLMSwitcher Errors
    'LLM001': {
        'message': 'Failed to initialize LLMSwitcher',
        'http_status': 500,
    },
    'LLM002': {
        'message': 'Error in LLMSwitcher get_methods',
        'http_status': 500,
    },'LLM004': {
        'message': 'Module not found in LLMSwitcher',
        'http_status': 400,
    },
    'LLM005': {
        'message': 'Error executing method in LLMSwitcher',
        'http_status': 500,
    },
    'LLM006': {
        'message': 'Error fetching methods for module in LLMSwitcher',
        'http_status': 400,
    },'LLM007': {
        'message': "Attribute 'gpt' has not been initialized in LLMSwitcher.",
        'http_status': 500,
    },'LLM008': {
        'message': "The model object does not have a 'perform' method.",
        'http_status': 500,
    },
    'LLM009': {
        'message': "No suitable model found for the task.",
        'http_status': 500,
    },'LLM010': {
        'message': "Class not found in the module.",
        'http_status': 500,
    },
    'LLM011': {
        'message': "Failed to import module.",
        'http_status': 500,
    },'LLM012': {
        'message': "Module not registered.",
        'http_status': 404,
    },
    'LLM013': {
        'message': "Method not callable in module.",
        'http_status': 400,
    },
    'LLM014': {
        'message': "Method not found in module.",
        'http_status': 404,
    },
}
