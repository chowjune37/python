class Shape:
	def __init__(self,cvns,points):
		self.cvns = cvns
		self.points = points
		self.pid = None
	def delete(self):
		if self.pid:
			self.cvns.delete(self.pid)

class HatTop(Shape):
	def draw(self):
		self.pid = self.cvns.create_oval(*self.points)

class HatBottom(Shape):
    def draw(self):
        self.pid = self.cvns.create_polygon(*self.points)

class Hat:
	def __init__(self,cvns,start_point,w,h):
		self.cvns = cvns
		self.start_point = start_point
		self.w = w
		self.h = h
		self.ht = HatTop(self.cvns,self.ht_cacu())
		self.hb = HatBottom(self.cvns,self.hb_cacu())
	def draw(self):
		self.ht.draw()
		self.hb.draw()
	def delete(self):
		self.ht.draw()
		self.hb.draw()
	def ht_cacu(self):
		r = self.h/3/2
		x1 = self.start_point[0]+self.w/2-r
		y1 = self.start_point[1]
		x2 = x1+2*r
		y2 = y1+2*r
		return x1,y1,x2,y2
	def hb_cacu(self):
		x1 = self.start_point[0] + self.w / 2
		y1 = self.start_point[1] + self.h / 3
		x2 = self.start_point[0] + self.w / 3
		y2 = self.start_point[1] + self.h
		x3 = self.start_point[0] + self.w / 3 * 2
		y3 = y2
		return x1,y1,x2,y2,x3,y3

class Snow:
	def __init__(self,cvns,points,w=150,h=450):
		self.cvns = cvns
		self.points = points
		self.w = w
		self.h = h
		self.hat = Hat(self.cvns,self.points,self.w,self.h/6)
	def draw(self):
		self.hat.draw()

if __name__ == '__main__':
	import tkinter
	root = tkinter.Tk()
	cvns = tkinter.Canvas(root,width=600,height=665,bg='white')
	cvns.pack()
	snow = Snow(cvns,(10,5),300,660)
	snow = snow.draw()
	root.mainloop()


	# 10 + (300 - 220) / 2 = 50
	# 110

	# 50+35 = 85
	# 110+66 = 176
	
	# 85+73=158
	# 176+66=242