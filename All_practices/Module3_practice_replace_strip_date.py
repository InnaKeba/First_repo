
# text = "Hello,, son ,,,, When are yoo coming home,"

# def dad_filter(message):
#     while ",," in message:
#         message = message.replace(",,",",")
#     return message.strip(",") #strip чистить зайву кому вкінці

# res = dad_filter(text)
# print(res)

### DATE
import datetime
now = datetime.datetime.now()
print(now)

#щоб отримати дату (без часу) та час (без дати):
from datetime import datetime
current_datetime = datetime.now()
print(current_datetime.date())
print(current_datetime.time())

# Створення об'єкта datetime з конкретною датою і часом
import datetime
specific_datetime = datetime.datetime(2020, 1, 7, 14, 30, 15)
print(specific_datetime)  # Виведе "2020-01-07 14:30:15"
from datetime import date # початок роботи з датами

#Розрахунок різниці між датами
since = date(2025, 6, 5)
td = date.today()
days = (td-since).days
print(days)

#Ми хочемо визначити скільки пройшло повних днів, коли Наполеон спалив Москву, а це відбулося 14 вересня 1812 року
from datetime import datetime
# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)
# Поточна дата
current_date = datetime.now()
# Розрахунок кількості днів
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since)

# == (рівність): Порівнює, чи є дві дати рівні.
# != (нерівність): Порівнює, чи дві дати не є рівними.
# < (менше): Визначає, чи одна дата передує іншій.
# > (більше): Визначає, чи одна дата наступає за іншою.
# <= (менше або дорівнює): Порівнює, чи одна дата менше або дорівнює іншій.
# >= (більше або дорівнює): Порівнює, чи одна дата більше або дорівнює іншій.