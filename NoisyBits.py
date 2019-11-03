import random
import playsound
import time
#import msvcrt
import keyboard

def main():
    rand = random.randint(60, 300)
    randFart = str(random.randint(1,3))
    time.sleep(rand)
    counter = 0
    
    #while (True):
        #keypress = msvcrt.getch()
        

    FartName = "Farts/Fart" + randFart + ".mp3"
    from playsound import playsound
    playsound(FartName)




while(True):
    main()