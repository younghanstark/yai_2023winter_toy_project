# IMPORTANT! BE AWARE OF YOUR QUOTA LIMIT
# This Python code makes multiple 'search' requests.

import os
import csv
# from googleapiclient.discovery import build

PATH = './thumbnails/images'

categories = dict()
for root, dirs, files in os.walk(PATH):
    for dir in dirs:
        categories[dir] = len(os.listdir(os.path.join(root, dir)))
print(categories)

maxNumber = categories[max(categories, key=categories.get)]
for key, value in categories.items():
    categories[key] = maxNumber - value
    print(f'For {key}, need {categories[key]} more data.')

# youtube = build('youtube', 'v3', developerKey=apiKey)
