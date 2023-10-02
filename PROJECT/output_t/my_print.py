from helpers.all_helpers import *


def output_with_your_print(passes, start_date, end_date):
    
    now = datetime.now(tz)
    
        
    def print_passess(day_str, date):
        print(f'\nСпутники, видимые {date.strftime("%Y-%m-%d")} ({day_str}) при минимальном угле {angle}°:')
        next_today_seen = False
        for rise_time, pass_time, set_time, visibility_window_str, max_elevation, sat_name, sat_types in passes:
            local_rise_time = rise_time.astimezone(tz)
            local_set_time = set_time.astimezone(tz)
            if local_rise_time.date() == date:
                if local_rise_time <= now <= local_set_time:
                    color_code = '\033[92m'  # Зеленый для спутников, которые видны в данный момент
                elif local_rise_time > now:
                    if local_rise_time.date() == now.date():
                        if not next_today_seen:
                            color_code = '\033[93m'  # Желтый для следующего видимого спутника сегодня
                            next_today_seen = True
                        else:
                            color_code = '\033[94m'  # Синий для спутников, видимых позже сегодня
                    else:
                        color_code = '\033[94m'  # Синий для спутников, видимых завтра
                else:
                    color_code = '\033[91m'  # Красный для спутников, которые были видны ранее сегодня или вчера

                # Определить цвет фона на основе максимальной высоты
                elevation_difference = max_elevation - angle
                if abs(elevation_difference) <= 5:
                    bg_color_code = '\033[41m'  # Красный фон 
                elif abs(elevation_difference) <= 10:
                    bg_color_code = '\033[45m'  # Фиолетовый фон
                elif abs(elevation_difference) <= 25:
                    bg_color_code = '\033[46m'  # Голубой фон
                else:
                    bg_color_code = '\033[42m'  # Зеленый фон

                print(f'{color_code}{sat_name} {local_rise_time.strftime("%H:%M:%S")} - {local_set_time.strftime("%H:%M:%S")}\033[0m ({bg_color_code}окно: {visibility_window_str}, максимальный угол: {max_elevation}°\033[0m) [type_select:{",".join(sat_types)}]')  # Сбросить цвет

    # Вывести пролеты за каждый день в заданном промежутке дат
    from babel.dates import format_date


    
    datee = start_date
    while datee <= end_date:
        day_of_week = format_date(datee, 'EEEE', locale='ru_RU')
        print_passess(day_of_week, datee)
        datee += timedelta(days=1)

        