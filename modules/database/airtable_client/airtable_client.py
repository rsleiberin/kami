from pyairtable import Api
import inspect
import config
import logging
from utils import get_methods

api_key = config.AIRTABLE_PERSONAL_ACCESS_TOKEN

#initialize error logger
logging.basicConfig(filename='airtable_error.log', level=logging.ERROR)

# Create an instance of the Api class

#create dictionary of tables
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
    def __init__(self,api_key):
        """Initializes AirtableClient with API key."""
        self.api = Api(api_key)
        self.base_dictionary ={'Kami':config.AIRTABLE_BASE_ID}
        self.active_baseID = self.base_dictionary['Kami']
        self.table_dictionary = {}
    
    def get_methods(self):
        return get_methods(self)

    class Read:
        """Encapsulates read operations for AirtableClient. Provides methods to retrieve bases, tables, and records."""
        pass

        def get_methods(self):
            return get_methods(self)

        #retrieve table dictionary
        def get_tables(self):
            """Fetches all tables, updates self.table_dictionary, returns dict_keys of table names."""
            try:
                self.table_dictionary = static_table_dictionary
                return self.table_dictionary.keys()
            except Exception as e:
                logging.error(str(e))


        #retrieve records using table name
        def get_records(self, table_name):
            """Fetches all records from specified table_name, returns list of dictionary records."""
            try:
                # Access a table by name from the baseID and tableID
                table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
                # Use the table instance to get all records
                records= table.all()
                return records
            except Exception as e:
                logging.error(str(e))
 
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
            """
            Fetches a paginated set of records from a specified table.
            
            Args:
                table_name (str): The name of the table to fetch records from.
                page_size (int): The number of records to fetch per page.
                page_number (int): The page number to fetch.
                
            Returns:
                list: A list of dictionary records from the specified table, for the specified page number.
            """
            try:
                # Access a table by name from the active base ID and table dictionary
                table = self.api.table(self.active_baseID, self.table_dictionary.get(table_name))
                # Calculate the offset for the records to fetch
                offset = (page_number - 1) * page_size
                # Use the table instance to get a set of records, with the specified page size and offset
                records = table.all(max_records=page_size, offset=offset)
                return records
            except Exception as e:
                logging.error(f"Error in get_records_paginated: {str(e)}")
                return None
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

if __name__ == "__main__":
    instance = AirtableClient('1')
    print (instance.get_methods())
    print (instance.Read().get_methods())

'''
if __name__ == "__main__":
#Testing functions.
    # Create an instance of AirtableClient
    airtable_client = AirtableClient(api_key)

    # Call the get_bases method and print the result
    try:
        print(airtable_client.get_bases())
    except Exception as e:
        print("Get Bases Error")

    # Call the get_tables method and print the result
    try:
        print(airtable_client.get_tables())
    except Exception as e:
        print("Get Tables Error")

    # Call the get_records method for a specific table and print the result
    # Assume 'Roles' is a valid table name in your Airtable base
    try:
        print(airtable_client.get_records('Roles'))
    except Exception as e:
        print("Get Records Error")

#Test Results:

dict_keys(['Kami'])
dict_keys(['AgentMessages', 'Tables', 'Keywords', 'Roles', 'UserMessages', 'Sockets', 'Contexts', 'AuditLogs', 'Changes', 'Responses', 'ResponseKeywords', 'Models', 'AgentSockets', 'Agents', 'Sessions', 'Users'])
[{'id': 'recBmcZd4r3D1bFPr', 'createdTime': '2023-10-06T01:35:31.000Z', 'fields': {'RoleDescription': "The Assistant role represents messages that store previous assistant responses or can be used to provide examples of desired behavior. These messages help shape the conversation's context and guide the assistant's behavior.\n", 'RoleName': '"assistant"', 'Note': '"Assistant messages serve multiple purposes in a conversation. They can store previous responses for reference, showcase the assistant\'s capabilities, or demonstrate the desired behavior to the model. While not as common as System and User messages, they play a valuable role in shaping the interaction."\n', 'Models': ['recVVavZLrEBY4Yuh', 'rec2bcgGvrFuBwwlc', 'recq1CHxez5td41kY', 'recjOJxH6e1Iafqii', 'receqQIGClmc02RjU'], 'RoleID': 3}}, {'id': 'recGoWNTz1R312vfK', 'createdTime': '2023-10-06T01:33:21.000Z', 'fields': {'RoleDescription': "The System role represents messages that set the behavior and instructions for the assistant within a conversation. System messages help guide the assistant's responses and actions.\n", 'RoleName': '"system"', 'Note': ' "The System role is typically used at the beginning of a conversation to provide high-level instructions or to modify the personality and behavior of the assistant. It helps shape the context for the conversation and influences how the assistant responds to subsequent user messages. While optional, a well-crafted System message can significantly impact the conversation\'s outcome."\n', 'Models': ['recVVavZLrEBY4Yuh', 'rec2bcgGvrFuBwwlc', 'recq1CHxez5td41kY', 'recjOJxH6e1Iafqii', 'receqQIGClmc02RjU'], 'Sockets': ['recXkUNJHo3ELhsZv', 'recwMjhUYZvhsZtAF', 'receFtpM0OLlL5UGf', 'recvW56wZ7PAvW2Xk', 'recEgeEU130ZA8a5X', 'rech3iip1yynHKPH1', 'recQS2o2U3jiKWvl9'], 'RoleID': 1}}, {'id': 'recNPDi6R1ZKKNoEp', 'createdTime': '2023-10-06T01:35:22.000Z', 'fields': {'RoleDescription': 'The User role represents messages from the user, including requests, queries, or comments. User messages drive the conversation by providing input for the assistant to respond to.\n', 'RoleName': '"user"', 'Note': '"User messages are an essential part of the conversation as they define the user\'s intent and the tasks they want the assistant to perform. These messages typically come after the System message and provide context and instructions for the assistant to generate relevant responses."\n', 'Models': ['recVVavZLrEBY4Yuh', 'rec2bcgGvrFuBwwlc', 'recq1CHxez5td41kY', 'recjOJxH6e1Iafqii', 'receqQIGClmc02RjU'], 'RoleID': 2}}]
'''

'''

'''