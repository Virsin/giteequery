#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import sys
import re
import csv
sys.path.append("..")
import tocken



keywords = ["java","php","objective-c","go","android","javascript","c#","python","html","c++","c","swift","nodejs","ruby"]

for keyword in keywords:
	page = 1
	search_url = "%s%s%s" % ("https://gitee.com/search?search=", keyword, "&type=project&language=&&condition=")
	print "%s%s" % ("generized esarch url: ", search_url)

	try:
		request = urllib2.Request(search_url)
		response = urllib2.urlopen(request)
		print response.code
		#print (' the name of class is : ',dir(response))
		content = response.read().decode('utf-8')
		#print content
		#pattern = re.compile('<a href=.*? target="_blank"><strong>')
		p1 = r'(?<=<a href=").+?(?=" target="_blank"><strong>)'
		pattern = re.compile(p1)
		content_items = re.findall(pattern,content)
		if content_items:
			#for content_item in content_items:
			print content_items
		else:
			print 'no'



	except urllib2.URLError, e:
		if hasattr(e,"code"):
			print e.code
		if hasattr(e,"reason"):
			print e.reason

	print("break! \n\n\n\n")


	with open('test.csv','a') as myFile:
		my_writer = csv.writer(myFile)
		my_writer.writerow([keyword,content_items])

'''
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