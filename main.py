from datetime import datetime, timedelta
from timezonefinder import TimezoneFinder
from skyfield.api import Topos, load as sky_load
from pytz import timezone
import json

with open('data.json') as f:
    data = json.load(f)

longitude = data['longitude']
latitude = data['latitude']
angle = data['angle']

# Load data
data = sky_load('de421.bsp')  # Load JPL ephemeris DE421
load = sky_load  # Create a Loader object
ts = load.timescale()  # Call timescale() on the Loader object
tf = TimezoneFinder()

# Get timezone for location
tz_name = tf.timezone_at(lng=longitude, lat=latitude)
tz = timezone(tz_name)

# Set time range
start_time = datetime.now(tz) - timedelta(days=1)
end_time = start_time + timedelta(days=2)

# Set observer location
observer = Topos(str(latitude)+' N', str(longitude)+' E')

# Load satellite data
satellites_url = 'http://celestrak.com/NORAD/elements/weather.txt'
satellites = load.tle_file(satellites_url)
print(f'Loaded {len(satellites)} satellites')
print("""
      ОПИСАНИЕ 
    Цвета: 
       \033[92mЗеленый\033[0m - спутник видим в данный момент,
       \033[93mЖелтый\033[0m - следующий видимый спутник сегодня, 
       \033[94mСиний\033[0m - спутники, видимые позже сегодня или завтра,
       \033[91mКрасный\033[0m - спутники, которые были видны ранее сегодня или вчера.
    Фоны: 
       \033[41mКрасный\033[0m - максимальный угол больше минимального на < 5°, плохо*
       \033[45mФиолетовый\033[0m -  максимальный угол больше минимального < 10°, нормально*
       \033[46mГолубой\033[0m -  максимальный угол больше минимального на < 25°, хорошо*
       \033[42mЗеленый\033[0m - максимальный угол больше минимального на > 25°. отлично*
    *Максимальный угол- угол который достигает спутник во время пролета по отношению к координатам.
    *Минимальный угол- угол указанный в переменной angle, минимальный угол при котором возможен прием. 
      
    Фоны позволяют определить временное окно в которое спутник будет доступен для приема.
      """)
print(f"Указанный угол: {angle}°")

# Find satellite passes
passes = []
for sat in satellites:
    rise_time = None
    t, events = sat.find_events(observer, ts.utc(start_time), ts.utc(end_time), altitude_degrees=angle)
    for ti, event in zip(t, events):
        if event == 0:  # Satellite rises above horizon
            rise_time = ti.utc_datetime()
        elif event == 1:  # Satellite is at its highest point
            pass_time = ti.utc_datetime()
            alt, az, distance = (sat - observer).at(ti).altaz()  # Get altitude and azimuth
            max_elevation = round(alt.degrees, 3)  # Convert altitude (elevation) to degrees and round to 3 decimal places
        elif event == 2:  # Satellite sets below horizon
            if rise_time is not None:
                set_time = ti.utc_datetime()
                visibility_window_seconds = (set_time - rise_time).total_seconds() 
                visibility_window_minutes, visibility_window_seconds = divmod(visibility_window_seconds, 60)
                visibility_window_hours, visibility_window_minutes = divmod(visibility_window_minutes, 60)
                visibility_window_str = "%02d:%02d:%02d" % (visibility_window_hours, visibility_window_minutes, visibility_window_seconds)
                passes.append((rise_time, pass_time, set_time, visibility_window_str, max_elevation, sat.name))

# Sort passes by time
passes.sort(key=lambda x: x[0])

# Print passes
now = datetime.now(tz)

def print_passes(day_str, date):
    print(f'\nСпутники, видимые {day_str}({date.strftime("%Y-%m-%d")}) при минимальном угле {angle}°:')
    next_today_seen = False
    for rise_time, pass_time, set_time, visibility_window_str, max_elevation, sat_name in passes:
        local_rise_time = rise_time.astimezone(tz)
        local_set_time = set_time.astimezone(tz)
        if local_rise_time.date() == date:
            if local_rise_time <= now <= local_set_time:
                color_code = '\033[92m'  # Green for currently visible satellites
            elif local_rise_time > now:
                if local_rise_time.date() == now.date():
                    if not next_today_seen:
                        color_code = '\033[93m'  # Yellow for next visible satellite today
                        next_today_seen = True
                    else:
                        color_code = '\033[94m'  # Blue for satellites visible later today
                else:
                    color_code = '\033[94m'  # Blue for satellites visible tomorrow
            else:
                color_code = '\033[91m'  # Red for satellites that were visible earlier today or yesterday

            # Determine background color based on max elevation
            elevation_difference = max_elevation - angle
            if abs(elevation_difference) <= 5:
                bg_color_code = '\033[41m'  # red background 
            elif abs(elevation_difference) <= 10:
                bg_color_code = '\033[45m'  # Purple background
            elif abs(elevation_difference) <= 25:
                bg_color_code = '\033[46m'  #  Cyan background
            else:
                bg_color_code = '\033[42m'  # 46 green background

            print(f'{color_code}{sat_name} {local_rise_time.strftime("%H:%M:%S")} - {local_set_time.strftime("%H:%M:%S")}\033[0m ({bg_color_code}окно: {visibility_window_str}, максимальный угол: {max_elevation}°\033[0m)')  # Reset color
print_passes(f'вчера', now.date() - timedelta(days=1))
print_passes(f'сегодня', now.date())
print_passes(f'завтра', now.date() + timedelta(days=1))
