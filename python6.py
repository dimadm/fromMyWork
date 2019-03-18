import sys
def is_prime (i):
	if i < 10:
		res = "True"
	else:
		res = "False"
	return res
#------------------------------------------------------------
i = 0
while  i <= 1000:
	if is_prime (i) == "True":
		print ("Число ", i, "простое")
		i += 1
	else:
		print ("Число ", i, "составное")
		i += 50
	