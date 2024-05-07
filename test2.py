import googleapiclient.discovery
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account
import os.path
from pathlib import Path
#import schedule
import time

import google.auth.exceptions
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# from datetime import datetime, timedelta
# import pytz

# # Define the time range (Korean Standard Time)
# start_time = datetime.strptime('03:06', '%H:%M').time()
# end_time = datetime.strptime('03:20', '%H:%M').time()

# API information
api_service_name = "youtube"
api_version = "v3"

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
CLIENT_SECRETS_FILE = 'client_secret2.json'


# API key

DEVELOPER_KEY = ""

with open(str(Path.home())+"/youtube/youtube_api_key", 'r') as file:
    DEVELOPER_KEY = file.readline()

creds = None
#credentials = service_account.Credentials.from_service_account_file(CLIENT_SECRETS_FILE, scopes=SCOPES)

if os.path.exists('token.json'):
    try:
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        creds.refresh(Request())
    except google.auth.exceptions.RefreshError as error:
        # if refresh token fails, reset creds to none.
        #creds = None
        print(f'An error occurred: {error}')
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('client_secret2.json', SCOPES)
        creds = flow.run_local_server(port=8086)
    with open('token.json', 'w') as token:
            token.write(creds.to_json())

# API client
#youtube = googleapiclient.discovery.build(
#    api_service_name, api_version, developerKey = DEVELOPER_KEY, credentials=credentials)
youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=creds)

# 'request' variable is the only thing you must change
# depending on the resource and method you need to use
# in your query
bokyem_id = "UCu9BCtGIEr73LXZsKmoujKw"
khan_id = "UCaMV-CjrWYh2Aefg_8iLwJQ"
phinguin_id = "UC07-J76O844ZdhyIRqK5IOQ"
bokemi_id = "UCCJ2b2lJE7M77cSuSHLcMOQ"
old_video_id = "A"
def first_comment(count):
    global old_video_id
    request = youtube.search().list(
        part = "id,snippet",
        channelId=bokyem_id,
        order="date",
        type="video"
    )
    # Query execution
    response = request.execute()
    latest_video_id = response['items'][0]['id']['videoId']
    # Print the results
    #print(response)
    #print()
    #print(latest_video_id)

    old_video_id = latest_video_id
    request = youtube.commentThreads().insert(
        part='snippet',
        body={
            'snippet': {
                'videoId': latest_video_id,
                'topLevelComment': {
                    'snippet': {
                        'textOriginal': str(count)
                    }
                }
            }
        }
    )
    response = request.execute()
    print(latest_video_id)
    print("Comment posted successfully.")
    
    
    
    
    
    request = youtube.search().list(
        part = "id,snippet",
        channelId=bokemi_id,
        order="date",
        type="video"
    )
    # Query execution
    response = request.execute()
    latest_video_id = response['items'][0]['id']['videoId']
    # Print the results
    #print(response)
    #print()
    #print(latest_video_id)

    old_video_id = latest_video_id
    request = youtube.commentThreads().insert(
        part='snippet',
        body={
            'snippet': {
                'videoId': latest_video_id,
                'topLevelComment': {
                    'snippet': {
                        'textOriginal': str(count)
                    }
                }
            }
        }
    )
    response = request.execute()
    print("Comment posted successfully.")

# def print_hello():
#     print("Hello")
    
# schedule.every(1).seconds.do(first_comment)

# while True:
    
#     current_time = datetime.now(pytz.timezone('Asia/Seoul')).time()
#     if start_time <= current_time <= end_time:
#         schedule.run_pending()
#     time.sleep(1)
    
