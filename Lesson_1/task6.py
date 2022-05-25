words = ["сетевое программирование", "сокет", "декоратор"]
f_n = open("test.txt", "w")
for word in words:
    f_n.write(f"{word}\n")
f_n.close()
print(f_n.encoding)


f_n = open("test.txt", "r", encoding='UTF-8')
print(f_n.read())
f_n.close()
