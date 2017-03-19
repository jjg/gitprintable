#!/usr/bin/python

import json
import requests
from requests.auth import HTTPBasicAuth

searchUrl = 'https://api.github.com/search/code'

# get auth from user
githubUser = raw_input('github username: ')
githubPassword = raw_input('github password: ')

searchParams = dict(
    q='stl+in:extension'
)

searchResponse = requests.get(url=searchUrl, auth=HTTPBasicAuth(githubUser, githubPassword), params=searchParams)
searchData = json.loads(searchResponse.text)

for searchResult in searchData['items']:
    print searchResult['name']
    print searchResult['repository']['description']
