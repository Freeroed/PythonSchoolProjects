#ВАЖНО В КОДЕ В < > БУДУ ОСТАВЛЯТЬ ОПИСАНИЕ ТОГО, ЧТО ДОЛЖНО БЫТЬ НА ЭТОМ МЕСТЕ В КОДЕ
#Создание переменных и типы данных
num=10 #Целочисленный тип данных
fl = 1.5 # Число с плавающей точкой
word="hello" #Строковый тип данных
bit=True #Логический тип данных

#Строку можно умножить на число и получить повторение этой строки

#Написание условия
#if (<Логическое выражение или переменная типа Boolean (True/False)>) :
    #Ваш блок кода с отступом
#Логичекие операции 
# Равно ==
# Больше >      Меньше <
# Больше или равно =>    Меньше или равно <=
# И and
# ИЛИ or

#Вывод на экран     print(<Выражение для вывода (переменная или строка)>)
print("this is string")
print(num)

#Ввод данных с клавиатуры   <переменная> =  input(<Сообщение для пользователя>)
testint = input("Введи число")
#По умолчанию вводится строка. Если Нужно ввести число и работать с ним как с числом, выполняется преобразование типа 
testint = int(input()) #К целочисленному типу
testfl = float(input()) #К числу с плавающей точкой

#Пример
print("Пример на условие")
if (num == 10):
    print("Yes")
else:
    print("NO")

#Несколько условий

#if(<Условие>):
    #Действия
#elif(<Другое условие>)
    #Двугое действие

#Пример
print("Пример на несколько условий")
if(fl == 1.5):
    print("python top")
elif (fl==4.2):
    print("Python top anyway")

#Циклы
# Цикл со счётчиком
# for <название переменной> in <Интервал изменения>:
    #Блок кода

#Например. Вывод чисел от 0 до 10
print("Пример на цикл")
for i in range(10):
    print(i)

#Про функцию range. Принимает до трёх параметров
#range(<конец интервала>)
#range(<Начало интервала>, <Конец интервала>)
#range(<Начало интервала>, <Конец интервала>, <Шаг>)

print('Пример на Range со всем параметрами')
for j in range(0,100,5):
    print(j)

#Цикл с условием будет выполняться пока действительно условие (ОСТОРОЖНО, МОЖНО СДЕЛАТЬ БЕСКОНЕЧНЫМ)
#while (<Условие>):
    #Блок кода

#Пример
print("Пример на while")
temp1 = 10
temp2 = 50
while(temp2>temp1):
    temp2-=8
    print(temp2+temp1)
#Таким образом, пока temp2 будет больше temp1, из ней будет вычитаться 8 и выводиться результат на экран

#Массивы (Далее будем называть их списками, так как в питоне нет как такогового понятия массива)
#<Название> = [<Элемент0>, <Элемент1>.....]
print("Исходный список")
arr = [1,4,5,6,7]
#Простейший вывод на экран
print(arr)

#Операции над списками проводятся через цикл
#Например вывод на экран построчно
for i in arr:
    print(i)
#В данной ситуации в переменную i будут помещаться по очереди значения элемента списка и выводиться на экран
#Но, если мы попробуем таким образом изменить значение элементов списка, у нас ничего не выйдет
print("Пробудем поменять значения списка")
for i in arr:
    i+=2
print (arr)
print("Толку 0")
#В таком случае, нам нужно обрачаться к элементам списка по индексу  <имя списка>[<Индекс>]
#Нам поможет функиця len(<имя списка>) которая возвращает нам количество  элементов в списке
print("Вот теперь значения изменились")
for i in range(len(arr)):
    arr[i]+=1
print(arr)

#Некоторые функции для работы со списком
#<Имя списка>.append(<Элемент>)   добавление элемента в конец списка
arr.append(100)
print(arr)
#<Имя списка>.remove(<Элемент>)   удаление первого попавшегося элемента 
arr.remove(7)
print(arr)
#<Имя списка>.insert(<Идекс>, <Элемент>)  Добавление нового элемента на позицию с заданным индексом
arr.insert(3, 1233)
print(arr)
#<Имя списка>.count(<Элемент>)   Считаем, сколько раз втречается элемент 
print(arr.count(1233))
#<Имя списка>.sort()    Сортировка списка (по возрастанию)
arr.sort()
print(arr)
#<Имя списка>.reverse()   Список в обратном порядке
arr.reverse()
print(arr)

#Списки можно объединять простым сложением <Список3> =<Список1>+<Список2>

#Подпрограмы
#Описание подпрограммы начинается со слова def <Название процедуры>(<Входные параметры(не обызательно)>):
    #Блок кода подпрограммы

#После этого подпрограмму можно вызвать по названию

#<Название>

#Пример
def printing(word):
    for i in word:
        print(i)


#Теперь её можно вызвать
printing("ПИТОН")

#Чтобы сохранить значения, полученные в результате выполения подпрограммы, необходимо описать return. Как только Подпрограмма доходит до этого слова,
#Она останавливает своё выполение о возвращает результат

def couting(arr):
    result = 0 
    for i in arr:
        result+=i
    return result

cnt = couting(arr)
#Но сейчас мы не увидим результат работы программы. Нужно Результат вывести на экран
print(cnt)