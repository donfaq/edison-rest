import mraa
import pyupm_i2clcd as lcd

ledPin = mraa.Gpio(7)
ledPin.dir(mraa.DIR_OUT)

lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.clear()


def led_write(state):
    ledPin.write(state)


def lcd_write(message):
    lcdDisplay.clear()
    lcdDisplay.write(message)
