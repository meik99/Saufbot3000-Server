import logging

from message.warning import Warning

from gpiozero.pins.mock import MockFactory
from gpiozero import Device, LED
from time import sleep

PUMPS = [
    4, 17, 27, 22, 5, 6, 13, 26
]


LOGGER = logging.getLogger(__name__)

class Raspberry():
    def __init__(self, factory=MockFactory()):
        if len(PUMPS) != 8:
            LOGGER.warning(Warning().wrong_pump_count(8, len(PUMPS)))

        Device.pin_factory = factory

        self.pumps = []

        for pump_pin in PUMPS:
            self.pumps.append(LED(pump_pin))

class Pump():
    def __init__(self, led: LED):
        self.index = PUMPS.index(led.pin._number)
        self.value = led.value
        self.pin = led.pin._number
