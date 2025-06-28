# Weather application

![big_screen.png](static/icon/big_screen.png)

Цей проект розроблено з метою ознайомлення із роботою API, принципом отримання даних від віддаленого серверу, вмінням їх обробляти, структурувати та застосовувати у своємо проєкті. А саме застосовувалось API такого веб-ресурсу як [OpenWeatherMap](https://openweathermap.org). Проєкт допоможе розібратися із роботою файлів JSON, як правильно отримувати та зберігати дані у файлах з типом .json. Та познайомити користувача з інтерфейсом застосунку розробленим за допомогою пакету [CustomTkinter](https://customtkinter.tomschimansky.com)

### Зміст репозиторія:

1. [Основні модулі проєкту](#all-modules)
2. [Розгортання проєкту](#download-project)
3. [Створення віртуального оточення проєкту](#create-venv)
4. [Завантаження модулів до віртуального оточення](#download-modules-venv)
5. [Старт проєкту](#start-project)
6. [Основні механіки проєкту](#all-mechanics)
7. [Висновок по проєкту](#result) 
___
<h4 id= 'all-modules'>Основні модулі проєкту:</h4>
All modules

- [customtkinter](https://customtkinter.tomschimansky.com/)
- [json](https://docs.python.org/3/library/json.html)
- [requests]()
- [pillow]()
- [os]()
- [colorama]()
- [datetime]()
___
<h4 id= 'download-project'>Розгортання проєкту:</h4>
Download project

1. Склонувати з GitHub репозиторію:
    - натисніть на кнопку "Code"
    - скопіюйте посилання для клонування
![Image alt](https://github.com/alex21000211/WeatherApp-/blob/Alex-Belyaev/images/README%20clone.png)
2. Завантажити за допомогою zip-архіву
    - у тому ж "Code" треба завантажити zip-архів
![Image alt](https://github.com/alex21000211/WeatherApp-/blob/Alex-Belyaev/images/download%20Zip.png)
<h4 id= 'create-venv'>Створення віртуального оточення проєкту:</h4>
Сreate venv

1. Windows
    - треба відкрити bash терменал та написати python -m venv venv і ваше віртуальне оточення зробиться
![Image alt](https://github.com/alex21000211/WeatherApp-/blob/Alex-Belyaev/images/python%20-m%20venv%20venv.jpg)
    - для активації віртуальне оточення треба ця камнда source venv\Scripts\activate
![Image alt](https://github.com/alex21000211/WeatherApp-/blob/Alex-Belyaev/images/source%20venv%20Scripts%20activate.jpg)

2. Mac OS або Linux
    - щоб створити на Mac OS треба ця ж команда
![Image alt](https://github.com/alex21000211/WeatherApp-/blob/Alex-Belyaev/images/python%20-m%20venv%20venv.jpg)
    - щоб активувати на Mac OS треба source venv\bin\activate
![Image alt](https://github.com/alex21000211/WeatherApp-/blob/Alex-Belyaev/images/source%20venvbinactivate.jpg)
<h4 id= 'download-modules-venv'>Завантаження модулів до віртуального оточення:</h4>
Download modules venv

1. Окремими модулями
![Image alt](https://github.com/alex21000211/WeatherApp-/blob/Alex-Belyaev/images/os.jpg)
- треба написати pip install потім назву модолю який ходите встановити
2. За допомогою файлу requirements.txt
![Image alt](https://github.com/alex21000211/WeatherApp-/blob/Alex-Belyaev/images/requirements.jpg)
- встановіть за допомогою requirements

<h4 id= 'start-project'>Старт проєкту:</h4>
Start project
    - терміналі: python main.py (або python3 main.py)

<h4 id= 'start-project'>Висновок по проєкту::</h4>
Result
    - У цьому проєкті я ознайомився з використанням бібліотек customtkinter, requests, Pillow, Colorama, datetime. Працював через термінал і навчився правильно організовувати структуру коду.
