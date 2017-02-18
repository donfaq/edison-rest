from flask import Flask

import edison_control as ec
from flask import request

from decorator import crossdomain

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


if __name__ == '__main__':
    app.run()
