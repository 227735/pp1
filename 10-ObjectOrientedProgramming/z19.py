import random

class Thermometer:
    def __init__(self):
        self.is_on = False
        self.temperature = 0.0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure_temperature(self):
        if self.is_on:
            self.temperature = round(random.randrange(340, 421) / 10, 1)
            return self.temperature
        else:
            return "Thermometer is off."

    def display(self):
        message = f"Temperature: {self.temperature}C"
        if self.temperature >= 37.0:
            message += " (fever)"
        if self.temperature >= 41.0:
            message += " !!CRITICAL TEMPERATURE!!"
        return message

thermometer = Thermometer()
thermometer.turn_on()
temperature_measurement = thermometer.measure_temperature()
temperature_display = thermometer.display()
print(temperature_display)
thermometer.turn_off()
temperature_measurement_while_off = thermometer.measure_temperature()
print(temperature_measurement_while_off)