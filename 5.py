#Калькулятор


from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print( Fore.MAGENTA )

print( Back.WHITE )

what = input( "Что делаем? (+, -, *, /): " )

a = float(input("Введите первое число: ") )
b = float(input("Введите второе число: ") )

if what == "+":
	c = a + b
	print("Результат: " + str(c))

elif what == "-":
	c = a - b
	print("Результат: " + str(c))

elif what == "*":
	c = a * b
	print("Результат: " + str(c))

elif what == "/":
	c = a / b
	print("Результат: " +str(c))

else: 
	print("Выбрана неверная операция! ")

input()
