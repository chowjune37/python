import os
import urllib.request
import re
import pdb

class sphinx(object):
    def __init__(self):
        self.url = 'http://www.maiziedu.com/course/teachers/?page=%s'
        self.User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8'

    def get_page(self,pageIndex):
        headers = {'User-Agent':self.User_Agent}
        request = urllib.request.Request(url=self.url % str(pageIndex),headers = headers)
        response = urllib.request.urlopen(request)
        return response.read()

    def analysis(self,content):
        compile = re.compile('<a title="([\w]+?)" href="([\S]+?)"><img alt=".*?" src="(.*?)">[\s,\S]*?<span class="color99">简介：</span>(.*?)</p>')
        items = compile.findall(content.decode('utf8'))
        return items

    def save(self,items,path):
        for item in items: 
            if not os.path.exists(path):
                os.makedirs(path)
            filepath = path + '/' + item[0] + '.txt'
            f = open(filepath,'w')
            f.write(item[-1])
            f.close()

    def run(self):
        for i in range(1,28):
            html = self.get_page(i)
            items = self.analysis(html)
            self.save(items,'tinfo')

if __name__ == '__main__':
    sp = sphinx()
    sp.run()
