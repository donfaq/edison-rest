import mraa
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_buzzer as upmBuzzer
import time

RED_LED_PIN = 2
GREEN_LED_PIN = 3
BLUE_LED_PIN = 4
TEMP_PIN = 0
BUZZER_PIN = 5

# led init
ledPins = {"R": mraa.Gpio(RED_LED_PIN), "G": mraa.Gpio(GREEN_LED_PIN), "B": mraa.Gpio(BLUE_LED_PIN)}
[ledPin.dir(mraa.DIR_OUT) for key, ledPin in ledPins.items()]

# temp init
temp = grove.GroveTemp(TEMP_PIN)

# lcd init
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.clear()

# buzzer init
buzzer = upmBuzzer.Buzzer(5)
buzzer.stopSound()
notes = [0, 10, 10, 30, 40, 70, 100, 130, 180, 220, 270, 300, 310, 290, 220, 130, 560, 210, 500, 500, 500, 500]
global playing_request
global stop_request
playing_request = False
stop_request = False


def change_led_state(color):
    led = ledPins.get(str(color))
    led.write(0 if led.read() == 1 else 1)
    return str(led.read())


def lcd_write(message):
    lcdDisplay.clear()
    lcdDisplay.write(message)


def get_temperature():
    return str(temp.value() - 3)


def play_sound():
    buzzer.playSound(upmBuzzer.DO, 10000)
    time.sleep(2)
    buzzer.stopSound()


def stop_music():
    global stop_request
    stop_request = True


def music_thread():
    global playing_request
    global stop_request
    try:
        current_notes = list(notes)
        while True:
            while playing_request and not stop_request:
                if len(current_notes) == 0:
                    print("Start from beginning")
                    current_notes = list(notes)

                note = current_notes.pop(0)
                buzzer.playSound(note, 100000)
                time.sleep(0.05)
                print("playing " + str(note))
            if stop_request:
                playing_request = False
                stop_request = False
                current_notes = list(notes)
                buzzer.stopSound()
    except (KeyboardInterrupt, SystemExit):
        buzzer.stopSound()
        exit()
