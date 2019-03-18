import sys
def is_year_leap (year):
	if (year % 4) == 0:
		res = "True"
	else: res = "False"
	return res
def isInt(year):
    return int(year) == float(year)
try:
	year = int(input("Введите год: "))
except ValueError:
	print ("Вы ввели не верное значение, вычисление не возможно")
	sys.exit()
if (year + abs(year)) == 0:
	print ("Вы ввели отрицательное значение, вычисление не возможно")
	sys.exit()
if str(isInt(year)) == "False":
	print ("Вы ввели не верное значение, вычисление не возможно")
	sys.exit()
	
if is_year_leap (year) == "True":
	print ("Год", year, "високосный")
else:
	print ("Год", year, "не високосный")
