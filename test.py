#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import sys
sys.path.append("..")
import tocken

gitee_api_url = "https://gitee.com/oauth/token"
api_repos = "http://gitee.com/api/v5/users/weixinwang/repos"
api_tocken_data = urllib.urlencode(tocken.gitee_api_tocken)
request = urllib2.Request(gitee_api_url,api_tocken_data)
response = urllib2.urlopen(request)
print response.read()

request = urllib2.Request(api_repos)
response = urllib2.urlopen(request)
print response.read()