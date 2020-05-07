# Задание 2
# Создайте две функции, вычисляющие значения определённых алгебраических выражений.
# Выведите на экран таблицу значений этих функций от -5 до 5 с шагом 0.5.
# 1) (x - 2) / (x + 2)
# 2) 3 / (5 - |x|)

def first_function(a, b):
  print('Выражение (x - 2) / (x + 6)')
  print()
  for i in range(a, b):
    formula_1 = (i - 2) / (i + 6)
    print('При x =', i, 'Выражение равно =', formula_1, sep = '\t') 
    print()


def second_function(a, b):
  print('Выражение 3 / (6 - |x|)')
  print()
  for i in range(a, b):
    formula_2 = 3 / (6 - abs(i))
    print('При x =', i, 'Выражение равно =', formula_2, sep = '\t')
    print()

first_function(-5, 5)
second_function(-5, 5)