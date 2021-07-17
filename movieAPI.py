import requests
import json


def get_recent_data():
    list_of_data = []
    url = "https://www.scorebat.com/video-api/v1/"
    response = requests.get(url)
    soccer_info = response.json()

    for i in range(5):
        # list_of_data.append(soccer_info[i]['competition'])
        print(soccer_info[i]['competition'])
    # return list_of_data
