from time import *
import random
from guizero import *
from engi1020.arduino.api import *
def sound_it():
    frequency = 0
    hear = App(title='SoundIt')

    # Function to play a random tone
    def play_random_tone():
        frequency = random.randint(0, 1023)  # Generate a random frequency
        print(frequency)
        duration = 2  # Set the duration of the tone (can change)

        buzzer_frequency(5, frequency)  # Play the tone
        sleep(duration)  # Wait for the duration
        buzzer_stop(5)  # Stop the tone
        return frequency
        
    def frequency_value(value):
        # Map the dial value (0-1023) to a frequency range (200-2000 Hz)
        return int(value / 1023 * 1700) + 300

    # Main loop for the game
    def hear_game():
        guessos = 0
        start_time = time()
        while True:
            
            frequency = play_random_tone()  # Play a random tone
            
            while digital_read(6) is False:
                dial_value = analog_read(0)  # Read the value from the rotary dial
                frequency_map = frequency_value(dial_value) # Map dial value to frequency 
                buzzer_frequency(5, frequency_map) # Play the corresponding tone
                sleep(0.1)  # Small delay to prevent overwhelming serial output

                # Determine if the guess is close enough to the played tone
                # You may adjust the tolerance level based on your preferences
            
            else:
                if abs(dial_value - frequency) < 50:
                    oled_clear()
                    oled_print("Congratulations!")
                    buzzer_stop(5)
                    end_time = time()
                    watch = end_time - start_time
                    results = Window(hear, title='Your Results')
                    blank1 = Text(results, size=60)
                    ttl = Text(results, size=60, text='Congratulations! \nYou guessed the frequency!')
                    guesses = Text(results, size =30, text=f'It took you {guessos} guesses and {watch:.2f} seconds')
                    with open('resultats.txt', 'a') as r:
                        r.write(f'{Guesses} guesses. Time: {watch:.3f} seconds')
                    start_again = Text(results, size=24, text='Close this window to play again')
                    break
                
                else:
                    guessos += 1
                    oled_clear()
                    oled_print("Incorrect! Try again!")


        
    ### The Graphical User Interface
    blank1 = Text(hear, size=60)
    title = Text(hear, size=70, text='SoundIt')
    start = PushButton(hear, text='Start Game', command=hear_game)
    blank2 = Text(hear,size=60, align='bottom')
    instructions = Box(hear, align='bottom', layout='grid')
    sec1 = Text(instructions, 'The game will proceed as follows:', size=24, grid=[0,0])

    instr1 = Text(instructions, '1. The buzzer will play a random sound.',grid=[0,1], align='left', size=18)
    instr2 = Text(instructions, '2. You have to try and match the frequency by turning the rotary dial',grid=[0,2], align='left', size=18)
    instr3 = Text(instructions, '3. Press the Button to confirm your guess', grid=[0,3], align='left', size=18)
    instr4 = Text(instructions, '4. The OLED Screen will print if you are correct or not. You can keep guessing until you are correct', grid=[0,4], align='left', size=18)
    instr5 = Text(instructions, '5. Once you get it correct, a new window will open with results ',grid=[0,5], align='left', size=18)
    instr6 = Text(instructions, 'Press the Start Game Button to Start', grid=[0,6], size=24)

    hear.display()

