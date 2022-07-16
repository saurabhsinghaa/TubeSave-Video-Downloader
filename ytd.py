from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
# TO MOVE FILE TO DIRECTORY
import shutil

# FUNCTIONS
def select_path():
    """
    To allow user to select path
    """
    path = filedialog.askdirectory()
    path_label.configure(text=path)

def download_file():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    root.title('Downloading...')
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    shutil.move(mp4_video,user_path)
    root.title('!!Download Completed!!')



root = Tk()

title = root.title('YOUTUBE VIDEO DOWNLOADER')
img = PhotoImage(file="yticonn.png")
root.iconphoto(False,img)

canvas = Canvas(root,width=500,height=500)
canvas.pack()
canvas.configure(bg='gray22')
logo_img = PhotoImage(file='ytred.png')
logo_img = logo_img.subsample(2,2)
canvas.create_image(250,90,image=logo_img)
link_field = Entry(root,width=50)
link_label = Label(root,text="PASTE YOUR LINK BELOW",font=('Arial',9),fg='white',bg='gray22')
path_label = Label(root,text='SELECT PATH TO DOWNLOAD',font=('Arial',9),fg='white',bg='gray22')
select_btn = Button(root,text="BROWSE PATH",padx=10,fg='white',bg='dim gray',command=select_path)

canvas.create_window(250,215,window=link_label)
canvas.create_window(250,240,window=link_field)
canvas.create_window(250,285,window=path_label)
canvas.create_window(250,310,window=select_btn)

download_btn = Button(root,text="DOWNLOAD FILE",padx=30,pady=7,fg='white',bg='indian red',borderwidth=3, command=download_file)
canvas.create_window(250,400,window=download_btn)


root.mainloop()