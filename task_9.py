# salary = 5000  # зарплата
# spend = 6000  # траты
# months = 10  # количество месяцев
# increase = 0.03  # рост цен
#
# need_money = 0  # количество денег, чтобы прожить 10 месяцев

def need_many(spend, increase, months, salary):
    expenses = 0
    money_capital = 0
    for i in range(1, months + 1):
        expenses += spend
        spend = spend + (spend * increase)
        money_capital += salary
    return expenses - money_capital


print(round(need_many(6000, 0.03, 10, 5000)))
