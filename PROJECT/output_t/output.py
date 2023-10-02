from helpers.all_helpers import *
from output_t import my_print,pretty_t,rich_t
def choise_output(passes, start_date, end_date):
    # Выберите функцию вывода

    #для использования стандартного вывода choise = 0
    #для использования вывода pretty_table choise = 1
    # Для использования вывода rich choise = 1
    choise=1
    if choise==0:
        output_function = my_print.output_with_your_print
    elif choise==1:
        output_function = pretty_t.print_table
    elif choise==2:
        print("НЕ РЕКОМЕНДУТЕСЯ СТАВИТЬ РАСЧЕТ БОЛЕЕ ЧЕМ НА 3 ДНЯ НА rich.")
        time.sleep(7)
        output_function = rich_t.output_with_rich
    

    
        

    true_sats = [key for key in satellite_types if satellite_types[key] == True]
    print(f'''
    ──────────────────────────────────────  
    🌐 Временная зона: {tz}
    ⏰ Настоящее время: {now}
    📅 Даты: {start_date} --- {end_date}
    🛰️ Выбранные типы спутников: {', '.join(true_sats)}
    📐 Минимальный угол видимости: {angle}
    🧭 Указанный азимут: {azimuth_range}
    ──────────────────────────────────────
''')
    # Отсортировать пролеты по времени

    output_function(passes, start_date, end_date)
