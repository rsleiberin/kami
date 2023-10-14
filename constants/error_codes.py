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
    #Test Errors
    'TEST001': {
        'message': 'Test failed during execution.',
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
    'AIR003': {
        'message': 'Error initializing Read class',
        'http_status': 500,
    },
    'AIR004': {
        'message': 'Error fetching methods for AirtableClient',
        'http_status': 500,
    },
    #AirtableClient Read Operations Errors
    'READ001': {
        'message': 'Failed to initialize the Read class.',
        'http_status': 500  # Internal Server Error
    },
    'READ002': {
        'message': 'Failed to retrieve methods in Read class.',
        'http_status': 500  # Internal Server Error
    },
    'READ003': {
        'message': 'Failed to fetch tables in Read class.',
        'http_status': 500  # Internal Server Error
    },
    'READ004': {
        'message': 'Failed to fetch records in Read class.',
        'http_status': 500  # Internal Server Error
    },
    'READ005': {
        'message': 'Failed to fetch a record by its ID in Read class.',
        'http_status': 500  # Internal Server Error
    },
    'READ006': {
        'message': 'Failed to fetch records with a given filter in Read class.',
        'http_status': 500  # Internal Server Error
    },
    'READ007': {
        'message': 'Failed to fetch sorted records in Read class.',
        'http_status': 500  # Internal Server Error
    },
    'READ009': {
        'message': 'Failed to fetch records by date range in Read class.',
        'http_status': 500  # Internal Server Error
    },
    'READ010': {
        'message': 'Failed to fetch records with specified fields in Read class.',
        'http_status': 500  # Internal Server Error
    },
    'READ011': {
        'message': 'Failed to search records in Read class.',
        'http_status': 500  # Internal Server Error
    },
    #Airtable Read Operations Errors
    'TEST_READ_INIT_001': {
        'message': 'Failed to initialize Read class in test environment',
        'http_status': 500,
    },
    'TEST_READ_GET_METHODS_001': {
        'message': 'Failed to test get_methods in Read class',
        'http_status': 500,
    },
    'TEST_READ_GET_TABLES_001': {
        'message': 'Failed to test get_tables in Read class',
        'http_status': 500,
    },
    'TEST_READ_GET_RECORDS_001': {
        'message': 'Failed to test get_records in Read class',
        'http_status': 500,
    },
    'TEST_READ_GET_RECORD_BY_ID_001': {
        'message': 'Failed to test get_record_by_id in Read class',
        'http_status': 500,
    },
    'TEST_READ_GET_RECORDS_WITH_FILTER_001': {
        'message': 'Failed to test get_records_with_filter in Read class',
        'http_status': 500,
    },
    'TEST_READ_GET_RECORDS_SORTED_001': {
        'message': 'Failed to test get_records_sorted in Read class',
        'http_status': 500,
    },
    'TEST_READ_GET_RECORDS_PAGINATED_001': {
        'message': 'Failed to test get_records_paginated in Read class',
        'http_status': 500,
    },
        'TEST_READ_GET_RECORDS_BY_DATE_RANGE_001': {
        'message': 'Failed to test get_records_by_date_range in Read class',
        'http_status': 500,
    },
    'TEST_READ_GET_RECORDS_WITH_FIELDS_001': {
        'message': 'Failed to test get_records_with_fields in Read class',
        'http_status': 500,
    },
    'TEST_READ_SEARCH_RECORDS_001': {
        'message': 'Failed to test search_records in Read class',
        'http_status': 500,
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
    # FunctionState Errors
    'FS001': {
        'message': 'Error initializing FunctionState',
        'http_status': 500,
    },
    'FS002': {
    'message': 'Error setting the function state in FunctionState.set',
    'http_status': 500,
    },
    'FS003': {
    'message': 'Error checking function repetition in FunctionState.check_repetition',
    'http_status': 500,
    },
    'FS004': {
    'message': 'Error fetching methods in FunctionState.get_methods',
    'http_status': 500,
    },
}
