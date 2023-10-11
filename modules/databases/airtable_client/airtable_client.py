import sys
sys.path.append('/home/tank/kami')

from pyairtable import Api
import config  # Since config.py is in the root directory, and the root directory is in the PYTHONPATH
import logging
from modules.utils.utils import get_methods  # Adjusted to the correct import path
from modules.databases.airtable_client.read_operations import Read


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
        self.table_dictionary = static_table_dictionary
        self.Read = self.initialize_read()
        
    
    def initialize_read(self):
        """Initializes and returns an instance of the Read class."""
        return Read(self)

    
    def get_methods(self):
        return get_methods(self)

if __name__ == "__main__":
    instance = AirtableClient(config.AIRTABLE_PERSONAL_ACCESS_TOKEN)
    
    # Test the Read methods:
    print("Testing get_tables method:")
    print(instance.Read.get_tables())




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