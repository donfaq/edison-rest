import mraa
import pyupm_grove as grove
import pyupm_i2clcd as lcd

RED_LED_PIN = 2
GREEN_LED_PIN = 3
BLUE_LED_PIN = 4
TEMP_PIN = 0

ledPins = {"R": mraa.Gpio(RED_LED_PIN), "G": mraa.Gpio(GREEN_LED_PIN), "B": mraa.Gpio(BLUE_LED_PIN)}
[ledPin.dir(mraa.DIR_OUT) for key, ledPin in ledPins.items()]

temp = grove.GroveTemp(TEMP_PIN)

lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.clear()


# def sound():
#     play_sound()


def change_led_state(color):
    led = ledPins.get(str(color))
    led.write(0 if led.read() == 1 else 1)
    return str(led.read())


def lcd_write(message):
    lcdDisplay.clear()
    lcdDisplay.write(message)


def get_temperature():
    return str(temp.value()-3)
