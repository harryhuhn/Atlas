from __future__ import print_function
import pickle
import os.path
from datetime import time

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def mail():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    global msg
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is.unread").execute()
    messages = results.get('messages', [])
    message_count = int(input("How many messages do you want to see?"))

    if not messages:
        print('No messages found.')
    else:
        print('Messages:')
        for message in messages[:message_count]:
            msg = service.users().messages().get(userId='me', id=message['id'].execute())
            message_count = message_count + 1
        print("You have " + str(message_count) + " unread messages.")
        new_message_choice = input("Would you like to see your messages?").lower()
        if new_message_choice == "yes" or "y":
            email_data = msg['payload']['headers']
            for values in email_data:
                name = values["name"]
                if name == "From":
                    from_name = values["value"]
                    print("You have a new message from: " + from_name)
                    print("     " + msg['snipper'][:50] + "...")
                    print("\n")
        else:
            print("Good-bye")

if __name__ == '__mail__':
    mail()