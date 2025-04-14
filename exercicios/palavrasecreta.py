secret_word = 'pinto'
# i = 1
# new_secret_word = ['*'] * len(secret_word)
# while i <= 6:
#     print('****** Bem vindo ao jogo da palavra secreta ******')
#     letter = input("\nDigite uma letra: ")
#     if len(letter) > 1:
#         print('\nDigite apenas uma letra!')
#         i - 1
#         continue

#     j = 0

#     while j < len(secret_word):
#         if letter == secret_word[j]:
#             new_secret_word[j] = letter
#         j += 1

#     secret_word_string = "".join(new_secret_word)
#     print(f'Palavra secreta: {secret_word_string}')
#     if '*' not in secret_word_string:
#         print("\nParabens voce acertou a palavra secreta")
#         break
#     print(f'Voce ainda tem {6 - i} tentativas')
#     print('')


#     i += 1

# if '*' in secret_word_string:
#     print('Acabaram as tentativas! voce nao acertou a palavra secreta')
#     print(f'A palavra secreta era "{secret_word}"')

i = 1
letters_list = ''

while i <= 8:
    print('\n****** Bem vindo ao jogo da palavra secreta ******')
    letter = input("\nDigite uma letra: ")

    if len(letter) > 1:
        print('\nDigite apenas uma letra!')
        i - 1
        continue

    if letter in secret_word:
        letters_list += letter

    word = ''
    for l in secret_word:
        if l in letters_list:
            word += l
        else:
            word += '*'

    print(word)
    if '*' not in word:
        print('Parabens voce acertou a palavra secreta')
        break
    else:
        print(f'Restam {8 - i} tentativas!')

    i += 1

if '*' in word:
    print('Acabaram as tentativas! voce nao acertou a palavra secreta')
    print(f'A palavra secreta era "{secret_word}"')
