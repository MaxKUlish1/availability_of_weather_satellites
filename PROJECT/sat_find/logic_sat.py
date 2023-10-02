from helpers.all_helpers import *
ts = load.timescale()  # Вызвать timescale() на объекте Loader

# Установить временной диапазон
from helpers.all_helpers import *
ts = load.timescale()  # Вызвать timescale() на объекте Loader

# Установить временной диапазон
def logic_sat(_observer,_sat_list,_date, _satellite_filter):
    observer=_observer[0]
    satellites,satellite_types_list=_sat_list
    start_time,end_time=_date
    # Найти пролеты спутников
    passes = []
    for sat in satellites:
        if _satellite_filter and sat.name not in _satellite_filter:
            continue
        rise_time = None
        t, events = sat.find_events(observer, ts.utc(start_time), ts.utc(end_time), altitude_degrees=angle)
        for ti, event in zip(t, events):
            alt, az, distance = (sat - observer).at(ti).altaz()  # Получить высоту и азимут
            if azimuth_range[0] <= az.degrees <= azimuth_range[1]:  # Проверить, находится ли азимут в указанном диапазоне
                if event == 0:  # Спутник поднимается над горизонтом
                    rise_time = ti.utc_datetime()
                elif event == 1:  # Спутник находится на своей самой высокой точке
                    pass_time = ti.utc_datetime()
                    max_elevation = round(alt.degrees, 3)  # Преобразовать высоту (элевацию) в градусы и округлить до 3 десятичных знаков
                elif event == 2:  # Спутник опускается ниже горизонта
                    if rise_time is not None:
                        set_time = ti.utc_datetime()
                        visibility_window_seconds = (set_time - rise_time).total_seconds() 
                        visibility_window_minutes, visibility_window_seconds = divmod(visibility_window_seconds, 60)
                        visibility_window_hours, visibility_window_minutes = divmod(visibility_window_minutes, 60)
                        visibility_window_str = "%02d:%02d:%02d" % (visibility_window_hours, visibility_window_minutes, visibility_window_seconds)
                        passes.append((rise_time, pass_time, set_time, visibility_window_str, max_elevation, sat.name, satellite_types_list[sat.name]))

    # Отсортировать пролеты по времени
    passes.sort(key=lambda x: x[0])

    return passes
