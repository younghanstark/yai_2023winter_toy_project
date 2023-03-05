# IMPORTANT! BE AWARE OF YOUR QUOTA LIMIT
# This Python code makes multiple 'search' requests.

import os
import csv
from googleapiclient.discovery import build
import urllib.request

PATH = './thumbnails/images'

categories = dict()
for root, dirs, files in os.walk(PATH):
    for dir in dirs:
        categories[dir] = len(os.listdir(os.path.join(root, dir)))
print(categories)

with open('key.txt', 'r') as f:
    apiKey = f.read()

youtube = build('youtube', 'v3', developerKey=apiKey)

f = open('metadata.csv', 'a', encoding='utf-8', newline='')
wr = csv.writer(f)

MINIMUM_NUMBER = 300
for key, value in categories.items():
    print(f'Working on category {key}')
    if value >= MINIMUM_NUMBER:
        continue
    
    nextPageToken = None
    while len(os.listdir('./thumbnails/images/' + key)) < MINIMUM_NUMBER:
        response = youtube.search().list(
            type='video',
            videoCategoryId=key,
            part='id',
            maxResults=50,
            pageToken=nextPageToken
        ).execute()
        videoIds = ','.join([item['id']['videoId'] for item in response['items']])
        if videoIds == '':  # In case of no response
            break
        try:
            nextPageToken = response['nextPageToken']
        except:
            break

        response = youtube.videos().list(
            part='snippet',
            id=videoIds
            ).execute()

        # Get category and thumbnail
        for video in response['items']:
            try:
                videoId = video['id']
                categoryId = video['snippet']['categoryId']

                if 'maxres' in video['snippet']['thumbnails']:
                    thumbnailUrl = video['snippet']['thumbnails']['maxres']['url']
                elif 'standard' in video['snippet']['thumbnails']:
                    thumbnailUrl = video['snippet']['thumbnails']['standard']['url']
                elif 'high' in video['snippet']['thumbnails']:
                    thumbnailUrl = video['snippet']['thumbnails']['high']['url']
                elif 'medium' in video['snippet']['thumbnails']:
                    thumbnailUrl = video['snippet']['thumbnails']['medium']['url']
                else:
                    thumbnailUrl = video['snippet']['thumbnails']['default']['url']
                urllib.request.urlretrieve(thumbnailUrl, f'./thumbnails/images/{str(categoryId)}/{str(videoId)}.jpg')

                wr.writerow([videoId, categoryId])
            except Exception as e:
                print(f'An error occured while getting video {videoId}\'s data.')
                print(e)
                continue
        
        if not nextPageToken:
            break

f.close()