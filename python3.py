try:
	x  = int ( input ("Введите значение размера стороны квадрата: "))
except ValueError:
	x = 0
	print ("Вы ввели ерунду ")
def square (x):
	p = x * 4
	s = x ** 2
	d = (2 * (x ** 2)) ** 0.5
	d = float('{:.2f}'.format(d))
	res = (p, s, d)
	return res
if x > 0:
	print ("При стороне квадрата: ", x)
	print ("Периметр, Площадь и Диагональ соответственно равны: ", square (x))
else: 
	print ("Не верное значение, попробуйте ещё раз")
