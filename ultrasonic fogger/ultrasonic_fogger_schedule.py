from dotenv import find_dotenv
from dotenv import load_dotenv
import datetime
import os
import schedule
import serial
import time
import threading

# load settings
load_dotenv(find_dotenv())

# global
DAY_HOURS = os.getenv("DAY_HOURS")
NIGHT_HOURS = os.getenv("NIGHT_HOURS")
serialPort = os.getenv("SERIAL_PORT")
ULTRASONIC_FOGGER_OFF_MINUTES = os.getenv("ULTRASONIC_FOGGER_OFF_MINUTES")
ULTRASONIC_FOGGER_ON_MINUTES = os.getenv("ULTRASONIC_FOGGER_ON_MINUTES")

# FUNCTIONS --------------------------------------------------------------------
def initializeSerial():
    print("Opening serial connection")

    # open serial connection
    serialConnection = serial.Serial(serialPort, 9600)
    time.sleep(5)
    return serialConnection

# intro
def introduction():
    print("GROW LIGHT && ULTRASONIC FOGGER~~~")
    print("Grow Light: Running a {}/{} (day/night) schedule".format(DAY_HOURS, NIGHT_HOURS))
    print("Ultrasonic Fogger: Running a {}/{} (on/off) schedule".format(ULTRASONIC_FOGGER_ON_MINUTES, ULTRASONIC_FOGGER_OFF_MINUTES))

# generate minutes for the grow light schedule
def generateGrowLightTimes():
    # convert hours to int minutes
    dayMinutes = int(DAY_HOURS)
    nightMinutes = int(NIGHT_HOURS)


    return dayMinutes, nightMinutes

# generate times for the ultrasonic fogger schedule
def generateUltraSonicFoggerTimes():
    # convert to ints
    mistMinutes = int(ULTRASONIC_FOGGER_ON_MINUTES)
    dryMinutes = int(ULTRASONIC_FOGGER_OFF_MINUTES)

    return mistMinutes, dryMinutes

# run fogger sub schedule
def growLightCycle(dayMinutes):
    daySeconds = dayMinutes * 60

    growLight('DAY')

    timer = threading.Timer(daySeconds, growLight, ['NIGHT'])
    timer.start()

# run fogger sub schedule
def ultrasonicFoggerCycle(mistMinutes):
    mistSeconds = mistMinutes * 60

    ultrasonicFogger('MIST')

    timer = threading.Timer(mistSeconds, ultrasonicFogger, ['DRY'])
    timer.start()

# set the schedule
def setSchedule(dayMinutes, nightMinutes, mistMinutes, dryMinutes):
    # intervals for day/night cycle
    schedule.every(dayMinutes + nightMinutes).minutes.do(growLightCycle, dayMinutes)

    # intervals for mist/dry cycle
    schedule.every(mistMinutes + dryMinutes).minutes.do(ultrasonicFoggerCycle, mistMinutes)

# set grow_light mode
def growLight(mode):
    command = 0

    # check the mode and map it to a command
    if mode == 'DAY':
        command = "1"
        print("Running day mode for {}".format(DAY_HOURS))
    elif mode == 'NIGHT':
        command = "0"
        print("Running night mode for {}".format(NIGHT_HOURS))

    # send command to arduino
    serialConnection.write(command.encode())

# set ultrasonic_fogger mode
def ultrasonicFogger(mode):
    command = "2"

    # check the mode and map it to a command
    if mode == 'MIST':
        command = "3"
        print("Running mist mode for {}".format(ULTRASONIC_FOGGER_ON_MINUTES))
    elif mode == 'DRY':
        command = "2"
        print("Running dry mode for {}".format(ULTRASONIC_FOGGER_OFF_MINUTES))

    # send command to arduino
    serialConnection.write(command.encode())

# MAIN -------------------------------------------------------------------------
# inform user
introduction()

# initialize serial connection
serialConnection = initializeSerial()

# generate times
dayMinutes, nightMinutes = generateGrowLightTimes()
mistMinutes, dryMinutes = generateUltraSonicFoggerTimes()

# set schedule
setSchedule(dayMinutes, nightMinutes, mistMinutes, dryMinutes)

# start cycles
growLightCycle(dayMinutes)
ultrasonicFoggerCycle(mistMinutes)

# start schedule loop
while 1:
    schedule.run_pending()
    time.sleep(1)
