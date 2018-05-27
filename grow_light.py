from pathlib import Path
from dotenv import load_dotenv
import os
import serial

# load settings
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

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
