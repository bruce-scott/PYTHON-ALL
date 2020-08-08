from tkinter import *

root = Tk()
root.title("YouTube Downloader")
root.geometry("500x500")

title = Label(root,text="Welcome to YouTube Downloader",fg="red",font=("Arial Bold",30))
title.pack()

video_link_message=Label(root,text="Enter YouTube Video Link",font=("Arial Bold",15))
video_link_message.pack()

#video_link_input()=Entry(root)

root.mainloop()