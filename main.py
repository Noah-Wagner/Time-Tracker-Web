from flask import Flask, request, render_template

import TimeTracker

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("base.html")


@app.route('/clockout')
def calculate_time_page():
    return render_template("timeto40.html")


@app.route('/calc_time')
def calculate_time():
    goal_hours = request.args.get('goal_hours')
    hours_worked = request.args.get('hours_worked')
    clocked_in_time = request.args.get('time_clocked_in')
    try:
        clockout_time = TimeTracker.calculate_clockout_time(float(goal_hours), float(hours_worked), clocked_in_time)
        clockout_time_string = TimeTracker.format_time(clockout_time)
    except ValueError as err:
        print(err)
        return 'Error: ' + str(err)
    return clockout_time_string


if __name__ == '__main__':
    app.run()
