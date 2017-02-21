from flask import Flask
import edison_control as ec
from flask import request
from decorator import crossdomain
import threading


app = Flask(__name__)


@app.route("/led", methods=['POST'])
@crossdomain(origin='*')
def led():
    return ec.change_led_state(str(request.args.get('color')))


@app.route("/temperature", methods=['POST'])
@crossdomain(origin='*')
def temperature():
    return ec.get_temperature()


@app.route('/message',  methods=['POST'])
@crossdomain(origin='*')
def message():
    ec.lcd_write(str(request.args.get('text')))
    return "Message displayed"


@app.route('/sound',  methods=['POST'])
@crossdomain(origin='*')
def sound():
    ec.play_sound()
    return "Sound played"


@app.route('/music',  methods=['POST'])
@crossdomain(origin='*')
def music():
	if str(request.args.get('state')) == "playing":
		ec.playing = True
	elif str(request.args.get('state')) == "pause":
		ec.playing = False
	return "Succ"


if __name__ == '__main__':
	ec.playing = False
	thread = threading.Thread(target=ec.music_thread, args=())
	thread.start()
	app.run()
