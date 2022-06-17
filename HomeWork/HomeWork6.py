'''
1. Написать программу вычисления арифметического выражения заданного строкой. 
 Используются операции +,-,/,*. приоритет операций стандартный.
 Функцию eval не использовать!

Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;

Дополнительно: Добавить возможность использования скобок,
 меняющих приоритет операций.
 
Пример: 1+2*3 => 7; (1+2)*3 => 9;
'''
OPERATORS = {
    '*': (lambda b, a: a * b),
    '/': (lambda b, a: a / b),
    '+': (lambda b, a: a + b),
    '-': (lambda b, a: a - b)
}

PRIORITY = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0
}

def expression_number(sublist):
    result = ''
    for i in range(len(sublist)):
        if '0' <= sublist[i] <= '9':
            result += sublist[i] 
        else:
            return result

def calculation(math_expression):
    symbols_list = list(math_expression)
    operators_list = []
    numbers_list = []
    position = 0
    while position < len(math_expression):
        if '0' <= math_expression[position] <= '9':
            number = expression_number(symbols_list[position:])
            numbers_list.append(int(number))
            position += len(number)-1
        elif symbols_list[position] == '(':
            operators_list.append('(')
        elif symbols_list[position] == ')':
            while operators_list[-1] != '(':
                numbers_list.append(OPERATORS[operators_list.pop()](numbers_list.pop(),numbers_list.pop()))
            else:
                operators_list.pop()
        elif symbols_list[position] in OPERATORS:
            priority = PRIORITY[symbols_list[position]]
            while len(operators_list) > 0 and priority <= PRIORITY[operators_list[-1]]:
                numbers_list.append(OPERATORS[operators_list.pop()](numbers_list.pop(),numbers_list.pop()))
            operators_list.append(symbols_list[position])
        position +=1
    while len(operators_list) > 0:
        numbers_list.append(OPERATORS[operators_list.pop()](numbers_list.pop(),numbers_list.pop()))
    return numbers_list[0]      

math_expression = '(12+3)*((2+6)/4+((100/2+10)/30-6/2))'  # 15
calc_math = calculation(math_expression)
print(f'{math_expression} = {calc_math}')
print('-'*40)
'''
2. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста).
'''
def encode(text):
    result =[]
    count = 1
    for i in range (len(text)):
        if i == len(text)-1:
            result.append(str(count))
            result.append(text[i])
        elif text[i] == text[i+1]:
            count+=1
        else:
            result.append(str(count))
            result.append(text[i])
            count = 1
    return ''.join(result)

def decode(code_text):
    result = ''
    number = 0
    for i in range(len(code_text)):
        if code_text[i].isdigit():
            number = number * 10 + int(code_text[i])
        else:
            result += code_text[i] * number
            number = 0
    return result

some_text = 'aaaaaaaaaaaaBBBs'
print(f'some_text: {some_text}')

coding_text = encode(some_text)
print(f'coding_text: {coding_text}')

decoding_text = decode(coding_text)
print(f'decoding_text: {decoding_text}')

succes = 'успешно' if some_text == decoding_text else 'с ошибкой'
print(f'кодирование-декодирование прошло {succes}')
print('-'*40)
'''
3. ROT13 - это простой шифр подстановки букв,
 который заменяет букву буквой, которая идет через 13 букв после нее в алфавите.
 ROT13 является примером шифра Цезаря.

Создайте функцию, которая принимает строку и возвращает строку,
 зашифрованную с помощью Rot13 .
 Если в строку включены числа или специальные символы,
 они должны быть возвращены как есть.
 Также создайте функцию, которая расшифровывает эту строку обратно
 (некий начальный аналог шифрования сообщений).

Не использовать функцию encode.'''

def coding(text, code = 'encode'):
    if code == 'encode':
        key = 13
    elif code == 'decode':
        key = -13
    result = ''
    for i in text:
        if i in alfabet:
            result += alfabet[(alfabet.find(i) + key) % len(alfabet)]
        else:
            result += i
    return result

alfabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя-+*/\!"|&?.,%$#@~`№()<>=^1234567890'

some_text = 'Проверяем некий текст на кодирование-декодирование (encode - decode) 06,2022'
print(f'some_text: {some_text}')
coded_text = coding(some_text)
print(f'coded_text: {coded_text}')
decoded_text = coding(coded_text, 'decode')
print(f'decoded_text: {decoded_text}')

succes = 'успешно' if some_text == decoded_text else 'с ошибкой'
print(f'кодирование-декодирование прошло {succes}')