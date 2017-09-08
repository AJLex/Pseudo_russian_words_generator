import csv
from collections import Counter

'''
letter_number - current letter in cicle "for"
current_letter_number - len of variable "word"
word - sum of syllables
word_by_syllable_temp - list of syllable
word_by_letters - incoming word divided by letters

first condition: v|v,
second condition: v|cv,
third condition: vc|c...cv,
where v - vowel, c - consonant
'''
def obtaining_syllable(current_letter_number, letter_number,
                       word_by_letters, third_condition=False):
    syllable = ''
    sign = ['ь', 'ъ']
    if third_condition == False:
        for letter_number_temp in range(current_letter_number, letter_number + 1):
            syllable += word_by_letters[letter_number_temp]
        if word_by_letters[letter_number + 1] in sign:
                syllable += word_by_letters[letter_number + 1]
    else:
        for letter_number_temp in range(current_letter_number, letter_number + 2):
            syllable += word_by_letters[letter_number_temp]
        if word_by_letters[letter_number + 2] in sign:
                syllable += word_by_letters[letter_number + 2]
    return syllable


def recording_of_syllable(current_letter_number, letter_number, word_by_letters,
                          word, word_by_syllable_temp, third_condition=False):
    syllable = obtaining_syllable(current_letter_number, letter_number,
                                  word_by_letters, third_condition)
    word += syllable
    current_letter_number = len(word)
    word_by_syllable_temp.append(syllable)
    return current_letter_number, letter_number, word_by_syllable_temp, word


def last_letters_handler(word_by_letters, word_by_syllable_temp, vowel):
    sign = ['ь', 'ъ']
    if word_by_letters[-3] not in vowel and\
       word_by_letters[-3] not in sign:
        if len(word_by_letters) <= 3:
            word_by_syllable_temp = ['']
            word_by_syllable_temp[-1] += word_by_letters[-3]
        else:
            word_by_syllable_temp[-1] += word_by_letters[-3]
    return word_by_syllable_temp


def get_word_by_syllable(word_incoming,word_by_syllable_temp=[],
                         current_letter_number=0, word=''):
    word_by_letters = list(word_incoming) + ['а', 'б']
    if '-' in word_by_letters:
        return None
    else:
        vowel = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
        for letter_number in range(0, len(word_by_letters) - 2):
            if word_by_letters[letter_number] in vowel and \
               word_by_letters[letter_number + 1] in vowel:
                current_letter_number, letter_number , word_by_syllable_temp, word = \
                recording_of_syllable(current_letter_number, letter_number, word_by_letters,
                                      word, word_by_syllable_temp)

            elif  word_by_letters[letter_number] in vowel and \
                  word_by_letters[letter_number + 1] not in vowel and \
                  word_by_letters[letter_number + 2] in vowel:
                current_letter_number, letter_number , word_by_syllable_temp, word = \
                recording_of_syllable(current_letter_number, letter_number, word_by_letters,
                                      word, word_by_syllable_temp)

            elif word_by_letters[letter_number] in vowel and \
                 word_by_letters[letter_number + 1] not in vowel and \
                 word_by_letters[letter_number + 2] not in vowel:
                current_letter_number, letter_number , word_by_syllable_temp, word = \
                recording_of_syllable(current_letter_number, letter_number, word_by_letters,
                                      word, word_by_syllable_temp, third_condition=True)
        word_by_syllable_temp = last_letters_handler(word_by_letters, word_by_syllable_temp, vowel)
        return word_by_syllable_temp


def obtain_syllable_parameters(word_by_syllable_temp):
    syllable_param = []
    if word_by_syllable_temp:
        for syllable in word_by_syllable_temp:
            previous_syllable = word_by_syllable_temp[word_by_syllable_temp.index(syllable) - 1] \
            if word_by_syllable_temp.index(syllable) > 0 else 'BEG'
            syllable_param.append((syllable, previous_syllable,
                                   word_by_syllable_temp.index(syllable),
                                   len(word_by_syllable_temp)))
        word_by_syllable_temp = ''
        return syllable_param


def write_index_table(file_write, file_read='freqrnc2011.csv', ):
    with open(file_read, 'r', encoding='utf-8') as f:
        syllable_list = []
        fields = ['word', 'PoS', 'Freq', 'R', 'D', 'Doc']
        reader = csv.DictReader(f, fields, delimiter='	')
        for row in reader:
            try:
                syllable_param = []
                if list(row.get('word'))[0] != list(row.get('word'))[0].upper():
                    word_by_syllable = get_word_by_syllable(row.get('word'), [])
                    syllable_param = obtain_syllable_parameters(word_by_syllable)
                    if syllable_param:
                        syllable_list += syllable_param
            except IndexError:
                print('Нет гласных')
    count = Counter(syllable_list)
    with open(file_write, 'w', encoding='utf-8') as f:
        for key in count:
            f.write(str(key).strip('(').strip(')') + ', ' + str(count[key]) + '\n')


if __name__ == '__main__':
    write_index_table('index_table.txt')
