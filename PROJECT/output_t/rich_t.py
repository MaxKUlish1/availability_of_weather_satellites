from helpers.all_helpers import *

def output_with_rich(passes, start_date, end_date):
    # Создать объект Console
    console = Console()

    # Создать объект Table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Дата", style="dim", width=12)
    table.add_column("Время", style="dim", width=12)
    table.add_column("Спутник", style="dim", width=15)
    table.add_column("Тип", style="dim", width=15)

    # Добавить данные в таблицу
    now = datetime.now(tz)
    next_today_seen = False

    for rise_time, pass_time, set_time, visibility_window_str, max_elevation, sat_name, sat_types in passes:
        local_rise_time = rise_time.astimezone(tz)
        local_set_time = set_time.astimezone(tz)
        if start_date <= local_rise_time.date() <= end_date:
            # Определить цвет строки на основе времени пролета
            if local_rise_time <= now <= local_set_time:
                color_code = 'green'  # Зеленый для спутников, которые видны в данный момент
            elif local_rise_time > now:
                if local_rise_time.date() == now.date() and not next_today_seen:
                    color_code = 'yellow'  # Желтый для следующего видимого спутника сегодня
                    next_today_seen = True
                else:
                    color_code = 'blue'  # Синий для спутников, видимых завтра или позже сегодня
            else:
                color_code = 'red'  # Красный для спутников, которые были видны ранее сегодня или вчера

            # Добавить строку в таблицу
            table.add_row(
                local_rise_time.strftime("%Y-%m-%d"),
                f"{local_rise_time.strftime('%H:%M:%S')} - {local_set_time.strftime('%H:%M:%S')}",
                sat_name,
                ",".join(sat_types),
                style=color_code
            )

            # Добавить разделитель (строку из символов '-')
            table.add_row("───────────", "───────────", "──────────────", "──────────────")

    # Вывести таблицу
    console.print(table)