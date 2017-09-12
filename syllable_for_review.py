import random
import csv
from collections import Counter


'''
basic variables:
    current_letter_number - current letter in cicle "for"
                            inside function get_word_by_syllable
    letter_number - len of variable "word"
    word - sum of syllables
    word_by_syllable_temp - list of syllables
    word_by_letters - incoming word divided by letters
    syllable_params - list, include:
                                   [0] - current syllable
                                   [1] - previous_syllable
                                   [2] - index of current syllable in word
                                   [3] - number of syllables in word
                                   [4] - how often this set of parameters
                                         of syllable is postponed
    counted_idex_table - table include syllable_params[4] element
word by syllable conditions:
                            first condition: v|v,
                            second condition: v|cv,
                            third condition: vc|c...cv,
                            where v - vowel, c - consonant
'''


'''
function gets word_by_lettersm, letter_number, current_letter_number
return syllable like 'па'
'''
def obtain_syllable(letter_number, current_letter_number,
                    word_by_letters, third_condition=False):
    syllable = ''
    sign = ['ь', 'ъ']
    if third_condition == False:
        for current_letter_number_temp in range(letter_number, current_letter_number + 1):
            syllable += word_by_letters[current_letter_number_temp]
        if word_by_letters[current_letter_number + 1] in sign:
                syllable += word_by_letters[current_letter_number + 1]
    else:
        for current_letter_number_temp in range(letter_number, current_letter_number + 2):
            syllable += word_by_letters[current_letter_number_temp]
        if word_by_letters[current_letter_number + 2] in sign:
                syllable += word_by_letters[current_letter_number + 2]
    return syllable


'''
function return word_by_syllable with appended syllable
example: ['при'] - incoming word_by_syllable, 'вет' - obtained syllable
return ['при', 'вет']
'''
def record_of_syllable(letter_number, current_letter_number, word_by_letters,
                       word, word_by_syllable_temp, third_condition=False):
    syllable = obtain_syllable(letter_number, current_letter_number,
                               word_by_letters, third_condition)
    word += syllable
    letter_number = len(word)
    word_by_syllable_temp.append(syllable)
    return letter_number, current_letter_number, word_by_syllable_temp, word


'''
function handles the last unprocessed letters, if any
example: word_by_letters - ['б', 'л', 'е', 'д', 'н', 'о', 'с', 'т', 'ь', 'а', 'б']
after execution of the main part word_by_syllable = ['блед', 'нос']
letter_number = 7, len(word_by_letters) - 2 = 9
return ['блед', 'ность']
'''
def last_letters_handler(letter_number, word_by_letters,
                         word_by_syllable_temp, vowel):
    for current_letter_number in range(letter_number, len(word_by_letters) -2):
            word_by_syllable_temp[-1] += word_by_letters[current_letter_number]
    return word_by_syllable_temp


'''
function passes through each letter of the word
checks the fulfillment of word by syllables conditions for decomposition incoming word
if the condition is satisfied, then syllable are constructed
word_incoming = 'привет'
return ['при', 'вет']
'''
def get_word_by_syllable(word_incoming,word_by_syllable_temp=[],
                         letter_number=0, word=''):
    word_by_letters = list(word_incoming) + ['а', 'б']
    if '-' in word_by_letters:
        return None
    else:
        vowel = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
        for current_letter_number in range(0, len(word_by_letters) - 2):
            if word_by_letters[current_letter_number] in vowel and \
               word_by_letters[current_letter_number + 1] in vowel:
                letter_number, current_letter_number , word_by_syllable_temp, word = \
                record_of_syllable(letter_number, current_letter_number, word_by_letters,
                                      word, word_by_syllable_temp)

            elif  word_by_letters[current_letter_number] in vowel and \
                  word_by_letters[current_letter_number + 1] not in vowel and \
                  word_by_letters[current_letter_number + 2] in vowel:
                letter_number, current_letter_number , word_by_syllable_temp, word = \
                record_of_syllable(letter_number, current_letter_number, word_by_letters,
                                      word, word_by_syllable_temp)

            elif word_by_letters[current_letter_number] in vowel and \
                 word_by_letters[current_letter_number + 1] not in vowel and \
                 word_by_letters[current_letter_number + 2] not in vowel:
                letter_number, current_letter_number , word_by_syllable_temp, word = \
                record_of_syllable(letter_number, current_letter_number, word_by_letters,
                                      word, word_by_syllable_temp, third_condition=True)
        word_by_syllable_temp = last_letters_handler(letter_number, word_by_letters,
                                                     word_by_syllable_temp, vowel)
        return word_by_syllable_temp


'''
function gets parametrs of syllable(see the top)
word_by_syllable_temp = 'привет'
return [('при', 'BEG', 0, 2), ('вет', 'при', 1, 2)]
'''
def obtain_syllable_parameters(word_by_syllable_temp):
    syllable_params = []
    if word_by_syllable_temp:
        for syllable in word_by_syllable_temp:
            previous_syllable = word_by_syllable_temp[word_by_syllable_temp.index(syllable) - 1] \
            if word_by_syllable_temp.index(syllable) > 0 else 'BEG'
            syllable_params.append((syllable, previous_syllable,
                                   word_by_syllable_temp.index(syllable),
                                   len(word_by_syllable_temp)))
        return syllable_params


'''
function reads from csv dictionary words, then gets words by syllables,
next step is obtain syllable_params for each syllables
last step is count same syllables
return counted_index_table
'''
def get_index_table(file_read='freqrnc2011.csv', ):
    with open(file_read, 'r', encoding='utf-8') as f:
        syllable_list = []
        fields = ['word', 'PoS', 'Freq', 'R', 'D', 'Doc']
        reader = csv.DictReader(f, fields, delimiter='	')
        print('loading...')
        for row in reader:
            try:
                syllable_params = []
                if list(row.get('word'))[0] != list(row.get('word'))[0].upper():
                    word_by_syllable = get_word_by_syllable(row.get('word'), [])
                    syllable_params = obtain_syllable_parameters(word_by_syllable)
                    if syllable_params:
                        syllable_list += syllable_params
            except IndexError:
                nothing_to_do = True # exceptions occurs when no vowel in word
    raw_index_table = Counter(syllable_list)
    counted_idex_table = []
    for key in raw_index_table:
        temp = list(key)
        temp.append(raw_index_table[key])
        counted_idex_table.append(temp)
    return counted_idex_table


def write_index_table_to_file(count, file_write):
    with open(file_write, 'w', encoding='utf-8') as f:
        for key in count:
            temp = list(key)
            temp.append(count[key])
            f.write(str(temp).strip('[').strip(']') + '\n')


def reade_index_table_from_file(file_read):
    syllable_list = []
    with open(file_read, 'r', encoding='utf-8') as f:
        for line in f:
            syllable_list.append(f.readline)
    return syllable_list


'''
from counted_index_table function selects syllables according to the rules
return pseudo-russian word
'''
def pseudo_word_generator(counted_index_table=get_index_table()):
    print('\nВас приветствует генератор псевдо русских слов!')
    while True:
        pseudo_word = ''
        number_of_syllables = input('Введите число слогов в слове или exit для выхода.\n> ')
        if number_of_syllables =='exit':
            break
        try:
            top_percent = float(input('Ведите число для отбора первых U% слогов. (Например: 20).\n> '))*0.01
            previous_syllable = 'BEG'
            for syllable_index in range(0, int(number_of_syllables)):
                syllable_list = []
                for syllable_params in counted_index_table:
                    if syllable_params[1] == previous_syllable and \
                       syllable_params[2] == syllable_index and \
                       syllable_params[3] == int(number_of_syllables):
                        syllable_list.append(syllable_params)
                syllable_list.sort(key=lambda syllable_temp: syllable_temp[-1], reverse=True)
                top_syllables = syllable_list[:int(len(syllable_list)*top_percent)]
                syllable = ''
                selected_syllable = top_syllables[random.randint(0, len(top_syllables) - 1)]
                syllable = selected_syllable[0]
                pseudo_word += syllable
                previous_syllable = syllable
        except ValueError: #exceptions occurs when len(top_syllables) == 1
            print('Попробуте ещё раз. Можно уменьшить число слогов или увеличить число для отбора первых слогов.')
        print(pseudo_word)


if __name__ == '__main__':
    """
    Firt of all needs to create and turn on virtual envirement, then execute pip install -r requirements.
    For running app needs to download dictionary from link http://dict.ruslang.ru/Freq2011.zip
    and put it into folder with this program.
    """

    pseudo_word_generator()
