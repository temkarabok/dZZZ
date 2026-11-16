with open('diary.txt', 'w', encoding='utf-8') as f: #открыл файл и записал первые три строки
    f.write("Сегодня мы работали с файлами Python.") #записал первую
    f.write("Научились сохранять текст.") #записал вторую
    f.write("Узнали, как читать данные обратно.") #записал третью

with open('diary.txt', 'a', encoding='utf-8') as f: #открыл снова, чтобы дописать в конец
    f.write("Следующее занятие — CSV и JSON.") #добавил четвертую запись

with open('diary.txt', 'r', encoding='utf-8') as f: #открыл файл на чтение
    text = f.read() #прочитал все содержимое
    print(text) #показал текст

lines = text.strip().splitlines() #разделил текст на строки
print("Количество записей:", len(lines)) #вывел их количество