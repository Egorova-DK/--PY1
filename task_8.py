def number_of_months(money_capital, salary, spend, increase):
    money = money_capital
    month = 0
    while money > spend:
        money -= spend
        spend = spend + (spend * increase)
        money += salary
        month += 1
    return month


print(number_of_months(10000, 5000, 6000, 0.05))
