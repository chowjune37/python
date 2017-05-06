import requests
import re

class down_username():
	def __init__(self,baseurl):
		self.usernamelist = []
		self.nextpage = [baseurl]

	def next_page(self,content):
		patt = '<a href="(.*?)" class="next pagination-item " >'
		self.nextpage = re.findall(patt,content)		

	def get_page(self,url):
		headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
		r = requests.get(url,headers=headers)
		return r.text

	def get_username(self,content):
		patt = 'class="frs-author-name j_user_card " href=".*?" target="_blank">(.*?)</a>'
		name = re.findall(patt,content)
		self.usernamelist.extend(name)

	def run(self):
		while (self.nextpage):
			print(self.nextpage)
			content = self.get_page(self.nextpage[0])
			self.next_page(content)
			self.get_username(content)
		return 0

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
			content = self.get_img(name)
			self.save(name,content)

if __name__ == '__main__':
	getname = down_username('http://tieba.baidu.com/f?kw=python&amp;ie=utf-8')
	getname.run()
	


# http://tb.himg.baidu.com/sys/portrait/item/2383e6b389e883a1e5ae810e75

# new_iconinfo.   portrait.  http://tb.himg.baidu.com/sys/portrait/item/
# portrait

# http://tb.himg.baidu.com/sys/portrait/item/5967e5ada6e4b88de5a5bde6808ee4b988e58a9e5f7a?t=1464053430

# http://tieba.baidu.com/f?kw=python&ie=utf-8

# params = {'ie':'utf-8',
# 		'un':'学不好怎么办'}