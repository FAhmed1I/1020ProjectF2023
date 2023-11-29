import time
import random
from engi1020.arduino.api import *


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

pattern_game()