# Напишите функцию read_last(lines, file), которая будет открывать определенный файл 
# file и выводить на печать построчно последние строки в количестве lines
#  (на всякий случай проверим, что задано положительное целое число). Протестируем 
#  функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела


 def read_last(lines, file):
   with open(file, 'r', encoding='utf-8') as file:
       text = file.read().splitlines()
        
     for i in range (len(text) - lines, len(text)):
        print(text[i])
def check_for_positive_number(num):
     while num <= 0:
         num = int(input('Пожалуйста, введите положительное число: '))
    return num
 lines = int(input('Введите количество строк, которое хотите увидеть на экране: '))
 read_last(check_for_positive_number(lines), 'article.txt')



# Задание 2: Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# Требуется реализовать функцию longest_words(file),
# которая выводит слово, имеющее максимальную длину
#  (или список слов, если таковых несколько).

def longest_words(file):
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read().split()
    longest_word = text[0]
    for i in range (len(text)):
        if len(text[i]) >= len(longest_word):
            longest_word = text[i]    
    for j in range (len(text)):
        if len(text[j]) == len(longest_word):
            print(text[j])

longest_words('article.txt')





# ДОП ЗАДАЧА.
# Классическая задача про бассейн, который заполняется через 3 трубы, 
# слишком проста. У нас труб будет больше.

# Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена 
# заполнения всего бассейна только одной данной работающей трубой (в часах).
#  Затем после пустой строки перечислены трубы, которые будут заполнять бассейн.
#   Сколько минут на это потребуется?

# Номер трубы соответствует номеру строки, в которой записана ее производительность.

# Результат запишите в файл time.txt

# Пример
# Ввод

# 1
# 2
# 3
# (пустая строка)
# 1 2 3

# Вывод
# 32.72727272727273

Решение:
 def pool(file1, file2):
     with open(file1, 'r', encoding='utf-8') as file:
         pipes_speed = file.read().split('\n') 
     performance = 0
     counter = 0
     working_pipes = list(map(int, pipes_speed [-1].split())) 
     while pipes_speed[counter] != '':
         if counter + 1 in working_pipes:
             performance += 1 / (int(pipes_speed[counter]) * 60)
         counter += 1
     with open(file2, 'w', encoding='utf-8') as result:
         result.write(str(1 / performance))
 pool('pipes.txt', 'time.txt')
