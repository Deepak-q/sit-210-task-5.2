# Import necessary modules
import tkinter as tk
from tkinter import ttk
import RPi.GPIO as GPIO

# GPIO pins for LEDs
LED_PINS = [17, 18, 27]  

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Function to set the selected LED
def set_led(idx):
    for i, pin in enumerate(LED_PINS):
        if i == idx:
            # Turn on the selected LED
            GPIO.output(pin, GPIO.HIGH)
        else:
            # Turn off the other LEDs
            GPIO.output(pin, GPIO.LOW)

# Function to exit the program
def exit_program():
    # Clean up GPIO settings
    GPIO.cleanup()
    # Close the Tkinter window
    root.destroy()

# Create the main Tkinter window
root = tk.Tk()
root.title("LED Controller")
root.geometry("400x300")  # Set window size

# Create a label for user instructions
label = tk.Label(root, text="Select LED Color", font=("Helvetica", 16))
label.pack(pady=10)

# Create a frame to hold radio buttons
radio_frame = ttk.Frame(root)
radio_frame.pack()

# Create radio buttons for Red, Green, and Blue LEDs
radio_buttons = []
for i, color in enumerate(["Red", "Green", "Blue"]):
    # Use ttk.Radiobutton for themed radio buttons
    radio_button = ttk.Radiobutton(radio_frame, text=f"{color} LED", value=i, command=lambda idx=i: set_led(idx))
    radio_button.grid(row=i, column=0, sticky="w", padx=20, pady=5)
    radio_buttons.append(radio_button)

# Create an exit button to close the program
exit_button = ttk.Button(root, text="Exit", command=exit_program)
exit_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
