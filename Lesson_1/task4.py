# «разработка», «администрирование», «protocol», «standard»

words = ['разработка', 'администрирование', 'protocol', 'standard']

words_enc = list(map(lambda x: x.encode(), words))
print(*words_enc)
words_dec = list(map(lambda x: x.decode(), words_enc))
print(*words_dec)
