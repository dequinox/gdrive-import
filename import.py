from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


# Setup the Drive v3 API
SCOPES = 'https://www.googleapis.com/auth/drive'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('drive', 'v3', http=creds.authorize(Http()))

# Call the Drive v3 API
hasNextPage = True
nextPageToken = ""

while hasNextPage:
    results = service.files().list(pageToken=nextPageToken, fields="nextPageToken, files(id, name, size, mimeType)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(item)
            file_id = item['id']
            filename = item['name']
            """
            if 'size' in item:
                request = service.files().get_media(fileId=file_id)
                fh = io.FileIO(filename, 'wb')
                downloader = MediaIoBaseDownload(fh, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    print ("Download %d%%." % int(status.progress() * 100))
                    """
    if 'nextPageToken' in results:
        hasNextPage = True
        nextPageToken = results['nextPageToken']
    else:
        hasNextPage = False
