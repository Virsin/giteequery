#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import re
import csv
import tocken

def search_basic(keyword,search_url,page):

	search_url_generated = "%s%s%s%s" % (search_url, keyword, "&page=", str(page))
	#search_url_generated = 'https://gitee.com/search?utf8=%E2%9C%93&search=java&group_id=&project_id=&type='
	print "%s%s" % ("generized esarch url: ", search_url_generated)
	try:
		request = urllib2.Request(search_url_generated)
		response = urllib2.urlopen(request)
		print response.code
		print 'page: '+ str(page)
		content = response.read().decode('utf-8')
		#print content
		p1 = r'(?<=<a href=").+?(?=" target="_blank"><strong>)'
		pattern = re.compile(p1)
		content_items = re.findall(pattern, content)
		if content_items:
			print content_items
			return content_items
		else:
			print 'no'
	except urllib2.URLError, e:
		if hasattr(e, "code"):
			print e.code
		if hasattr(e, "reason"):
			print e.reason
	finally:
		pass


def get_repo_info(keywords,search_url,page=0,file_name='test.csv'):

	search_max_page = 10
	if(page != 0):
		search_max_page = page

	with open(file_name, 'a') as myFile:
		my_writer = csv.writer(myFile)
		for keyword in keywords:
			my_writer.writerow([keyword])
			for search_page in range(1,search_max_page,1):
				search_result = search_basic(keyword,search_url,search_page)
				for result_content in search_result:
					my_writer.writerow([result_content])






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