from gtts import gTTS
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfile
fh = open('select location of file','r')
txt=fh.read().replace('\n','')

language = 'en' #select language "en' stands for English

output = gTTS(text=txt,lang=language,slow=False) #slow refers to speed of speaking

output.save("Select the location here.mp3")

os.system("start that file.mp3")
