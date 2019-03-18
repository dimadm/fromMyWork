import sys
def arithmetic (x, y, oper):
	if oper == "+":
		res = x + y
	elif oper == "-":
		res = x - y
	elif oper == "*":
		res = x * y
	elif oper == "/":
		res = x / y
	else: res = "Неизвестная операция"
	return res
try:
	x = int(input("Введите первое число: "))
except ValueError:
	print ("Вы ввели не цифровое значение, операция не возможна")
	sys.exit()
try:	
	y = int(input("Введите второе число: "))
except ValueError:
	print ("Вы ввели не цифровое значение, операция не возможна")
	sys.exit()
oper = input("Введите математическую операцию (+-*/): ")

print ("Ответ: ", arithmetic(x, y, oper))

