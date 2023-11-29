import time
import random
from engi1020.arduino.api import *

frequency = 0

# Function to play a random tone
def play_random_tone():
    frequency = random.randint(0, 1023)  # Generate a random frequency
    print(frequency)
    duration = 2  # Set the duration of the tone (can change)

    buzzer_frequency(5, frequency)  # Play the tone
    time.sleep(duration)  # Wait for the duration
    buzzer_stop(5)  # Stop the tone
    return frequency
    
def frequency_value(value):
    # Map the dial value (0-1023) to a frequency range (200-2000 Hz)
    return int(value / 1023 * 1700) + 300

# Main loop for the game
while True:
    print("Listen to the tone...")
    frequency = play_random_tone()  # Play a random tone
    
    print("Now, try to match the tone by turning the rotary dial.")
    print("Adjust the dial and press Enter when you think you've matched it.")
    
    while True:
        dial_value = analog_read(0)  # Read the value from the rotary dial
        frequency_map = frequency_value(dial_value) # Map dial value to frequency 
        buzzer_frequency(5, frequency_map) # Play the corresponding tone
        time.sleep(0.1)  # Small delay to prevent overwhelming serial output
    
        input("Press Enter to check...")  # Wait for user input
        print("Your guess:", dial_value)

        # Determine if the guess is close enough to the played tone
        # You may adjust the tolerance level based on your preferences
        if abs(dial_value - frequency) < 50:
            print("Congratulations! You matched the tone!")
            buzzer_stop(5)
            break
        else:
            print("Sorry, your guess is not quite there. Try again!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        break
    
