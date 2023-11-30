import time
import random
from engi1020.arduino.api import *
from guizero import App, Box, Picture, Text, TextBox, PushButton, Window

pttrn = App(title='PatternTest')

# Function to generate a random pattern
def generate_pattern(length):
    return [random.choice(['0', '1']) for i in range(length)]

# Function to play the pattern
def play_pattern(pattern):
    for action in pattern:
        if action == '0':  # Play buzzer sound
            buzzer_frequency(5, 1150)
            time.sleep(0.3)
            buzzer_stop(5)
        elif action == '1':  # Light up LED
            digital_write(4, True)
            time.sleep(0.3)
            digital_write(4, False)
        time.sleep(0.2)

# Function to take user input for the pattern
def user_input(length):
    keylist = []
    keys = input()

    for i in keys:
        keylist.append(i)
        
    for i in keylist:
        if i == '0':  # Play buzzer sound
            buzzer_frequency(5, 1150)
            time.sleep(0.3)
            buzzer_stop(5)
        elif i == '1':  # Light up LED
            digital_write(4, True)
            time.sleep(0.3)
            digital_write(4, False)
        time.sleep(0.2)
    
    return keylist

# Main game loop
def pattern_game():
    pattern_length = 3 # Length of pattern, changes to scale with levels
    level = 0
    print("Welcome to the Pattern Game!")
    
    while True:
        pattern = generate_pattern(pattern_length)

        print("Watch the pattern of sound and light, then repeat it.")
        print("Press 1 for the LED, and press 0 for the buzzer.")
        print("Example: 11010")

        play_pattern(pattern)
        time.sleep(2)
        user_pattern = user_input(pattern_length)

        if user_pattern == pattern:
            print("Congratulations! You matched the pattern.")
            pattern_length += 1  # Increase pattern length upon correct match
            level = pattern_length - 3
            time.sleep(2)
            
        else:
            print("Sorry, your pattern didn't match.")
            print("You made it to level: ",level)
            break

### The Graphical User Interface ###

blank1 = Text(pttrn, size=50)
blank2 = Text(pttrn, size=70, align='bottom')
ptrn = Box(pttrn, align = 'bottom', layout="grid")
titular = Text(pttrn, 'PatternTest', size=80)
start = PushButton(pttrn, text='Press to Start',command=pattern_game, image='lightbulb_music.png')
sec1 = Text(ptrn, 'Welcome to the Pattern Game!', size=30, grid=[0,0])
sec2 = Text(ptrn, 'The game will proceed as follows:', size=24, grid=[0,1])

inst1 = Text(ptrn, '1. Watch and listen to the pattern coming from the LED and Buzzer on the arduino.',grid=[0,2], align='left', size=18)
inst2 = Text(ptrn, '2. Once the pattern is over, you will need to type a series of 1s and 0s.',grid=[0,3], align='left', size=18)
inst3 = Text(ptrn, '3. 1s correspond to the LED, and 0s correspond to the Buzzer. (Example: 11010)', grid=[0,4], align='left', size=18)
inst4 = Text(ptrn, '4. Each time you get the pattern correct the length of the pattern will increase by one.', grid=[0,5], align='left', size=18)
inst5 = Text(ptrn, '5. If you get a pattern wrong your game will be over and you will be prompted to play again.',grid=[0,6], align='left', size=18)
inst6 = Text(ptrn, '6. You will be able to see your score once the game is over.',grid=[0,7], align='left', size=18)
inst7 = Text(ptrn, 'Press the Lightbulb to Start', grid=[0,8], size=24)

pttrn.set_full_screen()
pttrn.display()
pattern_game()