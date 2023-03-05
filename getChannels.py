from googleapiclient.discovery import build

with open('key.txt', 'r') as f:
    apiKey = f.read()

youtube = build('youtube', 'v3', developerKey=apiKey)

channels = []
next_page_token = None
while True:
    request = youtube.search().list(
        part="snippet",
        maxResults=50,
        type="channel",
        regionCode="US",
        pageToken=next_page_token
    )
    response = request.execute()
    channels += [item['snippet']['customUrl'] for item in response['items']]
    next_page_token = response.get('nextPageToken')
    if not next_page_token:
        break

print(channels)