import unittest
from unittest.mock import patch
from modules.databases.airtable_client.airtable_client import AirtableClient
from modules.databases.airtable_client.read_operations import Read
from modules.utils.error_handler import handle_error
from constants.error_codes import ERROR_CODES

class TestReadOperations(unittest.TestCase):

    def setUp(self):
        """
        Initialize variables or set up any necessary database connections.
        This method will be executed before each test in the class.
        """
        self.mock_api_key = "mock_api_key"  # This is a mock API key for testing purposes
        self.airtable_client = AirtableClient(self.mock_api_key)
        self.read_operations = Read(self.airtable_client)

    def tearDown(self):
        """
        Close database connections and clean up any changes.
        This method will be executed after each test in the class.
        """
        pass
    
    def test_read_initialization(self):
        """
        Test if the Read class is initialized properly.
        """
        try:
            # Arrange
            expected_api = self.airtable_client.api
            expected_baseID = self.airtable_client.active_baseID
            expected_table_dict = self.airtable_client.table_dictionary

            # Act
            read_operations = Read(self.airtable_client)
            
            # Assert
            self.assertEqual(read_operations.api, expected_api)
            self.assertEqual(read_operations.active_baseID, expected_baseID)
            self.assertEqual(read_operations.table_dictionary, expected_table_dict)

        except Exception as e:
            error_message, http_status = handle_error('TESTREAD001')
            self.fail(f"{error_message} | HTTP Status: {http_status} | Exception: {str(e)}")
    
    def test_get_methods(self):
        """
        Test if get_methods in Read class returns correct methods.
        """
        try:
            # Arrange
            read_instance = self.airtable_client.Read(self.airtable_client)  # Assuming you can access Read like this.
            
            # Act
            methods = read_instance.get_methods()
            
            # Assert
            self.assertIsInstance(methods, dict)  # Replace with the actual type and checks you need.
            
        except Exception as e:
            error_message, http_status = handle_error('TEST_READ_GET_METHODS_001')
            self.fail(f"{error_message} | HTTP Status: {http_status} | Exception: {str(e)}")
    
    def test_get_tables(self):
        """
        Test if get_tables in Read class returns correct table names.
        """
        try:
            # Arrange
            read_instance = self.airtable_client.Read(self.airtable_client)  # Assuming you can access Read like this.
            
            # Act
            tables = read_instance.get_tables()
            
            # Assert
            self.assertIsInstance(tables, dict_keys)  # Replace with the actual type and checks you need.
            
        except Exception as e:
            error_message, http_status = handle_error('TEST_READ_GET_TABLES_001')
            self.fail(f"{error_message} | HTTP Status: {http_status} | Exception: {str(e)}")
    
    def test_get_records(self):
        """
        Test if get_records in Read class returns correct records from a specified table.
        """
        try:
            # Arrange
            read_instance = self.airtable_client.Read(self.airtable_client)  # Assuming you can access Read like this.
            test_table_name = 'YourTestTableName'  # Replace with a table name for testing
            
            # Act
            records = read_instance.get_records(test_table_name)
            
            # Assert
            self.assertIsInstance(records, list)  # Make sure it returns a list
            # Further assertions based on what you expect in the records list can be added.
            
        except Exception as e:
            error_message, http_status = handle_error('TEST_READ_GET_RECORDS_001')
            self.fail(f"{error_message} | HTTP Status: {http_status} | Exception: {str(e)}")

    def test_get_record_by_id(self):
        """
        Test if get_record_by_id in Read class returns the correct record by its ID from a specified table.
        """
        try:
            # Arrange
            read_instance = self.airtable_client.Read(self.airtable_client)  # Assuming you can access Read like this.
            test_table_name = 'YourTestTableName'  # Replace with a table name for testing
            test_record_id = 'YourTestRecordID'  # Replace with a record ID for testing
            
            # Act
            record = read_instance.get_record_by_id(test_table_name, test_record_id)
            
            # Assert
            self.assertIsInstance(record, dict)  # Make sure it returns a dictionary
            # Further assertions based on what you expect in the record dictionary can be added.
            
        except Exception as e:
            error_message, http_status = handle_error('TEST_READ_GET_RECORD_BY_ID_001')
            self.fail(f"{error_message} | HTTP Status: {http_status} | Exception: {str(e)}")
            
    def test_get_records_with_filter(self):
        """
        Test if get_records_with_filter in Read class returns records that match the filter expression from a specified table.
        """
        try:
            # Arrange
            read_instance = self.airtable_client.Read(self.airtable_client)  # Assuming you can access Read like this.
            test_table_name = 'YourTestTableName'  # Replace with a table name for testing
            test_filter_expression = 'YourTestFilterExpression'  # Replace with a filter expression for testing
            
            # Act
            records = read_instance.get_records_with_filter(test_table_name, test_filter_expression)
            
            # Assert
            self.assertIsInstance(records, list)  # Make sure it returns a list
            # Further assertions based on what you expect in the records list can be added.
            
        except Exception as e:
            error_message, http_status = handle_error('TEST_READ_GET_RECORDS_WITH_FILTER_001')
            self.fail(f"{error_message} | HTTP Status: {http_status} | Exception: {str(e)}")
    
    def test_get_records_sorted(self):
        """
        Test if get_records_sorted in Read class returns sorted records from a specified table.
        """
        try:
            # Arrange
            read_instance = self.airtable_client.Read(self.airtable_client)  # Assuming you can access Read like this.
            test_table_name = 'YourTestTableName'  # Replace with a table name for testing
            test_sort_field = 'YourTestSortField'  # Replace with a sort field for testing
            
            # Act
            records = read_instance.get_records_sorted(test_table_name, test_sort_field)
            
            # Assert
            self.assertIsInstance(records, list)  # Make sure it returns a list
            # Further assertions based on what you expect in the records list can be added.
            
        except Exception as e:
            error_message, http_status = handle_error('TEST_READ_GET_RECORDS_SORTED_001')
            self.fail(f"{error_message} | HTTP Status: {http_status} | Exception: {str(e)}")

    def test_get_records_paginated(self):
        """
        Test if get_records_paginated in Read class returns paginated records from a specified table.
        """
        try:
            # Arrange
            read_instance = self.airtable_client.Read(self.airtable_client)  # Assuming you can access Read like this.
            test_table_name = 'YourTestTableName'  # Replace with a table name for testing
            test_page_size = 10  # Replace with a size for testing
            test_page_number = 1  # Replace with a page number for testing
            
            # Act
            records = read_instance.get_records_paginated(test_table_name, test_page_size, test_page_number)
            
            # Assert
            self.assertIsInstance(records, list)  # Make sure it returns a list
            self.assertEqual(len(records), test_page_size)  # Make sure it returns the expected number of records
            
        except Exception as e:
            error_message, http_status = handle_error('TEST_READ_GET_RECORDS_PAGINATED_001')
            self.fail(f"{error_message} | HTTP Status: {http_status} | Exception: {str(e)}")

    def test_get_records_by_date_range(self):
        """
        Test if get_records_by_date_range in Read class returns records within a specified date range.
        """
        try:
            # Arrange
            read_instance = self.airtable_client.Read(self.airtable_client)  # Assuming you can access Read like this.
            test_table_name = 'YourTestTableName'  # Replace with a table name for testing
            test_start_date = '2023-01-01'  # Replace with a start date for testing
            test_end_date = '2023-12-31'  # Replace with an end date for testing
            
            # Act
            records = read_instance.get_records_by_date_range(test_table_name, test_start_date, test_end_date)
            
            # Assert
            self.assertIsInstance(records, list)  # Make sure it returns a list
            
            for record in records:
                # Assuming 'Date Field' exists and contains a date string in the format 'YYYY-MM-DD'
                record_date = datetime.strptime(record['Date Field'], '%Y-%m-%d').date()
                self.assertTrue(test_start_date <= record_date <= test_end_date)  # Make sure records fall within the date range
            
        except Exception as e:
            error_message, http_status = handle_error('TEST_READ_GET_RECORDS_BY_DATE_RANGE_001')
            self.fail(f"{error_message} | HTTP Status: {http_status} | Exception: {str(e)}")
    
    def test_get_records_with_fields(self):
        """
        Test if get_records_with_fields in Read class returns records with specified fields.
        """
        try:
            # Arrange
            read_instance = self.airtable_client.Read(self.airtable_client)  # Assuming you can access Read like this.
            test_table_name = 'YourTestTableName'  # Replace with a table name for testing
            test_fields_list = ['Field1', 'Field2']  # Replace with fields that you want to test
            
            # Act
            records = read_instance.get_records_with_fields(test_table_name, test_fields_list)
            
            # Assert
            self.assertIsInstance(records, list)  # Make sure it returns a list
            
            for record in records:
                for field in test_fields_list:
                    self.assertIn(field, record)  # Make sure specified fields are present in each record
            
        except Exception as e:
            error_message, http_status = handle_error('TEST_READ_GET_RECORDS_WITH_FIELDS_001')
            self.fail(f"{error_message} | HTTP Status: {http_status} | Exception: {str(e)}")

    def test_search_records(self):
        """
        Test if search_records in Read class returns records based on a query.
        """
        try:
            # Arrange
            read_instance = self.airtable_client.Read(self.airtable_client)  # Assuming you can access Read like this.
            test_table_name = 'YourTestTableName'  # Replace with a table name for testing
            test_query = 'YourTestQuery'  # Replace with a query for testing
            
            # Act
            records = read_instance.search_records(test_table_name, test_query)
            
            # Assert
            self.assertIsInstance(records, list)  # Make sure it returns a list
            # Here you might add more specific tests depending on what kind of query you are running.
            
        except Exception as e:
            error_message, http_status = handle_error('TEST_READ_SEARCH_RECORDS_001')
            self.fail(f"{error_message} | HTTP Status: {http_status} | Exception: {str(e)}")


if __name__ == '__main__':
    unittest.main()