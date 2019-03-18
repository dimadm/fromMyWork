import sys
def bank (a, year):
	i = 1
	while i <= year:
		a = a * (1 + 0.1)
		i += 1
	return a
#------------------------------------------------------------
def isInt(num):
    return int(num) == float(num)
#------------------------------------------------------------
def data (x):
	res = "True"
	try:
		num = int(x)
	except ValueError:
		print ("Вы ввели не верное значение, вычисление не возможно")
		sys.exit()
	if (num + abs(num)) == 0:
		if num != 0:
			print ("Вы ввели отрицательное значение, вычисление не возможно")
			sys.exit()
	if str(isInt(num)) == "False":
		print ("Вы ввели не верное значение, вычисление не возможно")
		sys.exit()
	return res
#------------------------------------------------------------

print ("Введите количество лет: ")
x = input()
if data(x) == "True":
	year = int(x)
print ("Введите сумму: ")
x = input()
if data(x) == "True":
	a = int(x)
print ("Ваш доход: ", bank(a, year))