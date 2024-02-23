import random
import time

from Server import sendVitals


def generateAlert(alertType):
    print(f"Alert: {alertType}")
    time.sleep(5)

def generate_heart_rate():
    while True:
        temp =  random.randint(59, 101)
        if temp < 60:
            generateAlert("Heart Rate low")
        elif temp > 100:
            generateAlert("Heart Rate high")
        yield temp
        time.sleep(1)

def generate_respiration_rate():
    while True:
        temp = random.randint(11, 21)
        if temp < 12:
            generateAlert("Respiration Rate low")
        elif temp > 20:
            generateAlert("Respiration Rate high")
        yield temp
        time.sleep(1)

def generate_temperature():
    while True:
        temp = round(random.uniform(36.4, 37.6), 1)
        if temp < 36.5:
            generateAlert("Temperature low")
        elif temp > 37.5:
            generateAlert("Temperature high")
        yield temp
        time.sleep(1)


def generate_spO2():
    while True:
        temp = random.randint(94, 100)
        if temp < 95:
            generateAlert("SpO2 low")
        yield temp 
        time.sleep(1)



heart_rate_stream = generate_heart_rate()
respiration_rate_stream = generate_respiration_rate()
temperature_stream = generate_temperature()
spO2_stream = generate_spO2()

while True:
    print(f"Heart Rate: {next(heart_rate_stream)}")
    print(f"Respiration Rate: {next(respiration_rate_stream)}")
    print(f"Temperature: {next(temperature_stream)}")
    print(f"SpO2: {next(spO2_stream)}")
    print()
    time.sleep(1)
