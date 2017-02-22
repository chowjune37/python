class publish:
	def __init__(self):
		self.user = []
	def adduser(self,obj):
		self.user.append(obj)
	def updata(self,con):
		for i in self.user:
			i.talk(con);

class subscribe:
	def talk(self,con):
		print(con)

class expublish(publish):
	pass

class exsubscribe(subscribe):
	pass

if __name__ == '__main__':
	ep = expublish()
	es = exsubscribe()
	ep.adduser(es)
	ep.updata('hello word!!')
