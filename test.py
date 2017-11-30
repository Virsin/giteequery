#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import gitee_webAPI
import sys
import re
import csv
sys.path.append("..")
import tocken



keywords = ["java","php","objective-c","go","android","javascript","c#","python","html","c++","c","swift","nodejs","ruby"]
url_prefix = "https://gitee.com/search?utf8=%E2%9C%93&search="
gitee_webAPI.get_repo_info(keywords,url_prefix)

'''
https://gitee.com/search?utf8=%E2%9C%93&search=java&group_id=&project_id=&type=

key = r"<html><body><h1>hello world</h1></body></html>"
p1 = r"(?<=<h1>).+?(?=</h1>)"  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
matcher1 = re.findall(pattern1, key)  # 在源文本中搜索符合正则表达式的部分
print matcher1  # 打印出来
'''


'''
gitee_api_url = "https://gitee.com/oauth/token"
api_repos = "http://gitee.com/api/v5/users/weixinwang/repos"
api_tocken_data = urllib.urlencode(tocken.gitee_api_tocken)
request = urllib2.Request(gitee_api_url,api_tocken_data)
response = urllib2.urlopen(request)
print response.read()

request = urllib2.Request(api_repos)
response = urllib2.urlopen(request)
print response.read()
'''