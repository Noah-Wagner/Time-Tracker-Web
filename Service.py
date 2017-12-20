from flask import Flask
from flask import request
from flask import json

import TimeTracker

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/time')
def clockout_time():
    goal_hours = request.args.get('goal_hours')
    hours_worked = request.args.get('hours_worked')
    clocked_in_time = request.args.get('time_clocked_in')
    try:
        clockout_time = TimeTracker.calculate_clockout_time(float(goal_hours), float(hours_worked), clocked_in_time)
        clockout_time_string = TimeTracker.format_time(clockout_time)
    except ValueError as err:
        print(err)
        return 'Error!'
    return clockout_time_string


if __name__ == '__main__':
    app.run()
