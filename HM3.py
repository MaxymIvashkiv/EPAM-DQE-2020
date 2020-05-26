import collections, re

# функція повертає наймовірнішу літеру для такої позиції при такій спробі
# Спроба означає, для прикладу спроба №1 - бере наймовірнішу букву 30%, спроба №2 другу за ймовірністю - 20%. і так далі
# тобто функція перебирає усі літери на першій/другій/третій/і так далі позиції слова і вираховує їхню ймовірність
def character_frequency(word_list, char_position, move):
    check_list = list()
    for element in word_list:
        check_list.append(element[int(char_position)])
    most_common_character = collections.Counter(check_list).most_common()[move]
    total = sum(collections.Counter(check_list).values())
    frequency = most_common_character[1] / total
    return most_common_character[0], frequency


def game_result(character_list, new_char, char_position, required_change):
    if required_change:
        character_list[char_position] = new_char
    result = ''
    for element in character_list:
        result += str(element) + ' '
    print('_' * 60)
    print(' ' * 60)
    print(result)
    print(' ' * 60)

print('='*10 + 'GAME STARTED' + '='*10)
word = input('Please enter your word: ')
word_len = len(word)
# додає у список слів лише ті слова довжина яких рівна заданому слову
words = [el for el in re.findall('(\S+)\n', open(f"words.txt", "r", encoding="utf-8").read()) if len(el) == word_len]
word_board = list('_' * word_len)
char_position = 0
turn = 0

game_result(word_board, 'Start game', 0, False)
attemp = 0

while char_position < word_len:
    attemp += 1
    # якщо помилка IndexError, то комп'ютер перепробував усі літери на такій позиції у ймовірних словах. Тобто можливі букви закінчились
    try:
        character = character_frequency(words, char_position, turn)[0]
        frequency = str(character_frequency(words, char_position, turn)[1] * 100)[0:5] + '%'
    except IndexError:
        print(f'You cheated me. I tried all letters at {char_position+1}th position. There is no any words like this.')
        break
    print(f'Attemp №{attemp}\nProbability is {frequency} that "{character}" is your letter at position {char_position+1}')
    question = input('Do you agree with me? - Y/N: ')
    if question == 'Y':
        game_result(word_board, character, char_position, True)
        # перезаписує список вибираючи лише слова з вірними буквами на позиціях
        stage_list = words.copy()
        words.clear()
        words = [element for element in stage_list if character in element[char_position]]
        if len(words) == 0:
            print('You cheated. There is no any words like this')
            game_result(word_board, character, char_position, True)
            break
        char_position += 1
        turn = 0
        continue
    elif question == 'N':
        game_result(word_board, character, char_position, False)
        turn += 1
        continue
    else:
        print('Choose right option')
        continue
if char_position == word_len:
    guessed_word = words[0]
    if guessed_word == word:
        print(f'I attempted {attemp} times and guessed. "{guessed_word}" should be your word.')
    else:
        print(f'You fooled me once. I guessed another word "{guessed_word}" instead of "{word}"')
