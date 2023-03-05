from googleapiclient.discovery import build

with open('key.txt', 'r') as f:
    apiKey = f.read()

youtube = build('youtube', 'v3', developerKey=apiKey)

request = youtube.videoCategories().list(
        part="snippet",
        regionCode="US"
    )
response = request.execute()

for item in response['items']:
    print(item['id'], item['snippet']['title'])
print('Total', len(response['items']))
