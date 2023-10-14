from datetime import datetime
import logging
from modules.utils.error_handler import handle_error
logging.basicConfig(level=logging.DEBUG)


class Read:
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
            error_message, http_status = handle_error('READ001')  # Assuming 'READ001' is the error code for Read initialization
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            raise  # Re-raise the exception to ensure it gets caught higher up

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
            error_message, http_status = handle_error('READ002')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.1-Exception in Read-get_methods | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
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
            error_message, http_status = handle_error('READ003')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.2-Exception in Read-get_tables | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
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
            error_message, http_status = handle_error('READ004')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.3-Exception in Read-get_records | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
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
            table_id = self.table_dictionary.get(table_name)
            if not table_id:
                raise ValueError(f"Invalid table name: {table_name}")
            table = self.api.table(self.active_baseID, table_id)
            record = table.get(record_id)
            return record
        except Exception as e:
            error_message, http_status = handle_error('READ005')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.4-Exception in Read-get_record_by_id | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return None

    def get_records_with_filter(self, table_name, filter_expression):
        """
        Fetches records from the specified table that match a given filter expression.
        ---
        Debug Tag: DT.4.5-Read-get_records_with_filter
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.5-Read-get_records_with_filter | Time: {timestamp}")

        try:
            table_id = self.table_dictionary.get(table_name)
            if not table_id:
                raise ValueError(f"Invalid table name: {table_name}")
            table = self.api.table(self.active_baseID, table_id)
            records = table.search(filter=filter_expression)
            return records
        except Exception as e:
            error_message, http_status = handle_error('READ006')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.5-Exception in Read-get_records_with_filter | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return []
    
    def get_records_sorted(self, table_name, sort_field, ascending=True):
        """
        Fetches all records from a specified table, sorted by a specified field.
        ---
        Debug Tag: DT.4.6-Read-get_records_sorted
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.6-Read-get_records_sorted | Time: {timestamp}")

        try:
            table_id = self.table_dictionary.get(table_name)
            if not table_id:
                raise ValueError(f"Invalid table name: {table_name}")
            table = self.api.table(self.active_baseID, table_id)
            records = table.all(sort=[(sort_field, ascending)])
            return records
        except Exception as e:
            error_message, http_status = handle_error('READ007')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.6-Exception in Read-get_records_sorted | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return []
    
    def get_records_paginated(self, table_name, page_size, page_number):
        """
        Fetches a paginated set of records from a specified table.
        ---
        Debug Tag: DT.4.7-Read-get_records_paginated
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.7-Read-get_records_paginated | Time: {timestamp}")

        try:
            table_id = self.table_dictionary.get(table_name)
            if not table_id:
                raise ValueError(f"Invalid table name: {table_name}")
            table = self.api.table(self.active_baseID, table_id)
            offset = (page_number - 1) * page_size
            records = table.all(max_records=page_size, offset=offset)
            return records
        except Exception as e:
            error_message, http_status = handle_error('READ008')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.7-Exception in Read-get_records_paginated | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return []
    
    def get_records_by_date_range(self, table_name, start_date, end_date):
        """
        Fetches records from a specified table that fall within a specified date range.
        ---
        Debug Tag: DT.4.8-Read-get_records_by_date_range
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.8-Read-get_records_by_date_range | Time: {timestamp}")

        try:
            table_id = self.table_dictionary.get(table_name)
            if not table_id:
                raise ValueError(f"Invalid table name: {table_name}")
            table = self.api.table(self.active_baseID, table_id)
            formula = f"AND({{Date Field}} >= '{start_date}', {{Date Field}} <= '{end_date}')"
            records = table.search(formula=formula)
            return records
        except Exception as e:
            error_message, http_status = handle_error('READ009')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.8-Exception in Read-get_records_by_date_range | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return None
    
    def get_records_with_fields(self, table_name, fields_list):
        """
        Fetches specified fields from all records in a specified table.
        ---
        Debug Tag: DT.4.9-Read-get_records_with_fields
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.9-Read-get_records_with_fields | Time: {timestamp}")

        try:
            table_id = self.table_dictionary.get(table_name)
            if not table_id:
                raise ValueError(f"Invalid table name: {table_name}")
            table = self.api.table(self.active_baseID, table_id)
            records = table.all(fields=fields_list)
            return records
        except Exception as e:
            error_message, http_status = handle_error('READ010')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.9-Exception in Read-get_records_with_fields | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return None
    
    def search_records(self, table_name, query):
        """
        Searches for records in a specified table based on a query.
        ---
        Debug Tag: DT.4.10-Read-search_records
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4.10-Read-search_records | Time: {timestamp}")

        try:
            table_id = self.table_dictionary.get(table_name)
            if not table_id:
                raise ValueError(f"Invalid table name: {table_name}")
            table = self.api.table(self.active_baseID, table_id)
            records = table.search(query=query)
            return records
        except Exception as e:
            error_message, http_status = handle_error('READ011')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4.10-Exception in Read-search_records | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return None