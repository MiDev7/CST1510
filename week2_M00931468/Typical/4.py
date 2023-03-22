# calculating the amount of money you will have in 3 years

number_of_week_per_year = 52

normalRate = 10

yearOneRate = 20

revenue_for_first_year = yearOneRate * number_of_week_per_year

revenue_per_year = normalRate * number_of_week_per_year

expense_per_year = 0.5 * (number_of_week_per_year / 2)

print(expense_per_year * 3)

sumFirstYearRevenue = revenue_for_first_year - expense_per_year

sumTwoLastYear = (revenue_per_year - expense_per_year) * 2

print(f'The amount of money after 3 year is: £{sumFirstYearRevenue + sumTwoLastYear}')


