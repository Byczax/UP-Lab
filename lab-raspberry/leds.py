import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
PIN = 40

GPIO.setup(PIN, GPIO.OUT)
while True:
    time.sleep(0.1)
    GPIO.output(PIN, 0)
    time.sleep(0.1)
    GPIO.output(PIN, 1)