money = int(input())
"""years = int(input())
total = money

def total_deposit(money, years, total):
	for i in range(1,years):
		total = money+0.04*money
		print('%.2f' % total)
	if years == 0:
		return total

	else :
		return total_deposit(money, years-1, total)"""

first_year = money + money *0.04
print('%.2f' % first_year)
second_year = first_year + first_year *0.04
print('%.2f' % second_year)
third_year = second_year + second_year*0.04
print('%.2f' % third_year)
fourth_year = third_year + third_year*0.04
print('%.2f' % fourth_year)