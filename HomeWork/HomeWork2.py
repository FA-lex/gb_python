'''
1. Найти сумму чисел списка стоящих на нечетной позиции
    Пример:[1,2,3,4] -> 4
'''
def sum_odd_position_in_list(any_list):
    sum = 0
    for i in any_list[0::2]:
        sum += i
    return sum

'''
2. Найти произведение пар чисел в списке.
    Парой считаем первый и последний элемент, 
    второй и предпоследний и т.д. 
    
    Пример: [2, 3, 4, 5, 6] => [12, 15, 16];
            [2, 3, 5, 6] => [12, 15]
'''
def product_pair(use_list):
    p_p_list = []
    if len(use_list) % 2 == 0: 
        list_center = len(use_list)//2
    else:
        list_center = len(use_list)//2 + 1
    for e in range(0, list_center):
        p_p_list.append(use_list[e] * use_list[-(e+1)])
    return p_p_list

'''
3. В заданном списке вещественных чисел найдите
    разницу между максимальным и минимальным значением
    дробной части элементов. 

    Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
def difference_fraction(apply_list):
    fract_list = let_fraction(apply_list)
    min_fraction = fract_list[0]
    max_fraction = fract_list[0]
    for e in fract_list:
        if e < min_fraction: min_fraction = e
        if e > max_fraction: max_fraction = e
    return max_fraction - min_fraction

def let_fraction(float_list):
    fraction_list = []
    for i in float_list:
        if (i*10)%10 > 0: fraction_list.append(round((i*10)%10/10, 2))
    return fraction_list
'''
4.Написать программу преобразования десятичного числа в двоичное
'''
def decimal_to_binary(num):
    string_binary_num = ''
    while num > 0:
        string_binary_num = str(num % 2) + string_binary_num
        num = num // 2
    return int(string_binary_num)




print('\n' +'*' * 40)
print("1. Найти сумму чисел списка стоящих на нечетной позиции \n\
Пример:[1,2,3,4] -> 4")
print('-' * 40 + '\n')

my_list = [5, 2, 3, 4]
print(sum_odd_position_in_list(my_list))

print('-' * 40 + '\n')
print('*' * 40)

print("2. Найти произведение пар чисел в списке.\n \
    Парой считаем первый и последний элемент, \n \
    второй и предпоследний и т.д. \n \
    Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; \n \
            [2, 3, 5, 6] => [12, 15]")
print('-' * 40 + '\n')

exempl_list1 = [2, 3, 4, 5, 6]
exempl_list2 = [2, 3, 5, 6]
print(f'Для {exempl_list1} => {product_pair(exempl_list1)}')
print(f'Для {exempl_list2} => {product_pair(exempl_list2)}')

print('-' * 40 + '\n')
print('*' * 40)

print("3. В заданном списке вещественных чисел \n\
     найдите разницу между максимальным и минимальным значением \n\
     дробной части элементов. \n \
     Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19")
print('-' * 40 + '\n')

case_list = [1.1, 1.2, 3.1, 5, 10.01]
diff_fraction = difference_fraction(case_list)
print(diff_fraction)

print('-' * 40 + '\n')
print('*' * 40)

print("4.Написать программу преобразования десятичного числа в двоичное")
print('-' * 40 + '\n')

print(decimal_to_binary(255))

print('-' * 40 + '\n')














'''
Экстра-задачи:
1. Написать программу преобразования двоичного числа в десятичное.

2. Создайте программу, которая будет играть в игру “коровы и быки” с пользователем. Игра работает так:

Случайным образом генерируйте 4-значное число. Попросите пользователя угадать 4-значное число. За каждую цифру, которую пользователь правильно угадал в нужном месте, у них есть “корова”. За каждую цифру, которую пользователь угадал правильно, в неправильном месте стоит “бык”. Каждый раз, когда пользователь делает предположение, скажите им, сколько у них “коров” и “быков”. Как только пользователь угадает правильное число, игра окончена. Следите за количеством догадок, которые пользователь делает на протяжении всей игры, и сообщите пользователю в конце.

3.Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
4. Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
5.2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.Какое самое маленькое число делится нацело на все числа от 1 до 20?
'''