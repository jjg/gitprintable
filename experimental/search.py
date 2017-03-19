#!/usr/bin/python

import json
import requests
from requests.auth import HTTPBasicAuth

searchUrl = 'https://api.github.com/search/code'

# get auth from user
githubUser = raw_input('github username: ')
githubPassword = raw_input('github password: ')
searchTerm = raw_input('what to search for: ')

searchParams = dict(
    q='%s+extension:stl' % searchTerm
)

searchResponse = requests.get(url=searchUrl, auth=HTTPBasicAuth(githubUser, githubPassword), params=searchParams)
searchData = json.loads(searchResponse.text)

if searchData['items']:
    for searchResult in searchData['items']:
        print searchResult['name']
        print searchResult['repository']['name']
        print searchResult['repository']['description']
        print searchResult['repository']['html_url']
        print ''
else:
    print searchData
