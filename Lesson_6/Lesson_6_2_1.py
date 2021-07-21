# Первый способ
word = input('Введите слово - ')
new_word = ''
for i in reversed(word):
    new_word = new_word + i
if word == new_word:
    print('Введеное слово является палиндромом!')
else:
    print('Введеное слово НЕ является палиндромом!')