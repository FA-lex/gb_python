'''
1. Сформировать список из N членов последовательности. 
   Для N = 5: 1, -3, 9, -27, 81 и т.д.
'''

def create_list(n):
   new_list = [1]
   for i in range(1, n):
      new_list.append(new_list[i-1] * -3)
   return new_list

'''
2. Для натурального n создать словарь индекс-значение,
   состоящий из элементов последовательности 3n + 1.
   Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
'''
'''-----------------------------------------------------------'''
'''--Так не честно! Про словари рассказали на второй лекции.--'''
'''-----------------------------------------------------------'''

def create_dict_3N_plus_1(n):
   new_dict = {}
   for i in range(1, n+1):
      new_dict[i] = 3 * i +1
   return new_dict

'''
3. Пользователь задаёт две строки.
   Определить количество вхождений одной строки в другой.
'''
def find_inclusion(string_1, string_2):
   if len(string_1) < len(string_2):
      short_string = string_1
      large_string = string_2
   else:
      short_string = string_2
      large_string = string_1
   count = 0
   for s in range(len(large_string) - len(short_string) + 1):
      if short_string in large_string[s: s + len(short_string)]:
         count += 1

   return count

'''
4. Подсчитать сумму цифр в вещественном числе.
'''
def sum_digit_float(num):
   sum = 0
   for e in str(num):
      if e != "-" and e != "." and e != ",":
         sum += int(e)
   return sum


'''
5. Написать программу получающую набор произведений чисел от 1 до N.
   Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
'''
def product_numbers_list(number):
   p_n_list = [1, 2]
   for i in range(2, number + 1):
      p_n_list.append(p_n_list[i - 1] * i)
   return p_n_list



print('\n' +'*' * 40)

print("1. Сформировать список из N членов последовательности. \n \
          Для N = 5: 1, -3, 9, -27, 81 и т.д.")

print('-' * 40 + '\n')

print(create_list(5))

print('\n' +'*' * 40)

print("2. Для натурального n создать словарь индекс-значение,\
   состоящий из элементов последовательности 3n + 1.\
   Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}")

print('-' * 40 + '\n')

print(create_dict_3N_plus_1(6))

print('\n' +'*' * 40)

print("3. Пользователь задаёт две строки.\n\
   Определить количество вхождений одной строки в другой.\n\
   например:   1: this is a collision \n\
               2: is \n\
   ответ: 3")

print('-' * 40 + '\n')
'''
print('Введите две строки')
user_string_1 = input('1: ')
user_string_2 = input('2: ')
print(f'вхождений: {find_inclusion(user_string_1, user_string_2)}')
'''
print('\n' +'*' * 40)

print("4. Подсчитать сумму цифр в вещественном числе.")

print('-' * 40 + '\n')

float_number = -0.1234
print(f'Сумма цифр в числе: {sum_digit_float(float_number)}')

print('\n' +'*' * 40)

print("5. Написать программу получающую набор произведений чисел\
    от 1 до N.    \n\
   Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]")

print('-' * 40 + '\n')

N = 4
print(f'Набор произвдений чисел от 1 до N: {product_numbers_list(N)}')

print('-' * 40 + '\n')
