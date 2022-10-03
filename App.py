# Import
import subprocess, sys
import tkinter.simpledialog
from tkinter import *
from tkinter import ttk
import threading
import ffmpeg
from pytube import YouTube
import time
# Function
qc = ""

# Functions
def qc1():
    global qc
    qc = "1"


def qc2():
    global qc
    qc = "2"


def qc3():
    global qc
    qc = "3"


def link():
    global url
    url = getlink.get()

class Converter():
    def run(self):
        link()
        if qc == "1":
            YouTube(url).streams.filter(file_extension="mp4",
                                        progressive=True).get_lowest_resolution().download()
            time.sleep(0.0001)
            Progress.stop()
        else:
            pass
        if qc == "2":
            YouTube(url).streams.filter(
                adaptive=True).first().download(filename="video.mp4", output_path=r"Temp")
            YouTube(url).streams.filter(only_audio=True).first().download(filename="audio.mp3", output_path=r"Temp")
            p = subprocess.Popen(r'powershell.exe -ExecutionPolicy RemoteSigned -file "run.ps1"', stdout=sys.stdout)
            p.communicate()
            time.sleep(0.0001)
            Progress.stop()
        else:
            pass
        if qc == "3":
            title = YouTube(url).title
            YouTube(url).streams.filter(only_audio=True).first().download(filename="{}.mp3".format(title))
            time.sleep(0.0001)
            Progress.stop()
        else:
            pass
    
    def stop(self):
        Progress.stop()

    def __init__(self):
        Progress.start()
        t = threading.Thread(target=self.run)
        t.start()
# GUI

# Setting up Interface
root = Tk()
img = PhotoImage(file=r'C:\Users\Gustavo dos Santos\PycharmProjects\YoutubeDownloader\background.png')
option = IntVar()
root.geometry("700x500")
root.title("Youtube Downloader")
root.iconbitmap(r"C:\Users\Gustavo dos Santos\PycharmProjects\YoutubeDownloader\ico.ico")
canvas = tkinter.Canvas(root, width=700, height=500, highlightthickness=0)
canvas.pack(fill="both", expand=True)
Progress = ttk.Progressbar(canvas,mode="indeterminate", orient="horizontal", length=300)
# Adding widgets on top
canvas.create_image(0, 0, image=img, anchor="nw")
canvas.create_text(362, 120, text="Enter your video's URL", font=40)
getlink = Entry(canvas)
canvas.create_window(362, 150, window=getlink, width=300)
go = Button(canvas, command=Converter, text="Run")
canvas.create_window(362, 180, window=go)
button = Radiobutton(canvas, variable=option, command=qc1, value=1, text="Low Quality  ", background="#bb9df5")
button2 = Radiobutton(canvas, variable=option, command=qc2, value=2, text="High Quality", background="#bb9df5")
button3 = Radiobutton(canvas, variable=option, command=qc3, value=3, text="Audio Only   ", background="#bb9df5")
canvas.create_window(46, 350, window=button)
canvas.create_window(45, 375, window=button2)
canvas.create_window(46, 400, window=button3)
Progress.pack()
root.mainloop()
