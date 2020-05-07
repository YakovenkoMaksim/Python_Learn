#  Задание 3
# Создайте программу-калькулятор, которая поддерживает четыре операции: сложение,
# вычитание, умножение, деление. Все данные должны вводиться в цикле, пока пользователь не
# укажет, что хочет завершить выполнение программы. Каждая операция должна быть
# реализована в виде отдельной функции. Функция деления должна проверять данные на
# корректность и выдавать сообщение об ошибке в случае попытки деления на ноль.

#Функция деления
def division(x, y):
  if y != 0:
    div = x / y
    print('Деление ', x, ' на ', y, ' = ', div)
    print()  
  else:
    print('Деление на 0 не возможно!')
    print()

#Функция умножения
def multiplication(x, y):
  mult = x * y
  print('Умножение ', x, ' на ', y, ' = ', mult)
  print()

#Функция вычитания
def subtraction(x, y):
  sub = x - y
  print('Вычитание ', x, ' из ', y, ' = ', sub)
  print()

#Функция сложения
def addition(x, y):
  add = x + y
  print('Сумма ', x, ' и ', y, ' = ', add)
  print()


while True:
  x = float(input('Введи первое число: '))
  y = float(input('Введи второе число: '))
  print()
  print('Выберите, пожалуйста, операцию: ')
  print('1. Деление')
  print('2. Умножение')
  print('3. Вычитание')
  print('4. Сложение')
  print('0. Выйти из калькулятора')
  print()
  
  operation = int(input('Введите номер операции над числами: '))
  print()

  if operation == 1:
    division(x ,y)
    continue

  elif operation == 2:
    multiplication(x, y)
    continue
  
  elif operation == 3:
    subtraction(x, y)
    continue

  elif operation == 4:
    addition(x, y)
    continue

  elif operation == 0:
    break

  else:
    print('Вы выбрали не верную операцию!')
    continue