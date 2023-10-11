from modules.utils.utils import get_methods
from modules.databases.airtable_client.airtable_client import AirtableClient
import config

def test_get_methods():
    airtable_instance = AirtableClient(config.AIRTABLE_PERSONAL_ACCESS_TOKEN)
    methods = get_methods(airtable_instance)
    print(methods)

if __name__ == "__main__":
    test_get_methods()
