from helpers.libs import *

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
tz = timezone(tz_name)

now = True  # Измените это на False чтобы выставить свои даты для просчётов.
                #* True, чтобы выводить пролеты начиная со вчера и заканчивая завтра.
    # Вывести пролеты с использованием выбранной функции вывода.
    
def check_now_or_data():
    if now:
        # Установить временной диапазон
        Yesterday=0#до
        Tomorrow=2#после
        start_date = (datetime.now(tz) - timedelta(days=Yesterday)).date()
        end_date = start_date + timedelta(days=Yesterday+Tomorrow) # Расширить конечное время до 4 дней от текущего момента

    else:
        start_date = datetime.strptime("01-02-2023", "%d-%m-%Y").date()#??????????
        end_date = datetime.strptime("02-02-2023", "%d-%m-%Y").date()
    return start_date, end_date