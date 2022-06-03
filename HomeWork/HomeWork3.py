import random
import math
'''
1. Найти НОК двух чисел
'''
def NOD(a, b):
    if a > b:
        min = b
    else:
        min = a
    for i in range (1, min + 1):
        if a % i == 0 and b % i == 0:
            nod = i
    return nod

def NOK(a, b):
    return a * b / NOD(a, b)


'''
2. Вычислить число Пи c заданной точностью d 

Пример: при d = 0.001, c= 3.141.
'''

# Формула нахожения числа Пи (ряд Нилаканта): 
# Пи = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8)
#  - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14) ...


def calculate_pi_accurancy(accurancy):
    pi = 3
    for i in range(2, 100000, 2):
        if i%4 ==0: 
            sing = -1
        else:
            sing = 1
        pi += sing * 4 / (i * (i + 1) * (i + 2))
    return (math.floor(pi/accurancy))*accurancy


'''
3. Составить список простых множителей натурального числа N
'''
def create_list_prime_factors(number):
    list_p_m = []
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            k = 0
            for j in range(2, i // 2 + 1):
                if (i % j == 0):
                    k = k+1
            if (k <= 0):list_p_m.append(i)
    return list_p_m


'''
4. Дана последовательность чисел. 
Получить список неповторяющихся элементов исходной последовательности 

Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
'''

def create_list_unicum_elements(some_list):
    new_list = []
    for el in some_list:
        if el not in new_list: new_list.append(el)
    return new_list


'''
+ на тему файловой системы: 
5. Дан текстовый файл, содержащий целые числа. 
Удалить из него все четные числа.
'''
def create_file_random_number(quantity, file_name):
    with open(file_name, 'w') as data:
        for i in range(101):
            new_data = str(random.randint(0, 100)) + " "
            data.write(new_data)

def print_file_content(file_name):
    print("\nСодержимое файла:")
    data = open(file_name, 'r')
    for line in data:
       print(line)
    data.close()

def delete_even_number_from_file(file_name):
    iter_data = []
    with open("HomeWork3_5.txt",'r') as data:
        for line in data:
            iter_data = [int(x) for x in line.split()]
            new_data = ''
        for el in iter_data:
            if el % 2 != 0: new_data += str(el) + " "
    
    with open(file_name, 'w') as data:
        data.write(new_data)




print("1. Найти НОК двух чисел")
number1 = 34
number2 = 26
print('number1 = ', number1)
print('number2 = ', number2)
print(f'NOK({number1}, {number2})', NOK(number1, number2))
print('-' * 50)



print("2. Вычислить число Пи c заданной точностью d ")
accurancy = 0.001
print('Точность: ', accurancy)
print(calculate_pi_accurancy(accurancy))
#print("---")
#acc = 0.001
#print(math.floor(math.pi/acc)*acc)
print('-' * 50)



print("3. Составить список простых множителей натурального числа N")
n_digit = 87
print("Натуральное число: ", n_digit)
print("список множителей: ", create_list_prime_factors(n_digit))
print('-' * 50)



print("4. Получить список неповторяющихся элементов исходной последовательности")
any_list = [1, 2, 3, 5, 1, 5, 3, 10]
print("Дана последовательность чисел: ", any_list)
print("список неповторяющихся элементов: ", create_list_unicum_elements(any_list))
print('-' * 50)



print("5. Дан текстовый файл, содержащий целые числа.\
        Удалить из него все четные числа.")
# Создаем файл с целыми числами:
file_name = "HomeWork3_5.txt"
create_file_random_number(101, file_name)

# Выведем содержимое файла на экран:
print_file_content(file_name)

# Удаляем четные числа
delete_even_number_from_file(file_name)

# Выведем содержимое файла на экран:
print("\nПосле удаления:")
print_file_content(file_name)
