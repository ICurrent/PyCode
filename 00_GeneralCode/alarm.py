from datetime import datetime
import time
import winsound

set_alarm = input("Enter your alarm time in HH - MM - SS\n: ")

alarm_hr = set_alarm[0:2]
alarm_min = set_alarm[5:7]
alarm_sec = set_alarm[10:12]
alarm_hr = set_alarm[0:2]

now_hr = datetime.now().strftime('%H')
now_min = datetime.now().strftime('%M')
now_sec = datetime.now().strftime('%S')
now = datetime.now()

# print(now)

if alarm_hr == now_hr:
    if alarm_min == now_min:
        if alarm_sec == now_sec:
            print('Beeping...')
            winsound.Beep()