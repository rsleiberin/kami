from datetime import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')

try:
    from modules.utils.error_handler import handle_error
    from modules.utils.utils import get_methods
    from modules.databases.airtable_client.airtable_client import AirtableClient
    import config
    logging.info("Imports successful.")
except Exception as e:
    logging.error(f"Import failed: {e}")
