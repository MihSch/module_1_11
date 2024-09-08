             #ФУНКЦИИ
# def say_hello():    # def используется для определения функции define
#     print('Hello')  # это ОБЫЧНАЯ функция
#
#
#
# say_hello() #вызвали
# say_hello()
# say_hello()


# def say_hello(name):       # ПРИНИМАЮЩАЯ функц
#     print('Hello', name)
#
#
# say_hello('leha')
# say_hello('leh')
# say_hello('le')


# import random #библиотека рандом  .choice это метод который выбирает случ элемент
# def lottery():       # ВОЗВРАЩАЮЩАЯ функц
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win = random.choice(tickets)
#     return win #return прекращает выполнение данной команды
#
# win = lottery() + lottery() # cоздали переменную для того чтобы вывести
# print(win)


# import random
# #def lottery(mon,thue):      #одновременно ПРИНИМАЮЩАЯ и ВОЗВРАЩАЮЩАЯ ФУН
# def lottery(*args, **kwargs):  # если не знаем сколько фун будет принимать параметров
# # *args для обычных параметров и **kwargs для именованных параметров
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     tickets.remove(win1) # чтобы не было одинаковых номеров
#     win2 = random.choice(tickets)
#     #print(mon, thue)
#     print(*args)
#     return win1, win2
#
#
# #win1, win2 = lottery('mon','thue')
# win1, win2 = lottery(1,12,2,3,5) # с args сюда можно писать что угодно
# print(win1, win2)


    #В принимающих функциях мы можем задавать значение по умолчанию
# def test(a=2, b=True): # задали параметры сразу
#     print(a, b)
#
# test(False, 'ok') # можем задавать параметры тут



        # можем распаковать словарь или список
# def test(a=2, b=True):
#     print(a, b)
#
#
# test(*{'ffg': 2, 'ggh': 2}) # встал на место параметра a /вывод [1, 2] True
#   * - для распаковки / вывод 1 2
# можно это делать и со словарями то нужно учесть что количество ключей должно быть 2
# **- для распаковки словаря


                 #ЗАДАЧА

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)