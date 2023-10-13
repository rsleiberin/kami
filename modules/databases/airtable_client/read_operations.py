import logging
from pyairtable import Api
from modules.utils.utils import get_methods
from datetime import datetime

# Initialize logging
logging.basicConfig(filename='read_operations_error.log', level=logging.ERROR)

class Read:
    """Encapsulates read operations for AirtableClient. Provides methods to retrieve bases, tables, and records."""

    def __init__(self, parent):
        """
        Initializes Read with inherited keys from the parent AirtableClient.
        ---
        Debug Tag: DT.4-Read-Initialization
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4-Read-Initialization | Time: {timestamp}")

        try:
            self.api = parent.api
            self.active_baseID = parent.active_baseID
            self.table_dictionary = parent.table_dictionary
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4-Exception in Read-Initialization | Time: {timestamp}")
            logging.error(f"Error in Read __init__: {e}")

    def get_methods(self):
        """
        Return methods available in Read class.
        ---
        Debug Tag: DT.4.1-Read-get_methods
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.1-Read-get_methods | Time: {timestamp}")
        
        try:
            return get_methods(self)
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.1-Exception in Read-get_methods | Time: {timestamp}")
            logging.error(f"Error in Read get_methods: {e}")
            return {}


    def get_tables(self):
        """
        Fetches all tables and returns dict_keys of table names.
        ---
        Debug Tag: DT.4.2-Read-get_tables
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.2-Read-get_tables | Time: {timestamp}")
        
        try:
            return self.table_dictionary.keys()
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.2-Exception in Read-get_tables | Time: {timestamp}")
            logging.error(f"Error in Read get_tables: {e}")
            return []

    def get_records(self, table_name):
        """
        Fetches all records from specified table_name, returns list of dictionary records.
        ---
        Debug Tag: DT.4.3-Read-get_records
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.3-Read-get_records | Time: {timestamp}")

        try:
            table_id = self.table_dictionary.get(table_name)
            if not table_id:
                raise ValueError(f"Invalid table name: {table_name}")
            table = self.api.table(self.active_baseID, table_id)
            records = table.all()
            return records
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.3-Exception in Read-get_records | Time: {timestamp}")
            logging.error(f"Error fetching records for table {table_name}: {e}")
            return []
        
    def get_record_by_id(self, table_name, record_id):
        """
        Fetches a single record by its ID from the specified table.
        ---
        Debug Tag: DT.4.4-Read-get_record_by_id
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.4-Read-get_record_by_id | Time: {timestamp}")

        try:
            table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
            record = table.get(record_id)
            return record
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.4-Exception in Read-get_record_by_id | Time: {timestamp}")
            logging.error(f"Failed to get record by ID: {str(e)}")
            return None  # or however you want to handle errors

    def get_records_with_filter(self, table_name, filter_expression):
        """
        Fetches records from the specified table that match a given filter expression.
        ---
        Debug Tag: DT.4.5-Read-get_records_with_filter
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.5-Read-get_records_with_filter | Time: {timestamp}")

        try:
            table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
            records = table.search(filter=filter_expression)
            return records
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.5-Exception in Read-get_records_with_filter | Time: {timestamp}")
            logging.error(f"Failed to get records with filter: {str(e)}")
            return []  # or however you want to handle errors
    
    def get_records_sorted(self, table_name, sort_field, ascending=True):
        """
        Fetches all records from a specified table, sorted by a specified field.
        ---
        Debug Tag: DT.4.6-Read-get_records_sorted
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.6-Read-get_records_sorted | Time: {timestamp}")

        try:
            # Access a table by name from the active base ID and table dictionary
            table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
            # Use the table instance to get all records, sorted by the specified field
            records = table.all(sort=[(sort_field, ascending)])
            return records
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.6-Exception in Read-get_records_sorted | Time: {timestamp}")
            logging.error(f"Error in get_records_sorted: {str(e)}")
            return None  # or however you want to handle errors
    
    def get_records_paginated(self, table_name, page_size, page_number):
        """
        Fetches a paginated set of records from a specified table.
        ---
        Debug Tag: DT.4.7-Read-get_records_paginated
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.7-Read-get_records_paginated | Time: {timestamp}")

        try:
            table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
            offset = (page_number - 1) * page_size
            records = table.all(max_records=page_size, offset=offset)
            return records
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.7-Exception in Read-get_records_paginated | Time: {timestamp}")
            logging.error(f"Error fetching paginated records for table {table_name}: {e}")
            return []  # or however you want to handle errors
    
    def get_records_by_date_range(self, table_name, start_date, end_date):
        """
        Fetches records from a specified table that fall within a specified date range.
        ---
        Debug Tag: DT.4.8-Read-get_records_by_date_range
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.8-Read-get_records_by_date_range | Time: {timestamp}")

        try:
            # Access a table by name from the active base ID and table dictionary
            table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
            # Create a formula to filter records based on the date range
            formula = f"AND({{Date Field}} >= '{start_date}', {{Date Field}} <= '{end_date}')"
            # Use the table instance to get a set of records that meet the formula criteria
            records = table.search(formula=formula)
            return records
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.8-Exception in Read-get_records_by_date_range | Time: {timestamp}")
            logging.error(f"Error in get_records_by_date_range: {str(e)}")
            return None  # or however you want to handle errors
    
    def get_records_with_fields(self, table_name, fields_list):
        """
        Fetches specified fields from all records in a specified table.
        ---
        Debug Tag: DT.4.9-Read-get_records_with_fields
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.9-Read-get_records_with_fields | Time: {timestamp}")

        try:
            # Access a table by name from the active base ID and table dictionary
            table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
            # Use the table instance to get all records, but only retrieve specified fields
            records = table.all(fields=fields_list)
            return records
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.9-Exception in Read-get_records_with_fields | Time: {timestamp}")
            logging.error(f"Error in get_records_with_fields: {str(e)}")
            return None  # or however you want to handle errors
    
    def search_records(self, table_name, query):
        """
        Searches for records in a specified table based on a query.
        ---
        Debug Tag: DT.4.10-Read-search_records
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.10-Read-search_records | Time: {timestamp}")

        try:
            # Access a table by name from the active base ID and table dictionary
            table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
            # Use the table instance to search for records matching the query
            records = table.search(query)
            return records
        except Exception as e:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.10-Exception in Read-search_records | Time: {timestamp}")
            logging.error(f"Error in search_records: {str(e)}")
            return None  # or however you want to handle errors