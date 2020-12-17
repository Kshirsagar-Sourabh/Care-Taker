import time
from pygame import mixer
from datetime import datetime
from time import time
def musicanloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
def log_now(msg):
    f=open("mylogs.txt","a")
    f.write(f"{msg} {datetime.now()}\n")
if __name__ == "__main__":
    #musicanloop("water.mp3","stop")
      
        init_water=time()
        init_eyes=time()
        init_exercise=time()
        watersecs=5
        exsecs=20
        eyessecs=30
        while True:
            if time()-init_water > watersecs:
                print("Water Drinking time. Enter 'drank' to Stop the alarm. ")
                musicanloop("water.mp3","drank")
                init_water=time()
                log_now("Water Drank at ")
            if time()-init_eyes > eyessecs:
                print("Eyes Relaxed time. Enter 'eydone' to Stop the alarm. ")
                musicanloop("eyes.mp3","eydone")
                init_eyes=time()
                log_now("Eyes Relaxed at ")
            if time()-init_exercise > exsecs:
                print("Physical activity time. Enter 'exdone' to Stop the alarm. ")
                musicanloop("exercise.mp3","exdone")
                init_exercise=time()
                log_now("Exercise Done at ")