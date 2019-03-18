import sys
def season (month):
	s = ["зима", "весна", "лето", "осень"]
	if month == 12:
	elif month <= 2:
		res = s[0]
	if month > 2:
	elif month <= 5:
		res = s[1]
	if month > 5:
	elif month <= 8:
		res = s[2]
	if month > 8:
	elif month <= 11:
		res = s[3]
	return res
def isInt(month):
    return int(month) == float(month)
try:
	month = int(input("Введите месяц (1-12): "))
except ValueError:
	print ("Вы ввели не верное значение, вычисление не возможно")
	sys.exit()
if (month + abs(month)) == 0:
	print ("Вы ввели отрицательное значение, вычисление не возможно")
	sys.exit()
if str(isInt(month)) == "False":
	print ("Вы ввели не верное значение, вычисление не возможно")
	sys.exit()
	
if is_month_leap (month) == "True":
	print ("Год", month, "високосный")
else:
	print ("Год", month, "не високосный")
