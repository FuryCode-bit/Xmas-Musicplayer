import os, time, random, pygame
from PIL import Image, ImageTk
import tkinter as tk

playing = 0
index = 0
n = 0
music = "null"

pygame.mixer.init()

root = tk.Tk()
root.title("Reprodutor de musicas mp3")
root.geometry("850x750")
root.iconbitmap("./img/xmas.ico")
root.resizable(False, False)
bg= tk.PhotoImage(file="bg.png")

text = tk.StringVar()
text.set("Reprodutor de musicas mp3 [Xmas Edition]")

playBtn= tk.PhotoImage(file="./img/play50.png")
stopBtn= tk.PhotoImage(file="./img/stop50.png")
nextBtn= tk.PhotoImage(file="./img/forward50.png")

def getMusic():
    global index, files, music, n, text
    files = os.listdir('./music')

    n = len(files)
    #print(files)

    index = random.randint(0,n-1)

    music = files[index]

    return music

def nextMusic():
    global index, files, music, playing, n, text

    files.pop(index)
    n = len(files)
    if(n == 0):
        files = os.listdir('./music')
        n = len(files)
        #print(n)
        pygame.mixer.music.stop()

        index = random.randint(0,n-1)
        music = files[index]

        dirMusica = (f'./music/{music}')

        pygame.mixer.music.load(dirMusica)
        pygame.mixer.music.play()
        text.set(music)

        addQueue()

    else:
        if(playing == 1):
            pygame.mixer.music.stop()

            index = random.randint(0,n-1)
            music = files[index]

            dirMusica = (f'./music/{music}')

            pygame.mixer.music.load(dirMusica)
            pygame.mixer.music.play()
            text.set(music)

            addQueue()


    #print(files)

def addQueue():

    files = os.listdir('./music')

    for song in files:
        dirSong = (f'./music/{song}')

    pygame.mixer.music.queue(dirSong)

def play():
    global playing, text

    #print(playing)

    music = getMusic()
    #print(music)
    
    dirMusica = (f'./music/{music}')

    pygame.mixer.music.load(dirMusica)
    pygame.mixer.music.play()
    text.set(music)
    addQueue()
    
    playing = 1

def stop():
    global playing, text

    pygame.mixer.music.stop()
    text.set("Reprodutor de musicas mp3 [Xmas Edition]")

    playing = 0

label = tk.Label(root, image=bg)
label.place(x=0, y=0, relwidth=1, relheight=1)
varNome = tk.Label(root, textvariable=text, anchor="e", justify="center", font=('Helvetica', 15)).place(relx=0.5, rely=0.5, anchor="center")
play_btn = tk.Button(root, text="Play", command=play, image=playBtn, height=50, width=50).place(relx=0.4, y=500)
stop_btn = tk.Button(root, text="stop", command=stop, image=stopBtn, height=50, width=50).place(relx=0.5, y=500)
next_btn = tk.Button(root, text="Next", command=nextMusic, image=nextBtn, height=50, width=50).place(relx=0.6, y=500)


root.mainloop()


