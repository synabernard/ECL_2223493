import dht11
import RPi.GPIO as GPIO
import time
import blynklib
BLYNK_AUTH = '-3LYwlQaOUmTtpGhIieDolO8VROVpMYR'
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
instance = dht11.DHT11(pin=4)
blynk = blynklib.Blynk(BLYNK_AUTH)
while True:
    result = instance.read()
    if result.is_valid():
        humidity = result.humidity
        temperature = result.temperature
        print("Temperature: %d C" % temperature)
        print("Humidity: %d %%" % humidity)
        blynk.virtual_write(1, temperature)
        blynk.virtual_write(2, humidity)

        if humidity > 70:
            blynk.notify('Humidity is above 70%!')
        time.sleep(2)
