# uses

- json
- sys
- os.path
- math.sqrt

# Ближайшие бары

Скрипт использует открытые данные в json формате о барах Москвы
и выводит наибольший, наименьший бары по количеству мест,
а так же ищет ближайший к введенным координатам.

Функции:

- load_jsonfile(filepath)
загружает файл в json формате с исходными данными

- get_biggest_bar(json_input)
принимает на вход json данные и ищет словарь с информацией о самом вместительном баре

- get_smallest_bar(json_input)
принимает на вход json данные и ищет словарь с информацией о самом маленьком (по количеству мест) баре

- get_closest_bar(json_input, longitude, latitude)
принимает на вход json данные а так же координаты: долготу и ширину. Выводит словарь с информацией о баре

- print_bar(bar, type)
выводит даные бара на экран, подставляя его тип

- print_bars_info(json_input)
выводит большой/маленький бар а так же ближайший

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
файл с данными доступен по ссылке: https://op.mos.ru/EHDWSREST/catalog/export/get?id=84505
json (zip)

Запуск на Linux:

```#!bash

$ python bars.py filepath longitude latitude # possibly requires call of python3 executive instead of just python
python bars.py data.json 37 55                                                                                                                                                  

Biggest bar is: "Спорт бар «Красная машина»" with ID: 00138530, seats: 450                                                                                                                                          
Smallest bar is: "БАР. СОКИ", with ID: 00107283, seats: 0                                                                                                                                                           
Nearest bar is: "Staropramen" with ID: 00146638, seats: 50

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
