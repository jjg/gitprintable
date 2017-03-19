#!/usr/bin/python

import json
import requests
from requests.auth import HTTPBasicAuth

#searchUrl = 'https://api.github.com/search/code'

# get auth from user
githubUser = raw_input('github username: ')
githubPassword = raw_input('github password: ')
searchTerm = raw_input('what to search for: ')

searchUrl = 'https://api.github.com/search/code?q=%s+in:path+extension:stl' % searchTerm

#searchParams = dict(
#    q='%s+in:path+extension:stl' % searchTerm 
#)

searchResponse = requests.get(url=searchUrl, auth=HTTPBasicAuth(githubUser, githubPassword))
searchData = json.loads(searchResponse.text)

print 'request status: %d' % searchResponse.status_code

if searchResponse.status_code > 199 and searchResponse.status_code < 300:
    # TODO: make sure results collection exists
    print '%d matching results' % searchData['total_count']
    for searchResult in searchData['items']:
        print searchResult['name']
        print searchResult['repository']['name']
        print searchResult['repository']['description']
        print searchResult['repository']['html_url']
        print ''
else:
    print '%d error while searching: %s' % (searchResponse.status_code, response.text)
