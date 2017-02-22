
# ball class
class ball:
	def __init__(self):
		self.num = None
		self.time = None

	def get_time(self):
		self.time = time.asctime(time.localtime(time.time()))

# red_ball class
class red_ball(ball):
	def __init__(self):
		self.num = [0] * 6

	def shake(self):
		for i in range(0,6):
			num = random.randint(1,33)
			self.num[i] = num

# blue_ball class
class blue_ball(ball):
	def shake(self):
		num = random.randint(1,16)
		self.num = num

# double_ball class
class double_ball(ball):
	def __init__(self):
		self.rb = red_ball()
		self.bb = blue_ball()

	# save number
	def save(self):
		f = open('ball_log.txt','a')
		f.write(self.num)
		f.close()

	def shake(self):
		self.rb.shake()
		self.bb.shake()
		self.get_time()
		self.num = 	'[(红球号码):(' + \
					str(self.rb.num[0]) + ',' + \
					str(self.rb.num[1]) + ',' + \
					str(self.rb.num[2]) + ',' + \
					str(self.rb.num[3]) + ',' + \
					str(self.rb.num[4]) + ',' + \
					str(self.rb.num[5]) + \
					');(篮球号码):(' + \
					str(self.bb.num) + \
					')];[(开奖时间):(' + \
					self.time + \
					')]\n'
		self.save()

# buy double ball
class buy_ball(ball):
	def __init__(self):
		self.red_test = [str(x) for x in range(1,34)]
		self.blue_test = [str(x) for x in range(1,17)]
		self.red_num = [0] * 6
		self.blue_num = 0
		self.customer_name = ''
		self.i = 0

	def test_num(self,num,color = 'red'):
		if color == 'red':
			color = self.red_test
		else:
			color = self.blue_test
		if num in color:
			return True
		else:
			return False

	def get_num(self):
		while self.i >= 0 and self.i <= 7:
			if self.i >=0 and self.i<=5:
				num = input('input red ball number, please! \n(the number must equal or less then 33 and equal or greater then 0!)\n')
				if self.test_num(num):
					self.red_num[self.i] = num
				else:
					print('input error')
					continue
				self.i += 1
			elif self.i == 6:
				num = input('input blue ball number, please! \n(the number must equal or less then 16 and equal or greater then 0!)\n')
				if self.test_num(num,'blue'):
					self.blue_num = num
				else:
					print('input error')
					continue
				self.i += 1
			elif self.i == 7:
				num = input('input your name,please!')
				self.customer_name = num
				self.i += 1
		self.i = 0
		self.save()

	def save(self):
		f=open('sell_log.txt','a')
		self.get_time()
		self.num = 	'[(彩票购买者):(' + \
					self.customer_name + \
					')];[(红球号码):(' + \
					self.red_num[0] + ',' + \
					self.red_num[1] + ',' + \
					self.red_num[2] + ',' + \
					self.red_num[3] + ',' + \
					self.red_num[4] + ',' + \
					self.red_num[5] + \
					');(蓝球号码):(' + \
					self.blue_num + \
					')];[(购买时间):(' + \
					self.time + \
					')]\n'
		f.write(self.num)
		f.close()

# open double ball
class search():
	def __init__(self):
		self.re_buy_ticket = None
		self.re_ok_ticket = None
		self.c_buy_ticket = None
		self.c_ok_ticket = None
		self.seek_ok_num = 0

	def read_file(self):
		f1 = open('ball_log.txt','r')
		f2 = open('sell_log.txt','r')
		self.c_buy_ticket = f2.read()
		self.c_ok_ticket = f1.read()
		f1.close()
		f2.close()

	# [(彩票购买者):(s)];[(红球号码):(2,3,4,5,4,3);(蓝球号码):(4)];[(购买时间):(Sun Feb 12 16:15:25 2017)]
	# \[\(彩票购买者\):\((.*?)\)\];\[\(红球号码\):\(([\d]{1,2}),([\d]{1,2}),([\d]{1,2}),([\d]{1,2}),([\d]{1,2}),([\d]{1,2})\);\(蓝球号码\):\(([\d]{1,2})\)\];\[\(购买时间\):\((Mon|Tue|Wed|Thu|Fri|Sat|Sun) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([\d]{1,2}) ([\d]{2}:[\d]{2}:[\d]{2}) (20[\d]{2})\)\]
	# [(红球号码):(17,3,23,15,17,9);(篮球号码):(14)];[(开奖时间):(Sun Feb 12 16:20:04 2017)]
	# \[\(红球号码\):\(([\d]{1,2}),([\d]{1,2}),([\d]{1,2}),([\d]{1,2}),([\d]{1,2}),([\d]{1,2})\);\(篮球号码\):\(([\d]{1,2})\)\];\[\(开奖时间\):\((Mon|Tue|Wed|Thu|Fri|Sat|Sun) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([\d]{1,2}) ([\d]{2}:[\d]{2}:[\d]{2}) (20[\d]{2})\)\]
	def re_file(self):
		re_buy = re.compile('\[\(彩票购买者\):\((.*?)\)\];\[\(红球号码\):\(([\d]{1,2}),([\d]{1,2}),([\d]{1,2}),([\d]{1,2}),([\d]{1,2}),([\d]{1,2})\);\(蓝球号码\):\(([\d]{1,2})\)\];\[\(购买时间\):\((Mon|Tue|Wed|Thu|Fri|Sat|Sun) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([\d]{1,2}) ([\d]{2}:[\d]{2}:[\d]{2}) (20[\d]{2})\)\]')
		re_ok = re.compile('\[\(红球号码\):\(([\d]{1,2}),([\d]{1,2}),([\d]{1,2}),([\d]{1,2}),([\d]{1,2}),([\d]{1,2})\);\(篮球号码\):\(([\d]{1,2})\)\];\[\(开奖时间\):\((Mon|Tue|Wed|Thu|Fri|Sat|Sun) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([\d]{1,2}) ([\d]{2}:[\d]{2}:[\d]{2}) (20[\d]{2})\)\]')
		self.re_buy_ticket = re_buy.findall(self.c_buy_ticket)
		self.re_ok_ticket = re_ok.findall(self.c_ok_ticket)

	def show(self):
		seek = 0
		for i in self.re_ok_ticket:
			print(seek)
			print(i)
			seek += 1

if __name__ == '__main__':
	import random
	import time
	import re
	sh = search()
	sh.read_file()
	sh.re_file()
	sh.show()
	# bb = buy_ball()
	# bb.get_num()
	# db = double_ball()
	# db.shake()