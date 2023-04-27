import requests
import sys
import json


def __startService():
    userInput = input("Type something! \n")
    url = 'https://seoul.synctreengine.com/plan/entrance'
    headers = {
        'X-Synctree-Plan-ID': 'a559bbbcf324578a7fd89f2b177159cba3e86a03ddb8ca0d65a3ca12e5b84b75',
        'X-Synctree-Plan-Environment': 'dev',
        'X-Synctree-Bizunit-Version': '1.0',
        'Content-Type': 'application/json',
        'X-Synctree-Revision-ID': 'bb8f89e5e44596bc22e18cb5c666f0b36556b4df8a11c25adee12548f08b9ee9'
    }
    params = {
        'content': userInput
    }
    synctreeResponse = requests.post(url, params=params, headers=headers)
    data = json.loads(synctreeResponse.text)
    print(data.get('result'))


__startService()
