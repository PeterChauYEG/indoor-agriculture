# Indoor Agriculture
This indoor agriculture seeks to be an automated fogponics system.

## Setup
1. Build your circuit following `LED Grow Light.fzz`
2. Upload `grow_light.ino` to an Arduino board
3. Install Python3 dependancies with: `pip install -r requirements.txt`
4. Configure your serial connection to match with the one you are connecting to in: `.env`

## Programs
1. Ensure grow lights and serial communications are working correctly: `python grow_light.py`

**Commands**
```
0: Turn off grow lights
1: Turn on grow lights
exit: Exit program
```

2. Run grow lights on a schedule against `.env` config: `python grow_light_schedule.py`
- Configure your day/night schedule in `.env`
