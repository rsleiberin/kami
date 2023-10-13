from typing import Tuple
from constants.error_codes import ERROR_CODES

def handle_error(error_code: str) -> Tuple[str, int]:
    """
    Fetches the appropriate message and HTTP status code for a given error code.
    ---
    Debug Tag: DT.11-Utils-handle_error
    Debug Focus Log Tag: Error handling
    """
    try:
        error_info = ERROR_CODES.get(error_code, ERROR_CODES['GEN001'])
        return error_info['message'], error_info['http_status']
    except Exception as e:
        return f"Error in handle_error: {str(e)}", 500