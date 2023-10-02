from helpers.libs import *
from helpers.settings import*
with open('PROJECT/helpers/data.json') as f:
    data = json.load(f)

longitude = data['longitude']
latitude = data['latitude']
angle = data['angle']
azimuth_range = data.get('azimuth_range', (0, 360))  # Получить диапазон азимута из JSON-файла
satellite_types = data.get('satellite_types', {})  # Получить типы спутников из JSON-файла
satellite_names = data.get('satellite_names', []) # Получить названия спутников которые отображать/если их нет отображать все
tf = TimezoneFinder()
tz_name = tf.timezone_at(lng=longitude, lat=latitude)
if user_time_zone:
    tz = timezone(user_time_zone)
else:
    tz = timezone(tz_name)


def check_now_or_data():
    if now:
        # Установить временной диапазон
        start_date = (datetime.now(tz) - timedelta(days=Yesterday)).date()
        end_date = start_date + timedelta(days=Yesterday+Tomorrow) # Расширить конечное время до 4 дней от текущего момента

    else:
        start_date = datetime.strptime(start_date_, "%d-%m-%Y").date()#??????????
        end_date = datetime.strptime(end_date_, "%d-%m-%Y").date()
    return start_date, end_date