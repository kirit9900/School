def deq(a,de,b):
    if de =="плюс" or de == "+":
        return a+b
    if de =="минус" or de == "-":
        return a-b
    if de =="умножение" or de == "*":
        return a*b
    if de =="/":
        return a/b
    if de =="//":
        return a//b






print("Привет,ты попал в калькулятор)Давай посчитаем")
cou = int(input('Введи количество чисел от двух до бесконечности:'))
for i in range(cou+1):
    if cou == 2:
        one = int(input('Первое число:'))
        d = input('Введи действие:')
        two = int(input('Второе число:'))




