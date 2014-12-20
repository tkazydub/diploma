# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# import Tkinter
from Tkinter import *
from mongodb import MongoDB




# def whichSelected () :
# 	return int(select.curselection()[0])

# def addEntry () :
# 	phonelist.append ([nameVar.get(), phoneVar.get()])
# 	setSelect ()

# def updateEntry() :
# 	phonelist[whichSelected()] = [nameVar.get(), phoneVar.get()]
# 	setSelect ()

# def deleteEntry() :
# 	del phonelist[whichSelected()]
# 	setSelect ()

def loadEntry  (e) :
	position = int(select.curselection()[0])
	pub_time.set(new_res[position]['pubdate'].encode('utf8'))
	art_title.set(new_res[position]['title'].encode('utf8'))
	art_content.set(new_res[position]['content'].encode('utf8'))
	art_source.set(new_res[position]['link1'].encode('utf8'))

def makeSearchByWord(word):
	data_base = MongoDB()
	return data_base.findElemetByWord('article_info',word)

def makeTotalSearch():
	data_base = MongoDB()
	return data_base.findElements('article_info')



def makeWindow () :
	global pub_time,art_title,art_content,art_source, select, searchVar
	win = Tk()

	frame1 = Frame(win)
	frame1.pack()

	Label(frame1, text="Enter keyword to search:").grid(row=0, column=0, sticky=W)
	searchVar = StringVar()
	# searchVar.set('ДНР'.encode('utf8'))
	search_field = Entry(frame1, textvariable=searchVar).grid(row=0, column=1, sticky=W)
	search_button = Button(frame1, text="Search", command=searchByWord).grid(row=0,column=2,sticky=W)

	Button(frame1,text="Search All", command=searchAllElements).grid(row=1,column=2)
	

	frame2 = Frame(win)	  # Row of buttons
	frame2.pack(side=LEFT)

	pub_time = StringVar()
	pub_time_label = Label(frame2,text= "Publication time:").grid(row=0,column=0)
	pub_time_content = Message(frame2,textvariable=pub_time,width=800, anchor=W).grid(row=0,column=1)

	art_title = StringVar()
	art_title_label = Label(frame2,text= "Article title:").grid(row=1,column=0)
	art_title_content = Message(frame2,textvariable=art_title,width=800, anchor=E).grid(row=1,column=1)

	art_content = StringVar()
	art_content_label = Label(frame2,text= "Article content:").grid(row=2,column=0)
	art_content_content = Message(frame2,textvariable=art_content,width=800).grid(row=2,column=1)

	art_source = StringVar()
	art_source_label = Label(frame2,text= "Source link:").grid(row=3,column=0)
	art_source_content = Message(frame2,textvariable=art_source,width=800, anchor=NE).grid(row=3,column=1)



	pub_time.set('some date')
	art_title.set('some title')
	art_content.set('some content')
	art_source.set('some link')

	

	frame3 = Frame(win)	  # select of names
	frame3.pack(side=RIGHT)
	scroll = Scrollbar(frame3, orient=VERTICAL)
	select = Listbox(frame3, yscrollcommand=scroll.set, height=10)
	scroll.config (command=select.yview)
	scroll.pack(side=RIGHT, fill=Y)
	select.pack(side=LEFT,  fill=BOTH, expand=1)
	select.bind('<<ListboxSelect>>', loadEntry)
	return win

def setSelect (res):
	global new_res
	new_res = []
	if res.count() == 1:
		try:
			select.delete(0,END)
			select.insert(END, res['title'])
			new_res.append(res)
		except KeyError:
			pass
	else:
		select.delete(0, END)
		for i in res:
			try:
				select.insert(END, i['title'])
				new_res.append(i)
			except KeyError:
				pass



def searchByWord():
	word = searchVar.get().encode('utf8')
	res = makeSearchByWord(word)
	if res.count() == 1:
		pub_time.set(res['pubdate'].encode('utf8'))
		art_title.set(res['title'].encode('utf8'))
		art_content.set(res['content'].encode('utf8'))
		art_source.set(res['link1'].encode('utf8'))
		setSelect(res)
	elif res.count() == 0:
		print "query:  " + str(word)
	else:
		pub_time.set(res[0]['pubdate'].encode('utf8'))
		art_title.set(res[0]['title'].encode('utf8'))
		art_content.set(res[0]['content'].encode('utf8'))
		art_source.set(res[0]['link1'].encode('utf8'))
		setSelect(res)

def searchAllElements():
	res = makeTotalSearch()
	if res.count() == 1:
		try:
			pub_time.set(res['pubdate'].encode('utf8'))
			art_title.set(res['title'].encode('utf8'))
			art_content.set(res['content'].encode('utf8'))
			art_source.set(res['link1'].encode('utf8'))
		except KeyError:
			pass	
		setSelect(res)
	elif res.count() == 0:
		print "query:  ".encode('utf8') + str(word.encode('utf8'))
	else:
		try:
			pub_time.set(res[0]['pubdate'].encode('utf8'))
			art_title.set(res[0]['title'].encode('utf8'))
			art_content.set(res[0]['content'].encode('utf8'))
			art_source.set(res[0]['link1'].encode('utf8'))
		except KeyError:
			pass
		setSelect(res)

win = makeWindow()
# setSelect ()
win.mainloop()