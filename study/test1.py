import urllib.request
import urllib.parse
from html.parser import HTMLParser
import re
import json
import requests


class down_pic():
	def __init__(self,username):
		self.headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
		self.params = {'ie':'utf-8'}
		self.url = 'http://tieba.baidu.com/home/get/panel'
		self.imgurl_b = 'http://tb.himg.baidu.com/sys/portrait/item/'
		self.username = username

	def sub_name(self):
		self.username = set(self.username)
		self.username = list(self.username)
		return 0

	def get_img(self,name):
		self.params['un'] = name
		r = requests.get(self.url,params=self.params,headers=self.headers)
		imgurl_e = r.json()['data']['portrait']
		imgurl = self.imgurl_b+imgurl_e
		p = requests.get(imgurl,headers=self.headers)
		return p.content

	def save(self,name,content):
		ml = 'img/'+name+'.jpg'
		f = open(ml,'wb')
		f.write(content)
		f.close()

	def run(self):
		self.sub_name()
		for name in self.username:
			print(name)
			content = self.get_img(name)
			self.save(name,content)

if __name__ == '__main__':
	f = open('name.txt','r')
	name = f.readlines()
	name = [n.replace('\n','') for n in name]
	f.close()
	pic = down_pic(name)
	pic.run()




