import os
import csv
import urllib.request
from googleapiclient.discovery import build
import time
import pickle

with open('key.txt', 'r') as f:
    apiKey = f.read()

youtube = build('youtube', 'v3', developerKey=apiKey)

PATH = './thumbnails/images/'
if not os.path.exists(PATH):
    os.makedirs(PATH)

response = youtube.videoCategories().list(
        part="snippet",
        regionCode="US"
    ).execute()

for item in response['items']:
    categoryPath = PATH + str(item['id'])
    if not os.path.exists(categoryPath):
        os.makedirs(categoryPath)

f = open('metadata.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(['Id', 'Category'])

if not os.path.exists('./channels.pickle'):
    channelSet = set()
    with open('channels.pickle', 'wb') as pkl:
        pickle.dump(channelSet, pkl)

with open('channels.pickle', 'rb') as pkl:
    channelSet = pickle.load(pkl)

usernameList = ['kurzgesagt', 'Munchies', 'TopGear', 'BuzzFeedVideo', 'videogamedunkey', 'tryguys', 'MrBeast', 'TheCoderCoder', 'gameranxTV', 'TheInfographicsShow', 'LEMMiNO', 'mythicalkitchen', 'AbroadinJapan', 'IHincognitoMode', 'TechLinked', 'TheStig', 'JCS', 'ThrottleHouse', 'epicurious', 'TeamCoco', 'TheWarOwl', 'chrisfix', 'mkbhd', 'DonutMedia', 'LevelCapGaming', 'OverSimplified', 'penguinz0', 'austinevans', 'BBCNews', 'FirstWeFeast', 'Vox', 'screenjunkies', 'nowthisnews', 'ParksandRecreation', 'KeyAndPeele', 'CNET', 'NileRed', 'DoctorWho', 'jomaoppa', 'InternetHistorian', 'NBCNews', 'SkyNews', 'HardwareCanucks', 'AboutToEat', 'CDawgVA', 'ElectroBOOM', 'Fireship', 'LGR', 'eater', 'JREClips', 'TheStraightPipes', 'thegrandtour', 'theFword', 'DramaAlert', '3blue1brown', 'pbsspacetime', 'BarelySociable', 'bonappetit', 'SomeGoodNews', 'SamONellaAcademy', 'markiplier', 'DrBecky', 'shroud', 'OfficialGrahamNorton', 'LetsGameItOut', 'drewisgooden', 'Vsauce', 'MarkRober', 'TheDailyShow', 'smartereveryday', 'sea_space', 'LexClips', 'LinusTechTips', 'JomainNYC', 'InsiderNews', 'Techquickie', 'Drivetribe', 'AETV', 'TheOffice', 'jacksepticeye', 'gordonramsay', 'hellskitchen', 'NBCBrooklyn99', 'CarThrottle', 'EpicNameBro', 'veritasium', 'WebDevSimplified', 'CaptainDisillusion', 'carwow', 'VICE']

MAX_RESULTS = 50  # Maximum number of videos from one channel. Acceptable values are 0 to 50, inclusive.

for username in usernameList:
    if username in channelSet:
        continue
    
    print(f'Processing {username}...')
    channelSet.add(username)

    try:
        # Get channel ID from channel name
        response = youtube.channels().list(
            part='id',
            forUsername=username
        ).execute()
        channelId = response['items'][0]['id']

        # Get comma-seperated list of video ids from that channel
        response = youtube.playlistItems().list(
            part='snippet',
            maxResults=MAX_RESULTS,
            playlistId=f'UU{channelId[2:]}'
        ).execute()
        videoIds = ','.join([item['snippet']['resourceId']['videoId'] for item in response['items']])

        # Get information of videos
        response = youtube.videos().list(
            part='snippet',
            id=videoIds
        ).execute()
    
    except:
        print(f'An error occured while getting {username}\'s channel data.')
        continue

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
        except:
            print(f'An error occured while getting video {videoId}\'s data.')
            continue
    
    time.sleep(0.1)  # To avoid queries per minute limit

f.close()

with open('channels.pickle', 'wb') as pkl:
    pickle.dump(channelSet, pkl)