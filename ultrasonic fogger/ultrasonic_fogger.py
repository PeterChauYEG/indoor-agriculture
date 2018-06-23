from dotenv import load_dotenv
from dotenv import find_dotenv
import os
import serial

# load settings
load_dotenv(find_dotenv())

# global
loop = 1
serialPort = os.getenv("SERIAL_PORT")

# open serial connection
serialConnection = serial.Serial(serialPort, 9600)

# FUNCTIONS --------------------------------------------------------------------
# intro
def introduction():
    print("GROW LIGHT~~~\n")
    print("Connected to port: {}\n".format(serialPort))

    print("0: Turn off grow lights")
    print("1: Turn on grow lights")
    print("2: Turn off ultrasonic fogger")
    print("3: Turn on ultrasonic fogger")
    print("exit: Exit program\n\n")

# MAIN -------------------------------------------------------------------------
# inform user
introduction()

# start an input loop
while loop:
    # get user input
    user_input = input("Enter a command: ")

    # check for exit command
    if user_input == 'exit':
        loop = 0
    else:
        # send encoded input to arduino
        serialConnection.write(user_input.encode())
