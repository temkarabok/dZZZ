import csv #подключил модуль для работы с csv

with open('purchases.csv', 'w', encoding='utf-8', newline='') as f: #создал файл
    w = csv.writer(f, delimiter=';') #настроил запись через точку с запятой
    w.writerow(["Товар", "Цена за штуку", "Количество"]) #записал шапку
    w.writerow(["Тетрадь", "2.50", "4"]) #записал тетради
    w.writerow(["Ручка", "1.20", "3"]) #записал ручки
    w.writerow(["Папка", "4.00", "2"]) #записал папки
    w.writerow(["Маркер", "3.30", "1"]) #записал маркер

total = 0 #завел переменную для итога
with open('purchases.csv', 'r', encoding='utf-8') as f: #открыл файл для чтения
    r = csv.reader(f, delimiter=';') #настроил чтение
    next(r) #пропустил шапку
    for row in r: #прошел по строкам
        name = row[0] #взял название
        price = float(row[1]) #взял цену и перевел в число
        count = int(row[2]) #взял количество и перевел в число
        
        cost = price * count #посчитал стоимость позиции
        total += cost #добавил к общему итогу
        print(name, price, count) #вывел данные товара

print("Итог:", total) #показал общую сумму