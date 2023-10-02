availability_of_weather_satellites[BETA] Программа для определения времени доступности множества спутников. Работает без подключения к интернету.

Для запуска программы необходимо ввести следующие данные в файле data.json:

азимут, долготу и широту места наблюдения
минимальный угол видимости спутника (angle)
типы спутников, которые хотите видеть (например, military, iridium, weather, visual и т.д.)
конкретные названия спутников, которые хотите видеть (например, NOAA 17 [+])
Программа имеет три варианта интерфейса: старый (0), рекомендуемый (1) и улучшенный (2).

Пример интерфейса 1

![Image](https://github.com/MaxKUlish1/availability_of_weather_satellites/raw/main/1_interf.png)
Пример интерфейса 2

![Image](https://github.com/MaxKUlish1/availability_of_weather_satellites/raw/main/2_interf.png)
Пример интерфейса 3

![Image](https://github.com/MaxKUlish1/availability_of_weather_satellites/raw/main/3_interf.png)

ВНИМАНИЕ! ЭТА ВЕРСИЯ НЕ ПРОХОДИЛА ТЕСТИРОВАНИЕ. ЕСЛИ ВЫ НАЙДЕТЕ ОШИБКИ, ПОЖАЛУЙСТА, СВЯЖИТЕСЬ СО МНОЙ В ТЕЛЕГРАМ @MX_WORLD

*Что нового в этой версии

Добавлены три варианта интерфейса на выбор пользователя.
Добавлена возможность вводить азимут для учета препятствий на горизонте.
Расширен список типов спутников с одного до тринадцати.
Добавлена возможность выбирать конкретные спутники для отображения по полному названию.
Добавлена функция автообновления файлов орбит с настройкой периода устаревания.
Добавлены два способа выбора дат для отображения в интерфейсе.

Планируется

Добавить функцию, которая позволит отслеживать положение спутника на небе в реальном времени.
Исправить ошибку с автоматическим обновлением файлов орбит и добавлением новых.
Проверять наличие подключения к интернету и не удалять файлы орбит при его отсутствии.
Создать телеграм-бота.



