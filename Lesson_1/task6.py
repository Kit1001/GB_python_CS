import chardet

f_n = open("test_file.txt", "rb")
print(chardet.detect(f_n.read())['encoding'])
f_n.close()


f_n = open("test_file.txt", "r", encoding='UTF-8', errors='replace')
print(f_n.read())
f_n.close()
