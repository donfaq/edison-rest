from flask import Flask, url_for
import edison_control as ec
from flask import request

app = Flask(__name__)
led_state = 0


@app.route("/led")
def led():
    global led_state
    if led_state == 0:
        led_state = 1
    else:
        led_state = 0
    ec.led_write(led_state)
    return "Now led state is " + str(led_state)


@app.route('/message')
def message():
    ec.lcd_write(str(request.args.get('text')))
    return "Your message is: \"" + str(request.args.get('text'))


@app.route('/hello')
def hello_world():
    return 'hello world!'


if __name__ == '__main__':
    app.run()
