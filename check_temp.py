#! python3

from sense_hat import SenseHat

sense = SenseHat()

print(round(sense.get_temperature(), 1))

print(round(sense.get_temperature() - 17.7, 1))
