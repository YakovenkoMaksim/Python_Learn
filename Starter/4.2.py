# Задание 2
# Факториалом числа n называется число n! = 1 * 2 * 3 * ... * n. Создайте программу, которая
# вычисляет факториал введённого пользователем числа.

# Вариант 1

print('Давайте найдём факториал целого числа!')
number = int(input('Введите целое число: '))
factorial = 1

if number:
    for i in range(2, number+1):
        factorial *= i
    print('Факториал числа ', number,'! = ', factorial, sep='')

else:
    print('Введите корректное значение')

# Вариант 2

import math

x = int(input('Input integer: '))

if x > 0:
  print('Factorial ', x, '! = ', math.factorial(x), sep = '')
else:
  print('Your number no correct!')