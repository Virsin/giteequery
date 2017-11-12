#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import sys
import re
sys.path.append("..")
import tocken

def gitee_search():
	page = 1
	keyword = ["java","php","objective-c","go","android","javascript","c#","python","html","c++","c","swift","nodejs","ruby"]
	search_url = "%s%s%s" %("https://gitee.com/search?search=",keyword[0],"&type=project&language=&&condition=")
	print "generized esarch url:"
	print search_url
	print "/n"

	try:
		request = urllib2.Request(search_url)
		response = urllib2.urlopen(request)
		print "%s%d" %("Response with code: ",response.cods)
		return response
	except urllib2.URLError, e:
		if hasattr(e,"code"):
			print e.code
		if hasattr(e,"reason"):
			print e.reason



def gitee_APTinit():
	gitee_api_url = "https://gitee.com/oauth/token"
	print "%s%s" % ("start initalizing with url: ",gitee_api_url)
	api_tocken_data = urllib.urlencode(tocken.gitee_api_tocken)
	try:
		request = urllib2.Request(gitee_api_url, api_tocken_data)
		response = urllib2.urlopen(request)
		print "%s%d" %("Response with code: ",response.cods)
	except urllib2.URLError, e:
		if hasattr(e, "code"):
			print e.code
		if hasattr(e, "reason"):
			print e.reason
	print "%s%s" % ("Response content: ",response.read())

def gitee_searchDecode(response):
	content = response.read().decode('utf-8')
	p1 = r'(?<=<a href=").+?(?=" target="_blank"><strong>)'
	pattern = re.compile(p1)
	content_items = re.findall(pattern, content)
	if content_items:
		# for content_item in content_items:
		print content_items
	else:
		print 'no match found'
	return content_items