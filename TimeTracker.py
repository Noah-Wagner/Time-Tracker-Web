import datetime


def calculate_clockout_time(goal_hours_, hours_so_far_, clocked_in_time_):
    if goal_hours_ is None or hours_so_far_ is None or clocked_in_time_ is None:
        raise ValueError('No parameters can be null!')

    hours_left_ = goal_hours_ - hours_so_far_

    clocked_in_time_ = datetime.datetime.strptime(clocked_in_time_, "%H:%M")

    new_time_ = datetime.timedelta(hours=hours_left_) + clocked_in_time_
    return new_time_


def format_time(time):
    return datetime.datetime.strftime(time, "%I:%M %p")
