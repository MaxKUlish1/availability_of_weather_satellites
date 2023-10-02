from prettytable import PrettyTable
from datetime import datetime
import helpers.output_helpers as help_me
from helpers.all_helpers import *


def get_color_code(local_rise_time, local_set_time, next_today_seen):
    d_now = datetime.now(tz)
    if local_rise_time <= d_now <= local_set_time:
        color_code = '\033[92m'  # Зеленый для спутников, которые видны в данный момент
    elif local_rise_time > d_now:
        if local_rise_time.date() == d_now.date():
            if not next_today_seen:
                color_code = '\033[93m'  # Желтый для следующего видимого спутника сегодня
                next_today_seen = True
            else:
                color_code = '\033[94m'  # Синий для спутников, видимых позже сегодня
        else:
            color_code = '\033[94m'  # Синий для спутников, видимых завтра
    else:
        color_code = '\033[91m'  # Красный для спутников, которые были видны ранее сегодня или вчера
    return color_code, next_today_seen



def get_bg_color_code(max_elevation, angle):
    elevation_difference = max_elevation - angle
    if abs(elevation_difference) <= 5:
        bg_color_code = '\033[41m'  # Красный фон
    elif abs(elevation_difference) <= 10:
        bg_color_code = '\033[45m'  # Фиолетовый фон
    elif abs(elevation_difference) <= 25:
        bg_color_code = '\033[46m'  # Голубой фон
    else:
        bg_color_code = '\033[42m'  # Зеленый фон
    return bg_color_code


def print_table(passes, start_date, end_date):
    while start_date <= end_date:
        print_passes(start_date.strftime("%d-%m-%Y"), end_date, passes, start_date)
        start_date += timedelta(days=1)


def print_passes(day_str,end_date , passes, start_date):
    next_today_seen = False
    table = PrettyTable()
    table.field_names = ["Date", "Satellite Name", "Rise Time", "Set Time", "Visibility Window", "Max Angle", "Types"]
    for rise_time, pass_time, set_time, visibility_window_str, max_elevation, sat_name, sat_types in passes:
        local_rise_time = rise_time.astimezone(tz)
        local_set_time = set_time.astimezone(tz)
        if start_date <= local_rise_time.date() <= end_date:
            
            color_code, next_today_seen = get_color_code(local_rise_time, local_set_time, next_today_seen)
            bg_color_code = get_bg_color_code(max_elevation, angle)
            table.add_row([day_str, f'{color_code}{sat_name}\033[0m', local_rise_time.strftime("%d-%m-%Y %H:%M:%S"), local_set_time.strftime("%d-%m-%Y %H:%M:%S"), f'{bg_color_code}{visibility_window_str}\033[0m', max_elevation, ",".join(sat_types)])
    print(table)
