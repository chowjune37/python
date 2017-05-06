import urllib.request
import urllib.parse
import threading

gCondition = threading.Condition()

def a():
	global gCondition
	gCondition.acquire()
	print('hello')
	gCondition.wait()
	print('nihao')
	gCondition.release()

def b():
	global gCondition
	gCondition.acquire()
	print('yellow')
	gCondition.notify_all()
	gCondition.release()


if __name__ == '__main__':
		threading.Thread(target=a).start()
		print('jjjj')
		threading.Thread(target=b).start()
