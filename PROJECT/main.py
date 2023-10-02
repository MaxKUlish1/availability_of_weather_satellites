from helpers.all_helpers import *
from sat_find.data_sattelites import *
from sat_find.logic_sat import *
from output_t.output import *


# Время пролёта
start_date, end_date = check_now_or_data()
# Установить местоположение наблюдателя
observer = Topos(str(latitude)+' N', str(longitude)+' E')
# Найти пролеты спутников
satellites,satellite_types_list=load_sat_data()
# Просчёт0
passes=logic_sat([observer],[satellites,satellite_types_list],[start_date,end_date],satellite_names)
# Вывод
choise_output(passes, start_date, end_date)


