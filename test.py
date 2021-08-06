from google.oauth2 import service_account
import googleapiclient.discovery
from apiclient.http import MediaFileUpload
import sys

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service-account.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = googleapiclient.discovery.build('drive', 'v3', credentials=credentials)

if len(sys.argv)<2:
    print("You must pass the Google Folder ID as argument to this program")
    sys.exit(1)
    
folder_id = sys.argv[1]

print(f"Creating file in folder with id {folder_id}")
file_metadata = {
    'name': 'testfile.csv',
    'parents': [folder_id]
}
media = MediaFileUpload('testfile.csv',
                        mimetype='application/csv',
                        resumable=True)
file = service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
print(f"Open file at https://drive.google.com/file/d/{file.get('id')}/view")
