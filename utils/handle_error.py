from utils.print_tracer import print_tracer
from constants.error_codes import ERROR_CODES

def handle_error(error_code: str):
    """
    Fetches the appropriate message, HTTP status code, severity, description, and resolution for a given error code.
    """
    print_tracer("Utils", "handle_error", f"Retrieving error details for code {error_code}")
    
    try:
        error_info = ERROR_CODES.get(error_code, ERROR_CODES['GEN001'])
        print_tracer("Utils", "handle_error", f"Error details retrieved successfully for code {error_code}")
        return error_info
    except Exception as e:
        # Fallback if there's an issue retrieving the error info
        print_tracer("Utils", "handle_error", f"Error encountered while retrieving error details for code {error_code}")
        return {
            'message': f"Error in handle_error: {str(e)}",
            'http_status': 500,
            'severity': 'ERROR',
            'description': 'An error occurred while handling another error.',
            'resolution': 'Check the traceback for more details.',
        }