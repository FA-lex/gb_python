'''
1. Дан список чисел. 
Создать список, в который попадают числа, 
описываемые возрастающую последовательность. 

Пример: [1, 5, 2, 3, 4, 6, 1, 7] 
     => [1, 2, 3] 
    или [1, 7] 
    или [1, 6, 7] и т.д. 

Порядок элементов менять нельзя
'''
# Не понял самого алгоритма, пока что


'''
2. Создать и заполнить файл случайными целыми значениями. 
Выполнить сортировку содержимого файла по возрастанию.
'''
import random
def create_file_random_number(quantity, file_name):
    with open(file_name, 'w') as data:
        for i in range(101):
            new_data = str(random.randint(0, 100)) + "\n"
            data.write(new_data)

def print_file_content(file_name):
    print("\nСодержимое файла:")
    data = open(file_name, 'r')
    for line in data:
       print(line)
    data.close()

def sort_number_in_file(file_name):
    data_from_file = []
    with open(file_name, 'r') as data:
        for line in data:
            data_from_file = [int(x) for x in line.split()]
        new_data = data_from_file.sort()

    with open(file_name, 'w') as data:
        data.write(new_data)
'''def delete_even_number_from_file(file_name):
    iter_data = []
    with open("HomeWork3_5.txt",'r') as data:
        for line in data:
            iter_data = [int(x) for x in line.split()]
            new_data = ''
        for el in iter_data:
            if el % 2 != 0: new_data += str(el) + " "
    
    with open(file_name, 'w') as data:
        data.write(new_data)
'''
file = 'newFile.txt'
create_file_random_number(100, file)
print_file_content(file)
sort_number_in_file(file)

print_file_content(file)

'''
3. Вот вам файл с тысячей чисел. 
    /HomeWork/1Kints.txt

Задача: найти триплеты и просто выводить их на экран. 
Триплетом называются три числа, которые в сумме дают 0. 
(решение будет долгим, ибо является демонстрационным 
при теме многопоточного программирования).
'''

path = '/HomeWork/1Kints.txt'
data = open(path, 'r')
for line in data:
    
    print(line)
data.close()
