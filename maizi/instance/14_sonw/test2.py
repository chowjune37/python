if __name__ == '__main__':
	import tkinter
	root = tkinter.Tk()
	cvns = tkinter.Canvas(root,width=600,height=660,bg='white')
	pid1 = cvns.create_polygon(200,5,400,5,400,300,200,300,fill='white',outline='red')
	pid2 = cvns.create_polygon(10,10,100,10,100,100,10,100,fill='white',outline='red')
	pid3 = cvns.create_arc(10,10,100,50,start=0,extent=230)
	cvns.pack()
	print(pid1,pid2)
	root.mainloop()