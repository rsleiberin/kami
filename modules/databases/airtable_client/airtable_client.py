import sys
import logging
from pyairtable import Api
from modules.utils.utils import get_methods
from modules.databases.airtable_client.read_operations import Read
import config

# Adding system path
sys.path.append('/home/tank/kami')

# Initialize error logger
logging.basicConfig(filename='airtable_error.log', level=logging.ERROR)

# Define dictionary of tables
static_table_dictionary = {
    'AgentMessages': 'tblHwP2S9wrLSXZ8X',
    'Tables': 'tbl1e2TVk2Gsl67h0',
    'Keywords': 'tblIuO0o4RXt3XuOM',
    'Roles': 'tblzW4VZbCWanIIyN',
    'UserMessages': 'tblgb0zcBcICKsBuL',
    'Sockets': 'tblIx8uynrcs0U1oY',
    'Contexts': 'tblnM5iAC07MKkBE5',
    'AuditLogs': 'tblBPD6bMP4OKXsvv',
    'Changes': 'tblgPFTxtKkknnfP7',
    'Responses': 'tblLzPyyqqHA5LX37',
    'ResponseKeywords': 'tblEHTG1qWWGjhWUd',
    'Models': 'tblnS11drSEKpG1fF',
    'AgentSockets': 'tblecadjyehlqBwEk',
    'Agents': 'tbl9aWKqXf4pBZgYo',
    'Sessions': 'tbl0rofsENuhTICPT',
    'Users': 'tblpn8f66jTilogu1'
}

class AirtableClient:
    def __init__(self, api_key):
        """
        Initializes AirtableClient with API key.

        Args:
            api_key (str): The API key for Airtable.
        """
        try:
            self.api = Api(api_key)
            self.base_dictionary = {'Kami': config.AIRTABLE_BASE_ID}
            self.active_baseID = self.base_dictionary['Kami']
            self.table_dictionary = static_table_dictionary
            self.Read = self.initialize_read()
        except Exception as e:
            logging.error(f"Error initializing AirtableClient: {e}")
            raise

    def initialize_read(self):
        """
        Initializes and returns an instance of the Read class.

        Returns:
            Read: An instance of the Read class.
        """
        try:
            return Read(self)
        except Exception as e:
            logging.error(f"Error initializing Read class: {e}")
            raise

    def get_methods(self):
        """Return methods available in AirtableClient."""
        try:
            return get_methods(self)
        except Exception as e:
            logging.error(f"Error fetching methods for AirtableClient: {e}")
            return {}

if __name__ == "__main__":
    airtable = AirtableClient(config.AIRTABLE_PERSONAL_ACCESS_TOKEN)
    print(airtable.get_methods())
