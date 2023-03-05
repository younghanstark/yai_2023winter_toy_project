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

f = open('metadata.csv', 'a', encoding='utf-8', newline='')
wr = csv.writer(f)
if os.path.getsize('metadata.csv') == 0:
    wr.writerow(['Id', 'Category'])

if not os.path.exists('./channels.pickle'):
    channelSet = set()
    with open('channels.pickle', 'wb') as pkl:
        pickle.dump(channelSet, pkl)

with open('channels.pickle', 'rb') as pkl:
    channelSet = pickle.load(pkl)

channelIdList = ['UCW0xFzzIwbNQF9IO45WsqxQ', 'UCZx5TzdG3RC4CMNmxJLgfRw', 'UCB82v6uKp1S-I-DVoL2neDA', 'UCHzoeK57op5kRPY7baseKaQ', 'UCklPzWxEB9_jwrJfffvE1QA', 'UCoCSjc-4JCGqOxuhuw-xjSw', 'UCMewbKz8Q9q5hBbhUHguQGQ', 'UCa6b2GN21gMAVtWbS_wrabw', 'UCNySoZ-ZZIoOabLhqIAlDgA', 'UCiN7OwV8g8dMm_E0xphBVig', 'UCW9_z4xQB1dsz6Tm1hahM-Q', 'UCkqaNJOo0l3DMNiwYfEWViQ', 'UCRYJW3Ao5AOmeowheBEyKFQ', 'UC3eSeh7pFRRmVpfAQLolI-g', 'UCJNBZaQWMIHACqvHT_k2cWw', 'UCYM3pKj9tFQOXc2XcJmj8Vg', 'UCCb3DX0GO9f0EFizD5PT7bQ', 'UCcQNXHtBJmSpFhzBI6qfHRQ', 'UCtW5GPO_DZon6zVAuinvwxA', 'UCcdflab8cYknZ44-Ull5eXg', 'UC8ilKvUpaeizs_af0Q4vE6A', 'UC9w8tWMwtNxtF90EqmaymKw', 'UCzYN2asPfLSdbLbVCWXQzXA', 'UCjxJOLUPQvco4yhW26jY3dA', 'UC74bcC7aGRNz4KoRpJsJNEw', 'UC6wAZPPq8vCZjd9wzIjBqAQ', 'UCrFslqncMIdjD2WfB6pAcEg', 'UCyu8StPfZWapR6rfW_JgqcA', 'UCAg7hn6JVjO7MqpGpMg35qA', 'UCwk8QTieBA0_f3f_o6D969w', 'UCOWUNZA1AijnF_uTcEt1GVA', 'UCEbRSmzD8xASRlYq2OLmCrg', 'UCXw5vClfMWccw-OocfhQHiA', 'UCbIm2iqwql8bFqkO2bHv7Mw', 'UCF1zcCahFxWMbY_KULVFffg', 'UCPoCHHnaswi9xdXl-JQuD9Q', 'UC8UjlImzgVo1o6ziWxAre3Q', 'UCl2yqeDZUM1f8_sC_aEPYKw', 'UCW5g4EWONTc1gtqN1K9hU4w', 'UC_VtrptObkqqp9tp3jycINA', 'UCMtkk8LXf0wQ3VFAzoyN_og', 'UCAJnyTWJPpKXuwgWQDdNWrQ', 'UCbCmjCuTUZos6Inko4u57UQ', 'UCw7SNYrYei7F5ttQO3o-rpA', 'UCstEtN0pgOmCf02EdXsGChw', 'UC4PziMH5MvvsmqM0VCZTy-g', 'UCpDJl2EmP7Oh90Vylx0dZtA', 'UCPde4guD9yFBRzkxk2PatoA', 'UCN_u5w69V9wUZYG8WeJWuNg', 'UCP-Ng5SXUEt0VE-TXqRdL6g', 'UCGKQ4Tw5nPXMGsoYZHrHYeA', 'UCrreHSUa5rnuCVDeO8dX4eA', 'UCzkA5UTtr_vNYqMSB3DisVA', 'UCoookXUzPciGrEZEXmh4Jjg', 'UCqyCa01IgozJnJG3gAQaNdA', 'UCMoWQ_lvBWARyM7r1B3ZIIg', 'UC1FbPiXx59_ltnFVx7IxWow', 'UCTdRly9T3iyCJFjmRoCaepQ', 'UCrSx8rek9EuC3YGHvG8aalw', 'UCNcdbMyA59zE-Vk668bKWOg', 'UCHr2zD4qgWz8yXkzIun5aAg', 'UCTsgmnXbWotzbR36vU0YPrA', 'UCktaw9L-f65LzUUdjmCFkbQ', 'UCDCcr_N3OsqbH7FItELttvw', 'UC2Qc2XiBaYO2WI8pJpT0R0A', 'UCSPEjw8F2nQDtmUKPFNF7_A', 'UCvJJ_dzjViJCoLf5uKUTwoA', 'UCgOObQ-WkK2EA4CwXWspHGQ', 'UCuEgo07zsZr_FTcNTETRS5Q', 'UCrNnk0wFBnCS1awGjq_ijGQ', 'UCTvwy1xiI671wnyIwowM6mQ', 'UCUZzyuAlhHNP3oiuMjn7RfQ', 'UCTJDdO9klWGpTekswnXreGQ', 'UC74icFVsxTFr2BW3Vm8n_iw', 'UCGWkDcYbDKP9r--ym28YwAQ', 'UCVgO39Bk5sMo66-6o6Spn6Q', 'UCYDyGdodMhIuJ7WGmn0Bn3w', 'UCjZo1E1P6wDDyw6ImVgKM-A', 'UCMryAHWeLf3TxDyDxSWs4AQ', 'UCEduOt4TK8TtOaznB45TrhA', 'UCm4fSpMpPIZ9z6KHoezLUAg', 'UC73OSCbHaqKlhHLBpQqHPrQ', 'UCz6E3lF72mb6uoJ-mOlNo2A', 'UCKAqou7V9FAWXpZd9xtOg3Q', 'UC_jCXm9x_z9_kp8DNbIs6mQ', 'UCaEb7kPgpldLuEzCRzFXsLw', 'UCnEHS4Wa8WOxvQiKX4Vd-5g', 'UCSrZ3UV4jOidv8ppoVuvW9Q', 'UCDPk9MG2RexnOMGTD-YnSnA', 'UCx68_7D0FoZSu_u0z7Qc8sQ', 'UCmdI-Y9DGqIUzVXGZ-o1pOQ', 'UC1SxL7fbGVpyYk9V3H80ohw', 'UCzpcaCa-_9kwpk992S3Oi6w', 'UC0_1eG1YZQnuXc80zELWm_A', 'UCh6Havzyujxt0aqMw4tnXKw', 'UCcLzwVXQXSFlWYzhnYTaWqw', 'UCMPKq9xxIiAtfkOFW8gYwNw', 'UCjatLUib6wL9jUgUJ0eO2rw', 'UCtTQioTbrlagbJo97GqgXnw', 'UC_zcneV4GM5U7A_Zg5OdnKA', 'UC_zcneV4GM5U7A_Zg5OdnKA', 'UC5wfH9mjwSZXYA2P3d19BLQ', 'UCgGGVCU3lOdjwYwjw690UNw', 'UCYQSO4RKw1Qz0ZH-wFQworg', 'UCvH_WwHyNFhKewCCmyPiPqg', 'UCRfFsj9UbiR08u73WDxpQmg', 'UCplHwmU6xOYnNE7dfeFC5vQ', 'UCDo15DP4b-iQ8gRKqE7aPmA', 'UCqD-S85CMb8nnJPpHw84Y5w', 'UC5LHlJqzRHjkzsbVW2Q7Hag', 'UCsbrvEICOj3VMPeZK5qW0_g', 'UCsjQpXiwn1dkEvQ1ZEbg3Zg', 'UCChZtHuTkNJoKFnTYQfbHYA', 'UCXzM5FNOpzsf1HInajXqX5g', 'UCQINkxLSenu7XkAiAzgxTpQ', 'UCfRvBsR--lRXF1lMhzVUEBQ', 'UCxYA3UskRtQ0HutzaokbuBg', 'UCkz7cBzqIyQCdqNrG0i9ODQ', 'UCNYNK9gZ4-VLyx5Q1t3ZmsQ', 'UCvlhtitmaeumJaojxj4kc7A', 'UChKJmZprFDKkFY302eenxUQ', 'UC9E9-v2AbUiDxUl5j8Ok7eA', 'UCyLXWRcLVkKVuXEKTBDGncw', 'UCQPcrF2bFpdu97QPQdvcQUQ', 'UCjWB_yYtRNNl0r3dD8zLPDQ', 'UCO-nTTKH0Emyv3HoZU3yvsg', 'UCSOvHt7B5fEDvHE2vkb3-NA', 'UC2u0w6kUCeQiiIWjjyCn28A', 'UCpEia7rHs-3rI5vi4YuPLrw', 'UCmZ85_OF94lq1QDwqApTSeA', 'UCLuAw9xDzAf1tUV4lJCQpyQ', 'UCGWZA9yuyBL-Iake1Mi8wZQ', 'UC_ToLq5eEpIprjcQGryA7kw', 'UCvHo7cPNh_UUKY_rlkbz6Ng', 'UCV9JIB1WE458Zzy85QL7wMw', 'UCnljmFPdwWCbzAHMk7NxrXg', 'UCQsQArpn09R0RVMk2r4d42w', 'UCviwv9deqq5X9x6XIeaElVw', 'UCiUH62-aPb_xLWiE3C-wnyg', 'UCrpp4ph8eoWHZEpGJdTLlDw', 'UCdTq0_-6oMitcAKL4h5kynw', 'UCe7-bQeCilyCi_V7206nbyw', 'UCowTydVVibgi3C4Z1xKRAgw', 'UCKVGKReDpbvV4K_cRcMr6rA', 'UCVXTtHU1JVwGo32JQCzpbFQ', 'UCuCDZdiCBy2sCQ_BeBtXFqA', 'UCWy___cfcE2vEVWBsL5emtw', 'UCi2E9Lx7K48d0DXUuUev5lw', 'UC0omDgKaBwQKsfG0NAlrg4A', 'UCu_s2DDmsBQyotH5Ol_X2rw', 'UCei6M4-6qPRYgr-50tSQ56A', 'UCdd7Z5kzG87ItgDyK--r1aw', 'UC60WZ7Feo_xf9vwfM-9FKPQ', 'UCvgmHas1KyzVDW_aw3izeNw', 'UC3FCEDxyF8ECLdD2lIKb6kQ', 'UCjNfvxxSs1wnMEfQLhgkpnQ', 'UCuUjdn7KbMzJp-kUmxrqBEg', 'UCw6GP2XCdTOky6iJLmjoXig', 'UCrV-wFXsit9TNq1H7Yaqiyw', 'UCMMUW03VcuDBeytsgegdKzw', 'UCeR1QtsA0sFiD30zd2_oaBw', 'UChti-hhFOtxDurGiGnz_FmA', 'UCVZ9bGLt44A4BxzQwpcu3hg', 'UCFHCZFkzfdKVzfFv52ksQxw', 'UCNzR01e7DYJanViFQ3AXdeQ', 'UC2GM6luYGrT-SB3ly28dE9g', 'UCFOhfQ_qoIzyar_Nh5M3_Yw', 'UCJF7JjWbP9pelo5asBhnrNg', 'UCPXwXhW1-_DTRabFIXTzO6Q', 'UCbSLoWzV67SKi50sB4m3hfQ', 'UCxC9wIfBkg2f7vHGji9XW-g', 'UCUvTLgLxPVUbl_KIaAS_0BA', 'UCnI56mliiS07puGmEp1ATjw', 'UCTS0mfnsimKs_RWwdUodcIg', 'UCBIjU6S4pJA1fqqTSiYieSA', 'UCGexsAdaTlu2pOkWb3owKGw', 'UC4dY8BPK5jTFVE0e1Zc5LLg', 'UCRu2bWjnKtd9HI9GykgwF9w', 'UC8umM3WhFLMJdrDvVdF9JWQ', 'UCDbb7ZpJRkV4tCXsVLIhWlg', 'UCMT7PWwq3hYT7ZkaDrJG1zQ', 'UC2LC8xI1zRwoXRHn9w1SA0A', 'UCqF4v5xIfauOWCmyvECFFig', 'UCfnERisyXEw8ejyf1tP8KnA', 'UCF_4au-QtBrvj9DW0Dqk65A', 'UCOGL0wBqhSiB6zz7TWM5XnA', 'UC9S6jopBdxAxDvcIdj5eQMA', 'UCB5ars7mesCh_g3aHzFhmtg', 'UCPccDWjc5Ln4Rs_yl00RazA', 'UCpqyIPSydTHsV-kjs0h1aFg', 'UCi6C9GPwdyVf0ZBSZ58R2Ww', 'UChq8Lbe7o25qXX2zT_F7J8g', 'UCMqQJHgNoQhr6dOaSwlgCUg', 'UCjO4L3_76SRnTT753gGKvLA', 'UCsL1LV2lsxtRJCisdA_PPtQ', 'UCj45ExEtILYvUE01UB2ABIA', 'UCZ3wAZeHsiSlUptT9RGw5vA', 'UC8jJTPNeoQt_DIBgXyWrJXA', 'UC0HL4Kn6m0Ce_W8Uq3O-ytA', 'UCtURnkojSJA3mTBMGCJn0EA', 'UC0HL4Kn6m0Ce_W8Uq3O-ytA', 'UCtURnkojSJA3mTBMGCJn0EA', 'UCl7DMn1NI9IIHWKCzJmKMcA', 'UCwULBD5pq48zIynGl1XI3nA', 'UCDHRaE2ZE6jxa7RDMzzWwbA', 'UCPr-hyvrCZ1mfUKtxJWDDkQ', 'UCuAARdxNqR6uoBFzuA3ilvQ', 'UCbouGrDFjgvBEzubuMbi7Mg', 'UCAAZWzi_Aa-gCXMpUgRR8cQ', 'UCYlLWWUMEBJqraEJYAYlVEQ', 'UCtwXVSyNXe7y7ySuJTyymlg', 'UCotZJBwWGonskcKLUNV0Orw', 'UC8n3ogDFzrodQFUWfi8xrwA', 'UCOj-o3GHz6wfsnMqBcQwSGA', 'UCPs38bNA2XEHb8HbVSJAhyQ', 'UCsPz2W0sBWQAIPGYKfXGJMA', 'UCmnkcsoTcx9_YmA0fu8X5HQ', 'UCWX8-uIMjTwRmC0qTW105dA', 'UC7fhSf4E0cYps-bkL36wwZA', 'UC1CoCaFGb3nejAXQD-ozuMg', 'UCOchsP2BeVSVV5tc2pE7fPg', 'UCd2uHCRu4CbKvPoSKE0Iy2A', 'UC72rTLy4X-WQGKWjAWIyx2Q', 'UCTXwB8T-cxHXh5LGIZuRu0A', 'UC6ZIUWMbLS06Gxmeib8qI1A', 'UCTmmeRsZJ1X7cL4jSg7OEaA', 'UC3obHDsfcHdVvQp5kk6U7Hg', 'UCyHa8v8idQLDYqWqr4UGTQQ', 'UCIOB1W2mZE-UYV3ioCh5INA', 'UCCllzafDLkSW5BjAbJ1mYIw', 'UC4AZrNpbzFa0OCaQPYraDIQ', 'UCdq7e7OwwbhaskMA0UvhW1Q', 'UCyv71SbSGQDYakrpCmHH83w', 'UCqqTF1VH8VrRFXNA0Rx_9ug', 'UCYAmgJTLt-iCk_294JkYzLw', 'UCq30fCYYdTnY_r8cXoDjbAA', 'UCMR_Xv0smgZ7mpftlhTe3Lw', 'UCUWHgABvpltHbwmiR9j39iw', 'UCZDObIq94ZWZ6wzaEFnjyWA', 'UCWcolEAEpvWm9FMR9UoDYOg', 'UCIOgAXet3-xwrHAI7-9x4eA', 'UCpi0QaXMVoKqvUYhEPM9vTg', 'UCAUXhGH405xSFp7dtnF6SZw', 'UCO1ZS_M7POaPrTYb7IWb_ow', 'UC29SP985-pvApzDLIl60xRw', 'UCkvYzbmM2WQAJNWQhASXuBg', 'UCgOVgHl-0wW54b5O4mtQ32g', 'UClV-5Sw-YBu1tEcbysTMVFA', 'UCxwdKovisd8NB80oDAMtPRA', 'UCAPSLUJnptiMOtEGn__ZONg', 'UCjO4L3_76SRnTT753gGKvLA', 'UCsL1LV2lsxtRJCisdA_PPtQ', 'UCj45ExEtILYvUE01UB2ABIA', 'UCZ3wAZeHsiSlUptT9RGw5vA', 'UC8jJTPNeoQt_DIBgXyWrJXA', 'UC0HL4Kn6m0Ce_W8Uq3O-ytA', 'UCtURnkojSJA3mTBMGCJn0EA', 'UCl7DMn1NI9IIHWKCzJmKMcA', 'UCwULBD5pq48zIynGl1XI3nA', 'UCDHRaE2ZE6jxa7RDMzzWwbA', 'UCPr-hyvrCZ1mfUKtxJWDDkQ', 'UCuAARdxNqR6uoBFzuA3ilvQ', 'UCbouGrDFjgvBEzubuMbi7Mg', 'UCAAZWzi_Aa-gCXMpUgRR8cQ', 'UCYlLWWUMEBJqraEJYAYlVEQ', 'UCtwXVSyNXe7y7ySuJTyymlg', 'UCotZJBwWGonskcKLUNV0Orw', 'UC8n3ogDFzrodQFUWfi8xrwA', 'UCOj-o3GHz6wfsnMqBcQwSGA', 'UCPs38bNA2XEHb8HbVSJAhyQ', 'UCsPz2W0sBWQAIPGYKfXGJMA', 'UCmnkcsoTcx9_YmA0fu8X5HQ', 'UCWX8-uIMjTwRmC0qTW105dA', 'UC7fhSf4E0cYps-bkL36wwZA', 'UC1CoCaFGb3nejAXQD-ozog_C2CbImwCUW4QgFWKQ', 'UC6ZIUWMbLS06Gxmeib8qI1A', 'UCTmmeRsZJ1X7cL4jSg7OEaA', 'UC3obHDsfcHdVvQp5kk6U7Hg', 'UCzEItDHpiPpJHPg3UFtJVyA', 'UC7PtENVk6IPbY8PG5F9T9NA', 'UCIOB1W2mZE-UYV3ioCh5INA', 'UC7rz3Mdl6sFDiO9EShUIxOw', 'UCYFEwa2CrQPin5-6S-26qPA', 'UCJwY5KsMwvxbVFlidRLmtoA', 'UCmhMuaDxPPhHAu1WBryjtNA', 'UC4AZrNpbzFa0OCaQPYraDIQ', 'UCdq7e7OwwbhaskMA0UvhW1Q', 'UC620CT11fFkjeR3nnE0JpGQ', 'UCEjdBEauUzXh_ogtbSMfWww', 'UCD4pC9fS2cRUWTBqXIUc8mg', 'UCjUKtqslF6nK6aknZTzrV7w', 'UCKa-Tm7bQv0l7twko_k8Waw', 'UCLrGUP0v-6GTczsqeLzZteg', 'UCyv71SbSGQDYakrpCmHH83w', 'UCygNf21KaabKQ64sFojFdSA', 'UCqqTF1VH8VrRFXNA0Rx_9ug', 'UCjYOX-cepRzO6F-KH0jv0OA', 'UCAhyzZsr9UIFPywNP2e9eLA', 'UCHcGsAX92gkCRYyDOqSX9Kw', 'UCxEx_SfUpCCckKaF3ppw-uQ', 'UCw_4Xlu171PrI_Il16DlWIw', 'UC-fsbipUSQmmCgDLqEP3XiQ', 'UC0ywAu_AVkc-6qnKDnyLzcw', 'UCSi0I85zHBOBSjoYBb2chbA', 'UC79Z45NvcxTZzOGinFNCehQ', 'UCXRmfXgUxAXYQzNOVU01KrQ', 'UCvlX6msk8zIUveYNUNk2_iQ']

MAX_RESULTS = 50  # Maximum number of videos from one channel. Acceptable values are 0 to 50, inclusive.

for channelId in channelIdList:
    print(f'Processing {channelId}...')

    if channelId in channelSet:
        continue
    channelSet.add(channelId)

    try:
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
        print(f'An error occured while getting {channelId}\'s channel data.')
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