import logging
from pyairtable import Api
from modules.utils.utils import get_methods

# Initialize logging
logging.basicConfig(filename='read_operations_error.log', level=logging.ERROR)

class Read:
    """Encapsulates read operations for AirtableClient. Provides methods to retrieve bases, tables, and records."""
    
    def __init__(self, parent):
        """Initializes Read with inherited keys from the parent AirtableClient."""
        self.api = parent.api
        self.active_baseID = parent.active_baseID
        self.table_dictionary = parent.table_dictionary

    def get_methods(self):
        """Return methods available in Read class."""
        try:
            return get_methods(self)
        except Exception as e:
            logging.error(f"Error in get_methods: {e}")
            return {}

    def get_tables(self):
        """Fetches all tables and returns dict_keys of table names."""
        try:
            return self.table_dictionary.keys()
        except Exception as e:
            logging.error(f"Error fetching tables: {e}")
            return []

    def get_records(self, table_name):
        """Fetches all records from specified table_name, returns list of dictionary records."""
        try:
            table_id = self.table_dictionary.get(table_name)
            if not table_id:
                raise ValueError(f"Invalid table name: {table_name}")
            table = self.api.table(self.active_baseID, table_id)
            records = table.all()
            return records
        except Exception as e:
            logging.error(f"Error fetching records for table {table_name}: {e}")
            return []
        
    def get_record_by_id(self, table_name, record_id):
        """
        Fetches a single record by its ID from the specified table.
        
        Args:
            table_name (str): The name of the table to fetch the record from.
            record_id (str): The ID of the record to fetch.
            
        Returns:
            dict: A dictionary representing the record, or None if the record is not found.
        """
        try:
            table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
            record = table.get(record_id)
            return record
        except Exception as e:
            logging.error(f"Failed to get record by ID: {str(e)}")
            return None  # or however you want to handle errors

    def get_records_with_filter(self, table_name, filter_expression):
        """
        Fetches records from the specified table that match a given filter expression.
        
        Args:
            table_name (str): The name of the table to fetch records from.
            filter_expression (str): The filter expression to apply.
            
        Returns:
            list: A list of dictionaries representing the records that match the filter expression, or an empty list if no records match.
        """
        try:
            table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
            records = table.search(filter=filter_expression)
            return records
        except Exception as e:
            logging.error(f"Failed to get records with filter: {str(e)}")
            return []  # or however you want to handle errors
    
    def get_records_sorted(self, table_name, sort_field, ascending=True):
        """
        Fetches all records from a specified table, sorted by a specified field.
        
        Args:
            table_name (str): The name of the table to fetch records from.
            sort_field (str): The name of the field to sort records by.
            ascending (bool): Determines the order of sorting. If True, records are sorted in ascending order. Defaults to True.
            
        Returns:
            list: A list of dictionary records from the specified table, sorted by the specified field.
        """
        try:
            # Access a table by name from the active base ID and table dictionary
            table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
            # Use the table instance to get all records, sorted by the specified field
            records = table.all(sort=[(sort_field, ascending)])
            return records
        except Exception as e:
            logging.error(f"Error in get_records_sorted: {str(e)}")
            return None
    
    def get_records_paginated(self, table_name, page_size, page_number):
        """Fetches a paginated set of records from a specified table."""
        try:
            table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
            offset = (page_number - 1) * page_size
            records = table.all(max_records=page_size, offset=offset)
            return records
        except Exception as e:
            logging.error(f"Error fetching paginated records for table {table_name}: {e}")
            return []
    
    def get_records_by_date_range(self, table_name, start_date, end_date):
        """
        Fetches records from a specified table that fall within a specified date range.
        
        Args:
            table_name (str): The name of the table to fetch records from.
            start_date (str): The start date of the date range (inclusive) in 'YYYY-MM-DD' format.
            end_date (str): The end date of the date range (inclusive) in 'YYYY-MM-DD' format.
            
        Returns:
            list: A list of dictionary records from the specified table that fall within the specified date range.
        """
        try:
            # Access a table by name from the active base ID and table dictionary
            table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
            # Create a formula to filter records based on the date range
            formula = f"AND({{Date Field}} >= '{start_date}', {{Date Field}} <= '{end_date}')"
            # Use the table instance to get a set of records that meet the formula criteria
            records = table.search(formula=formula)
            return records
        except Exception as e:
            logging.error(f"Error in get_records_by_date_range: {str(e)}")
            return None
    
    def get_records_with_fields(self, table_name, fields_list):
        """
        Fetches specified fields from all records in a specified table.
        
        Args:
            table_name (str): The name of the table to fetch records from.
            fields_list (list): A list of field names to retrieve.
            
        Returns:
            list: A list of dictionary records with specified fields from the specified table.
        """
        try:
            # Access a table by name from the active base ID and table dictionary
            table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
            # Use the table instance to get all records, but only retrieve specified fields
            records = table.all(fields=fields_list)
            return records
        except Exception as e:
            logging.error(f"Error in get_records_with_fields: {str(e)}")
            return None
    
    def search_records(self, table_name, query):
        """
        Searches for records in a specified table based on a query.
        
        Args:
            table_name (str): The name of the table to search records in.
            query (str): The query string to use for searching records.
            
        Returns:
            list: A list of dictionary records matching the query from the specified table.
        """
        try:
            # Access a table by name from the active base ID and table dictionary
            table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
            # Use the table instance to search for records matching the query
            records = table.search(query)
            return records
        except Exception as e:
            logging.error(f"Error in search_records: {str(e)}")
            return None