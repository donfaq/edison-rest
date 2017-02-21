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

#led init
ledPins = {"R": mraa.Gpio(RED_LED_PIN), "G": mraa.Gpio(GREEN_LED_PIN), "B": mraa.Gpio(BLUE_LED_PIN)}
[ledPin.dir(mraa.DIR_OUT) for key, ledPin in ledPins.items()]

#temp init
temp = grove.GroveTemp(TEMP_PIN)

#lcd init
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.clear()

#buzzer init
buzzer = upmBuzzer.Buzzer(5)
buzzer.stopSound()
notes = [0,10,10,30,40,70,100,130,180,220,270,300,310,290,220,130,560,210,500,500,500,500]
global playing

def change_led_state(color):
    led = ledPins.get(str(color))
    led.write(0 if led.read() == 1 else 1)
    return str(led.read())


def lcd_write(message):
    lcdDisplay.clear()
    lcdDisplay.write(message)


def get_temperature():
    return str(temp.value()-3)


def play_sound():
    buzzer.playSound(upmBuzzer.DO, 10000)
    time.sleep(2)
    buzzer.stopSound()


def music_thread():
	try:
	    while(True):
        	if(playing):
        		for notes_ind in range (0,22):
        			print("playing " + str(notes[notes_ind]))
        			if playing == True:
        				#print("playing " + str(notes[notes_ind]))
        				buzzer.playSound(notes[notes_ind], 100000)
	                	time.sleep(0.05)
	                else:
						print("waiting butt") 
						buzzer.stopSound()
						i = 0
						while(playing != True):
							print (i)
							i = i + 1
							time.sleep(0.01)
	except (KeyboardInterrupt, SystemExit):
		buzzer.stopSound()
		exit()
