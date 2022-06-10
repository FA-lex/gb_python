'''
1. Напишите программу, удаляющую из текста
 все слова содержащие "абв", которое регистронезависимо.
 Используйте знания с последней лекции. 
 Выполните ее в виде функции.

 Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»
'''
def del_substring(any_string, substring):
    string_to_list = any_string.split(' ')
    result_list = list(filter(lambda word: substring.lower() not in word.lower(), string_to_list))
    return ' '.join(result_list)

our_text = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк'
delete_text = 'абв'
print(del_substring(our_text, delete_text))


'''
2. Вы когда-нибудь играли в игру "Крестики-нолики"
 Попробуйте создать её, причем чтобы сыграть в нее 
 можно было в одиночку.
'''
def make_area(area):
    for i in range(3):
        print ('-' * 13)
        print ('|', area[0+i*3], '|', area[1+i*3], '|', area[2+i*3], '|')
    print ('-' * 13)

def motion(symbol_player):
    valid = False
    while not valid:
        move = int(input(f'Ход игрока: {symbol_player}, выберите клетку '))

        if 1 <= int(move) <= 9:
            if (str(area[move-1]) not in "XO"):
                area[move-1] = symbol_player
                valid = True
            else:
                print ('Сюда уже ходили')
        else:
            print ('Некорректный ввод. Введите число от 1 до 9')

def win_combo(area):
    combination = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for combo in combination:
        if area[combo[0]] == area[combo[1]] == area[combo[2]]:
            return area[combo[0]]
    return False

def game_xo(area):
    count = 0
    win = False
    while not win:
        make_area(area)
        if count % 2 == 0:
            motion('X')
        else:
            motion('O')
        count += 1
        if count > 4:
            player = win_combo(area)
            if player:
                print (f'Игрок: {player}, выиграл!!!')
                win = True
                break
        if count == 9:
            print (';-)  Ничья!!!')
            break
    make_area(area)

area = list(range(1,10))
game_xo(area)


'''
3. Вот вам текст:
 «Ну, вышел я, короче, из подъезда. 
 В общем, короче говоря, шел я, кажется, в магазин. 
 Ну,эээ, в общем, было лето, кажется. Как бы тепло.
 Солнечно, короче. 
 Иду я, иду, в общем, по улице, а тут, короче, яма. 
 Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. 
 Ясен пень, в магазин. 
 В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. 
 Кстати, иду я по улице, иду, а тут, короче, яма. 
 Ну, я в нее упал, в общем. Вышел из подъезда, короче. 
 Лето на дворе, ясен пень. Птицы поют, короче, солнечно. 
 В общем, в магазин мне надо. Что-то явно не так, короче. 
 «Рекурсия», - подумал я. 
 Ээээ...короче, в общем, пошел другой дорогой и не упал 
 в эту… ээээ… яму. Хлеба купил».

Отфильтруйте его, чтобы этот текст можно было нормально прочесть.
Предусмотрите вариант, что мусорные слова могли быть 
написаны без использования запятых.'''

def delete_trash(interim_text, trash_words):
    for trash in trash_words:
        interim_text = interim_text.casefold().replace(trash, '_')

    interim_text = interim_text.replace('я,','я')\
                                .replace('_','')\
                                .replace('  ',' ')\
                                .split('.')

    sentences = []
    for sentence in interim_text:
      sentence = sentence.strip()
      if not sentence: continue
      sentences.append(sentence.capitalize())

    result_text = '. '.join(sentences) + '.'
    return result_text


text = 'Ну, вышел я,  из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем.Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо.Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил'
trash_words = ['ну', 'В общем', 'короче говоря', 'кажется', 'иду я','ээ','_э' ,'короче,', ',кажется', 'в общем', 'ясен пень', 'как бы', 'кстати', 'короче', '... ,', '….','…', '...',', ,', ', _', '_,' ]

print(delete_trash(text, trash_words))

