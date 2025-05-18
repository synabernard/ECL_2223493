import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED is ON")
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED is OFF")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram stopped and GPIO cleaned up.")
