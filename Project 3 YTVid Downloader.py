from pytube import YouTube

from tkinter import *

root = Tk()
root.geometry("300x400")
root.title("Youtube Video Downloader")
root.configure(bg="Black")
def start_message():
    messagebox.showinfo('YTV Downloader!',"Downloading Please Wait...!")

def downcomplete():
    messagebox.showinfo('YTV Downloader!',"Download Complete!!")
    
def youtube():
    a = var.get() #https://www.youtube.com/watch?v=7C2z4GqqS5E
    ytvideo = YouTube(a).streams.filter(file_extension = "mp4", progressive= True).order_by('resolution').desc().first()
    start_message()
    ytvideo.download()
    downcomplete()
    
   
l1 = Label(text = "Enter Youtube Link Below!", fg = "Red", font = "bold", bg = "black")
l1.place(x=60,y=30)

var = StringVar()
e1 = Entry(root,textvariable = var, width = 45)
e1.place(x=15,y=100)

b1 = Button(root, text = "Download Video!", command = youtube, font = "bold", bg = "red", width = 20, fg = "white")
b1.place(x= 60, y=150)


root.mainloop()