from guizero import App, Box, Picture, Text, TextBox, PushButton, Window
from engi1020.arduino.api import *
from random import *
from time import *
from PIL import *

rcton = App(title='ReactTest')

### The Game ###
def rctgame():
    times = []
    oled_clear()
    
    for i in range(3):

        start_time = time()
        
        while digital_read(6) is False:
            oled_clear()
            digital_write(4, True)

        
        else:
            digital_write(4, False)
            end_time = time()
            react_time = end_time - start_time
            print(react_time)
            times.append(react_time)
            oled_print(f'Your time was {react_time:.4f} seconds')
            sleep(randint(1,5))
    
    avg_time = sum(times)/len(times)
    print(avg_time)
    
    
    if avg_time < 0.773:
        quality = 'Above Average'
        pic = 'cheetah.png'
        
    
    elif avg_time == 0.773:
        quality = 'Average'
        pic = 'meh.png'
    
    else:
        quality = 'Below Average'
        pic = 'turtle.png'
        
    with open('resultats.txt','a') as r:
        r.write(f'Reaction: Average Reaction Time {react_time:.4f}. {quality.upper()}')
        
    results = Window(rcton, title='ReactTest Results')
    blank1 = Text(results, size=60)
    resttl = Text(results, size=60, text='Your Results')
    compa = Picture(results, image=pic)
    avg_time = Text(results, size=30, text=f'Your average reaction time was {react_time:.3f} seconds')
    react_age = Text(results, size=30, text=f'Your reaction times were {quality}')
    react_disclaimer = Text(results, size=16, text='The reaction times were based on the Human Benchmarks average reaction time, with an added .5 second lag due to the button')
    blank2 = Text(results, size=40)
    resexit = Text(results, size=30, text='Close this window to play again')
    

### The Graphical User Interface ###

blank1 = Text(rcton, size=50)
blank2 = Text(rcton, size=70, align='bottom')
rctn = Box(rcton, align = 'bottom', layout="grid")
titular = Text(rcton, 'ReactTest', size=80)
start = PushButton(rcton, text='Press to Start',command=rctgame, image='brain.png')
sec1 = Text(rctn, 'The game will proceed as follows:', size=24, grid=[0,0])

inst1 = Text(rctn, '1. The light on the Arduino will turn on.',grid=[0,1], align='left', size=18)
inst2 = Text(rctn, '2. You will press the Button on the Arduino when you see it light up.',grid=[0,2], align='left', size=18)
inst3 = Text(rctn, '3. Your reaction time will be logged and printed on the OLED screen', grid=[0,3], align='left', size=18)
inst4 = Text(rctn, '4. Steps 1-3 will repeat 10-20 times', grid=[0,4], align='left', size=18)
inst5 = Text(rctn, '5. Your average reaction time will be displayed in a new window on your computer, along with how they compare to the average',grid=[0,5], align='left', size=18)
inst6 = Text(rctn, 'Press the Brain to Start', grid=[0,6], size=24)

rcton.set_full_screen()
rcton.display()