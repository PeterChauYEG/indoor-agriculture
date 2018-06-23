# Indoor Agriculture
This indoor agriculture seeks to be an automated fogponics system.

## Setup
1. Build your circuit following `grow_light.fzz` or `ultrasonic_fogger.fzz`
2. Upload the appropriate program to an Arduino board
3. Install Python3 dependancies with: `pip install -r requirements.txt`
4. Configure your serial connection to match with the one you are connecting to in: `.env`

## Programs
### Test Grow Lights and Serial Communications
Ensure grow lights and serial communications are working correctly: `python grow_light.py`

**Commands**
```
0: Turn off grow lights
1: Turn on grow lights
exit: Exit program
```

### Run grow lights on a schedule
Run grow lights on a schedule against `.env` config: `python grow_light_schedule.py`
- Configure your day/night schedule in `.env`

### Test Grow Lights and Serial Communications
Ensure grow lights, ultrasonic fogger, and serial communications are working correctly: `python ultrasonic_fogger.py`

**Commands**
```
0: Turn off grow lights
1: Turn on grow lights
2: Turn off ultrasonic fogger
3: Turn on ultrasonic fogger
exit: Exit program
```

### Run grow lights and ultrasonic fogger on a schedule
Run grow lights on a schedule against `.env` config: `python ultrasonic_fogger_schedule.py`
- Configure your day/night schedule in `.env`
-
## Raspberry Pi Setup
- Create an image on a Micro SD card (Raspbian Jessie Lite)
- add the `ssh.txt` file in the pi folder to the card
- configure your network, and add the `wpa_supplicant.conf` file in the pi folder to the card
- run `sudo raspi-config`, expand your filesystem, and update the pi software
- reboot the pi with `sudo reboot`
- run `sudo apt-get update && sudo apt-get upgrade`
- install git: `sudo apt-get install git`
- install pip: `sudo apt-get install python3-pip`

**NOTE:** python version 3 is aliased as python3. Pip is pip3.
