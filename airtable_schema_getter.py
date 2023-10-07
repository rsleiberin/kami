import requests
import json
import config

# Replace with your credentials
PERSONAL_ACCESS_TOKEN = config.AIRTABLE_PERSONAL_ACCESS_TOKEN
BASE_ID = config.AIRTABLE_BASE_ID

def get_base_schema():
    url = f"https://api.airtable.com/v0/meta/bases/{BASE_ID}/tables"
    headers = {
        "Authorization": f"Bearer {PERSONAL_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        base_schema = response.json()
        for table in base_schema['tables']:
            print(f"Table: {table['name']}")
            print(f"Fields: {', '.join([field['name'] for field in table['fields']])}")
            print()  # Print a blank line between tables
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    get_base_schema()
'''
Table: Tables
Fields: TableID, TableName, TableDescription, Notes, Timestamp, Update Timestamp, Changes, AssociatedTables, TableName (from AssociatedTables), AuditLogs

Table: AuditLogs
Fields: AuditLogID, Timestamp, LogType, LogMessage, AssociatedTable, RecordID

Table: Changes
Fields: ChangeID, Timestamp, TableID, TableName (from TableID), RecordID, Field, OldValue, NewValue

Table: Contexts
Fields: ContextID, Timestamp, SummaryText, KeywordIndex, LastUserMessageID, AgentMessages, Responses

Table: Keywords
Fields: KeywordID, Timestamp, Keyword, ContextID, SummaryText (from ContextID), Responses

Table: Responses
Fields: ResponsesID, ResponseText, ContextID, Timestamp, ResponseKeywordsID, ResponseKeywords

Table: ResponseKeywords
Fields: ResponseKeywordID, Keyword, ResponseID

Table: Sessions
Fields: SessionID, UserID, StartTimestamp, EndTimestamp, age, UserMessages

Table: Agents
Fields: AgentID, AgentName, AgentDocumentation, AgentContextID, ModelID

Table: Models
Fields: ModelID, ModelName, TokenLimit, InputCost, OutputCost, ModelDescription, TrainingDate, Note, RoleID, RoleName (from RoleID), Agents

Table: Roles
Fields: RoleID, RoleName, RoleDescription, Note, AgentContexts, Sockets, Models

Table: Sockets
Fields: SocketID, Dependencies, Required, SocketName, SocketSize, SocketContext, SocketDescription, AgentContexts, RoleID, RoleName

Table: AgentMessages
Fields: AgentMessageID, UserMessageID, MessageText, Timestamp, ContextID, Sessions

Table: AgentContexts
Fields: AgentContextID, RoleID, RoleName, SocketID, SocketName (from SocketID), Agents

Table: Users
Fields: UserID, UserMessages, Sessions, UserName, UserEmail

Table: UserMessages
Fields: UserMessageID, ContextID, UserID, MessageText, Timestamp, AgentMessages, Sessions
'''