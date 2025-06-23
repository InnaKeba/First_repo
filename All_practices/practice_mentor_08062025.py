# Написати додаток, який дозволяє слідкувати за фінансами
# За тиждень буду витрачати: 1000
# За понеділок: 100
# За вівт: 200
# Чи вилітив я за бюджет?
# В який день найбільші витрати?

#Варіант з циклом. Нескінченний цикл зупиняється, натиснути Ctrl C в терміналі
#Відступи по всям рядкам вправо виділити код + Tab
#Відступи по всям рядкам вліво виділити код Shift + Tab

# Планований бюджет на тиждень
# Запуск функції def Поки користувач не ввів вірне число
def try_getting_number(prompt):
    while True:
        try:
            weekly_budjet = float(input(prompt))
            # print("Введено вірне значення")
            return weekly_budjet #зупиняє функцію 
        except ValueError:
            print("Введіть нове значення, попереднє число не є вірним")

weekly_budjet = try_getting_number("Введіть ваш бюджет на тиждень:  ")
print(f"Бюджет на тиждень {weekly_budjet}")
money_spent_during_the_week = []

weekdays=['monday', 'Tuesday', 'wednesday']
#Заповнення значень у список
for i in range(3):
    day = weekdays[i]
    money_spent_during_the_week.append(try_getting_number(f"Введіть ваші витрати {day} "))

# #Понеділок 
# money_spent_during_the_week.append(try_getting_number("Введіть ваші витрати за понеділок:  "))
# #Вівторок
# money_spent_during_the_week.append(try_getting_number("Введіть ваші витрати за вівторок: "))
# #Середа
# money_spent_during_the_week.append(try_getting_number("Введіть ваші витрати за середу: "))
print(money_spent_during_the_week)

sum_money = sum(money_spent_during_the_week) # агрегація витрат 
print(f"Витрати за тиждень:{sum_money}")
print(f"Фактична витрата: {weekly_budjet - sum_money}")

#Найбільший показник витрат за тиждень
# max_value = max(expenses.values())
# print(max_value)
# for day in expenses:
#     if expenses[day] == max_value:
#        break

