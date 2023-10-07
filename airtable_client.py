from airtable import Airtable
import config

BASE_ID = config.AIRTABLE_BASE_ID
airtable = Airtable(BASE_ID, api_key=config.AIRTABLE_PERSONAL_ACCESS_TOKEN)
