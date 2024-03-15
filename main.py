import random
from hangman_game import words

print('Temas Disponíveis')
for i in range(len(words)):
    print(f'[ {i + 1} ] {words[i][0]}', sep='')

opcao = int(input('Escolha um tema: ').strip()) - 1

while -1 >= opcao >= len(words):
    opcao = int(input('Escolha uma opção válida: ').strip()) - 1

print('')

theme = words[opcao]
rightWord = theme[random.randint(1, len(theme) - 1)].upper()

wordProgress = ''

for letter in rightWord:
    wordProgress += '_' if letter != ' ' else ' '

gameOver = False
victory = False
attempts = 6
usedLetters = []

# game started
while not gameOver and not victory:
    print(f'Tema: {theme[0]} - Tentativas restantes: {attempts}')

    if len(usedLetters) > 0:
        print(f'Letras incorretas utilizadas: {' - '.join(usedLetters)}')

    print('\n', wordProgress)

    letter = input('Digite uma letra: ').strip().upper()
    while len(letter) > 1:
        letter = input('Digite apenas uma letra: ').strip().upper()

    if letter in rightWord and letter not in wordProgress:
        splitWordProg = list(wordProgress)

        for i in range(len(rightWord)):
            if rightWord[i] == letter:
                splitWordProg[i] = letter

        wordProgress = ''.join(splitWordProg)
    elif letter in wordProgress or letter in usedLetters:
        print('Letra já utilizada')
    else:
        attempts -= 1
        usedLetters.append(letter)

    print()

    gameOver = attempts == 0
    victory = wordProgress == rightWord

if victory:
    print('Parabéns! você venceu!')
else:
    print('Você perdeu!')

print(f'Palavra correta: {rightWord}')