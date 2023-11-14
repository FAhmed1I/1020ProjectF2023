###Imports###
from engi1020.arduino.api import *
from guizero import *
from random import *
###Scripts/Algorithms###
def set_goal():
    freq = randint(0,100)
    print(freq)
    buzzer_frequency(5, freq)
    return freq



###GUI###
hear = App(title='Hearing Game')

pad1 = Text(hear, text = '', size = 40)
intro = Text(hear, text = "Welcome to the Sound Game", size=40)

mode_1 = PushButton(hear, text='Play', command=set_goal)

hear.display()