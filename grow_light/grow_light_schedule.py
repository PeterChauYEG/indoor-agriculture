from dotenv import load_dotenv
from dotenv import find_dotenv
import datetime
import os
import schedule
import serial
import time

# load settings
load_dotenv(find_dotenv())

# global
DAY_HOURS = os.getenv("DAY_HOURS")
NIGHT_HOURS = os.getenv("NIGHT_HOURS")
serialPort = os.getenv("SERIAL_PORT")

# open serial connection
serialConnection = serial.Serial(serialPort, 9600)

# FUNCTIONS --------------------------------------------------------------------
# intro
def introduction():
    print("Running a {}/{} (day/night) schedule".format(DAY_HOURS, NIGHT_HOURS))

# generate times for the schedule
def generateTimes():
    # get current time
    now = datetime.datetime.now()

    # convert hours to seconds
    nightSeconds = int(NIGHT_HOURS) * 60 * 60

    # generate times
    nightTime = (now + datetime.timedelta(0, nightSeconds)).strftime('%H:%M')
    dayTime = now.strftime('%H:%M')

    return dayTime, nightTime

# set the schedule
def setSchedule(dayTime, nightTime):
    schedule.every().day.at(dayTime).do(grow_light, 'DAY')
    schedule.every().day.at(nightTime).do(grow_light, 'NIGHT')

# set grow_light mode
def grow_light(mode):
    command = 0

    # check the mode and map it to a command
    if mode == 'DAY':
        command = 1
        print("Running day mode for {}".format(DAY_HOURS))
    elif mode == 'NIGHT':
        command = 0
        print("Running night mode for {}".format(NIGHT_HOURS))

    # send command to arduino
    serialConnection.write(command)

# MAIN -------------------------------------------------------------------------
# inform user
introduction()

# generate times
dayTime, nightTime = generateTimes()

# set schedule
setSchedule(dayTime, nightTime)

# start with lights on
grow_light('DAY')

# start schedule loop
while 1:
    schedule.run_pending()
    time.sleep(1)
