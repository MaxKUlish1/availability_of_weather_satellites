from helpers.libs import *


choise_interface=1#выбрать интерфейс
#настройки так же лежат в файле data.json
user_time_zone= "" #возможность вписать временную зону. по дефолту расчитывается по координатам.



##########################
now = True  # Измените это на False чтобы выставить свои даты для просчётов.
                #* True, чтобы выводить пролеты начиная со вчера и заканчивая завтра.
    # Вывести пролеты с использованием выбранной функции вывода.
Yesterday=0#сколько прошедших дней  показать
Tomorrow=2#сколько последующих дней  показать
start_date_="01-02-2023" #дата с которой начинается отсчет необходимых к показу спутников день/месяц/год
end_date_="02-02-2023" #дата на которой заканчивается отсчет необходимых к показу спутников день/месяц/год
##########################
days_for_update=15 #через сколько дней устаревает файл и требует обновления.