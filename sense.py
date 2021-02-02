#! python3
# sense hat reads approximately 17.7 degC higher than ambient temperature

import os, datetime
from sense_hat import SenseHat
from time import sleep

def measure_temp():
        temp = round(SenseHat().get_temperature() -17.7, 1)
        tzdelta = datetime.timezone(datetime.timedelta(hours=-7))
        dt = datetime.datetime.now(tz=tzdelta)
        time = dt.strftime("%m/%d/%Y, %H:%M:%S")
        return time, temp

while True:
        time, temp = measure_temp()
        with open("temp_log.txt", 'a') as f:
                f.write(f'Time: {time}, {temp}\n')
        sleep(900)

