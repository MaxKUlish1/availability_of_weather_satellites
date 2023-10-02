from helpers.all_helpers import *
from sat_find.connect_sites import *



def load_sat_data():
    # Загрузить данные о спутниках
    satellites = []
    satellite_types_list = {}
    for sat_type, url in satellite_urls.items():
        if satellite_types.get(sat_type, False):  # Если этот тип спутника установлен в True в JSON-файле
            filename = url.split('/')[-1]
            if os.path.exists(os.path.join('..', 'files', 'txt_files', filename)):
                file_time = os.path.getmtime(filename)
                if time.time() - file_time > 15 * 24 * 60 * 60:
                    print(f"Файл {filename} устарел. Хотите ли вы его обновить? (y/n)")
                    answer = input()
                    if answer.lower() == 'y':
                        os.remove(filename)
                        sats = load.tle_file(url)
                    else:
                        sats = load.tle_file(filename)  # Загрузите файл TLE из существующего файла
                else:
                    sats = load.tle_file(filename)  # Загрузите файл TLE из существующего файла
            else:
                sats = load.tle_file(url)

            satellites.extend(sats)
            for sat in sats:
                if sat.name not in satellite_types_list:
                    satellite_types_list[sat.name] = [sat_type]
                else:
                    satellite_types_list[sat.name].append(sat_type)
    return satellites,satellite_types_list
# Загрузить данные
data = sky_load('PROJECT/files/de421.bsp')  # Загрузить эфемериды JPL DE421
load = sky_load  # Создать объект Loader

