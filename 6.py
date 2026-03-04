#Вариант 1  
#Дана строка, содержащая русскоязычный текст. Найти количество слов, 
#начинающихся с буквы "е".  

string = input()
words = string.split()
count = 0

for word in words:
    if word[0].lower() == 'е': count += 1

print(count)

#Вариант 2  
#В строке заменить все двоеточия (:) знаком процента (%). Подсчитать количество 
#замен.

string = input()
count = string.count(':')
string = string.replace(':', '%')
print(string, count)
  
#Вариант 3  
#В строке удалить символ точку (.) и подсчитать количество удаленных символов.  

string = input()
count = string.count('.')
string = string.replace('.', '')
print(string, count)

#Вариант 4  
#В строке заменить букву(а) буквой (о). Подсчитать количество замен. 
#Подсчитать, сколько символов в строке.

string = input()
count = string.count('а')
string = string.replace('а', 'о')
print(string, count, len(string))
 
#Вариант 5  
#В строке заменить все заглавные буквы строчными.  

string = input()
string = string.lower()

#Вариант 6  
#В строке удалить все буквы "а"  и подсчитать количество удаленных символов.  

string = input()
count = string.count('а')
string = string.replace('а', '')
print(string, count)

#Вариант 7  
#Дана строка. Преобразовать ее, заменив звездочками все буквы "п", 
#встречающиеся среди первых n/2 символов. Здесь n - длина строки.  

string = input()
length = len(string) // 2

string = string[:length].replace('п', '*') + string[length:len(string)]
print(string)

#Вариант 8  
#Дана строка, заканчивающаяся точкой. Подсчитать, сколько слов в строке.  

string = input()
print(len(string.split()))

#Вариант 9  
#Определить, сколько раз в тексте встречается заданное слово.  

string = input()
word = input()
count = [w for w in string.split() if w == word]
print(len(count))

#Вариант 10  
#Дана строка-предложение на английском языке. Преобразовать строку так, 
#чтобы каждое слово начиналось с заглавной буквы. 

string = input()
new_string = []
for word in string.split():
    new_string.append(word[0].upper())
    
string = new_string.join(' ')

# Вариант 11  
#Дана строка. Подсчитать самую длинную последовательность подряд идущих 
#букв «н». Преобразовать ее, заменив  точками все восклицательные знаки.  

string = input()
sym = 'н'
count = 0
max_count = 0

for s in string:
    if s == sym:
        count += 1
        if count > max_count: max_count = count
    else:
        count = 0
        
string = string.replace('!', '.')
print(string, max_count)

#Вариант 12  
#Дана строка. Вывести все слова, оканчивающиеся на букву "я".  

string = input()
for word in string.split():
    if word[-1] == 'я': print(word)

#Вариант 13  
#Дана строка символов, среди которых есть одна открывающаяся и одна 
#закрывающаяся скобки. Вывести на экран все символы, расположенные внутри 
#этих скобок.  

string = input()
ind1 = string.index('(')
ind2 = string.index(')')

print(string[ind1+1:ind2])

#Вариант 14  
#Дана строка. Вывести все слова, начинающиеся на букву "а" и слова 
#оканчивающиеся на букву "я".  

string = input()
for word in string.split():
    if word.startswith('а') or word.endswith('я'): 
        print(word)

#Вариант 15  
#Дана строка текста. Подсчитать количество букв «т» в строке. 

string = input()
print(string.count('т'))
