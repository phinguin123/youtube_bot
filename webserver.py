from flask import Flask, request, jsonify
import xmltodict
import sys
import logging
from test2 import first_comment


app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
count = 9
@app.route('/callback', methods=['POST','GET'])
def handle_notification():
    if request.method == 'POST':
        global count
        count += 1
        print("received POST request")
        data = xmltodict.parse(request.data)
        print(data)
        first_comment(count)
        return request.args.get('hub.challenge')
    else:
        print("hellO")
        print("value is : ",request.args.get('hub.challenge'), flush=True)
        app.logger.info('value')
        return request.args.get('hub.challenge')
        #notification_data = request.json
        # Process the notification data
        #video_id = notification_data['entry']['yt:videoId']
        #channel_id = notification_data['entry']['yt:channelId']
        #print(f"Received notification for video ID: {video_id} from channel ID: {channel_id}")
        # You can implement further processing here, like writing a comment or triggering other actions
        

@app.route('/')
def hello():
    return 'Hello'

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True, port=5001)

