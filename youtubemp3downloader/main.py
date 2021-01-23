from __future__ import unicode_literals
import youtube_dl
import os
import tkinter
from tkinter import *
from tkinter import messagebox
import os



class Download(object):
    def __init__(self, url):
        self.url = url
        self.save_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        self.song()

    def song(self):
        opts = {
            'verbose': True,
            'fixup': 'detect_or_warn',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '1411',
            }],
            'ExtractAudio': True,
            'outtmp1': self.save_path + '/%(title).%(ext)s',
            'noplaylist': True
        }
        yd1 = youtube_dl.YoutubeDL(opts)
        yd1.download([self.url])


def urldownload():
    url1 = url1_field.get()
    url2 = url2_field.get()
    downloading()
    Download(url1)
    Download(url2)
    downloaded()

def openfile():
    os.startfile(r"C:\Users\SElangovan\PycharmProjects\youtubemp3downloader")






def downloading():
    messagebox.showinfo('Process','Downloading....')
def downloaded():
    messagebox.showinfo1('Process','Downloaded')

def clear():
    url1_field.delete(0,END)
    url2_field.delete(0,END)




if __name__ == '__main__':
    root = Tk()
    root.title('olivegreen Creation')
    root.configure(background='white')
    root.geometry("550x400")

    icon = tkinter.PhotoImage(file = r"C:\Users\SElangovan\Desktop\download.png")
    headlabel = tkinter.Label(image = icon)
    label = Label(root,text = 'Olivegreen.mp3 Downloader',fg='green',bg='white',font=('arial black',15))




    label1 = Label(root,text = 'Enter Url (1) :',fg = 'black',bg = 'white',font =('arial black',10))
    label2 = Label(root,text ='Enter Url (2) :',fg ='black',bg ='white',font=('arial black',10))

    headlabel.grid(row = 0,column =1)
    label.grid(row=1,column=1)
    label1.grid(row=2,column=0)
    label2.grid(row=6,column=0)

    url1_field = Entry(root)
    url2_field = Entry(root)
    url1_field.grid(row=2,column=1,sticky = 'E',ipadx = '125')
    url2_field.grid(row=6,column=1,sticky='E',ipadx = '125')


    button1 = Button(root,text ='Download',font =('arial black',8),fg = 'black',bg='grey',command =urldownload)
    button2 = Button(root,text ='Open Location',font =('arial black',8),fg='black',bg='yellow',command=openfile)
    button3 = Button(root,text = 'Clear',font=('arial black',8),fg='white',bg='red',command=clear)



    button1.grid(row ='7',column='1')
    button2.grid(row='10',column='1')
    button3.grid(row='4',column='2')


    root.mainloop()
