salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0
full_spend = 0
for i in range(months):
    full_spend = full_spend + spend
    spend = spend * (1 + increase)

full_salary = salary * months
need_money = full_spend - full_salary

print(round(need_money))
