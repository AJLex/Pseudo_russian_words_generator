import csv

'''
letter_number - current letter in cicle "for" from __main__
current_letter_number - is len of variable "word"
word - sum of syllables
word_by_syllable - list of syllable
word_by_letters - incoming word divided by letters

first condition: v|v,
second condition: v|cv,
third condition: vc|c...cv,
where v - vowel, c - consonant
'''
def obtaining_syllable(current_letter_number, letter_number,
                       word_by_letters, third_condition=False):
    syllable = ''
    if third_condition == False:
        for letter_number_temp in range(current_letter_number, letter_number + 1):
            syllable += word_by_letters[letter_number_temp]
    else:
        for letter_number_temp in range(current_letter_number, letter_number + 2):
            syllable += word_by_letters[letter_number_temp]
    return syllable


def recording_of_syllable(current_letter_number, letter_number, word_by_letters,
                          word, word_by_syllable, third_condition=False):
    syllable = obtaining_syllable(current_letter_number, letter_number,
                                  word_by_letters, third_condition)
    word += syllable
    current_letter_number = len(word)
    word_by_syllable.append(syllable)
    return current_letter_number, letter_number, word_by_syllable, word


def last_letters_handler(word_by_letters, word_by_syllable, vowel):
    if word_by_letters[-3] not in vowel:
        if len(word_by_letters) <= 3:
            word_by_syllable = ['']
            word_by_syllable[-1] += word_by_letters[-3]
        else:
            word_by_syllable[-1] += word_by_letters[-3]
    return word_by_syllable


def get_word_by_syllable(word_incoming, current_letter_number=0,
                         word_by_syllable=[], word=''):
    word_by_letters = list(word_incoming) + ['а', 'б']
    vowel = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    for letter_number in range(0, len(word_by_letters) - 2):
        if word_by_letters[letter_number] in vowel and \
           word_by_letters[letter_number + 1] in vowel:
            current_letter_number, letter_number , word_by_syllable, word = \
            recording_of_syllable(current_letter_number, letter_number, word_by_letters,
                                  word, word_by_syllable)

        elif  word_by_letters[letter_number] in vowel and \
              word_by_letters[letter_number + 1] not in vowel and \
              word_by_letters[letter_number + 2] in vowel:
            current_letter_number, letter_number , word_by_syllable, word = \
            recording_of_syllable(current_letter_number, letter_number, word_by_letters,
                                  word, word_by_syllable)

        elif word_by_letters[letter_number] in vowel and \
             word_by_letters[letter_number + 1] not in vowel and \
             word_by_letters[letter_number + 2] not in vowel:
            current_letter_number, letter_number , word_by_syllable, word = \
            recording_of_syllable(current_letter_number, letter_number, word_by_letters,
                                  word, word_by_syllable, third_condition=True)
    word_by_syllable = last_letters_handler(word_by_letters, word_by_syllable, vowel)
    return word_by_syllable


def obtain_syllable_parameters(word_by_syllable):
    syllable_param = []
    for syllable in word_by_syllable:
        previous_syllable = word_by_syllable[word_by_syllable.index(syllable) - 1] \
        if word_by_syllable.index(syllable) > 0 else ['BEG']
        syllable_param.append([syllable, previous_syllable,
                               word_by_syllable.index(syllable),
                               len(word_by_syllable)])
    return syllable_param


# def write_data_of_syllable(fileread='freqrnc2011.csv', filewrite):
#     with open(fileread, 'r', encoding='utf-8') as f:
#         fields = ['word', 'PoS', 'Freq', 'R', 'D', 'Doc']
#         reader = csv.DictReader(f, fields, delimiter='	')
#         for row in reader:
#             word_by_syllable = get_word_by_syllable(row.get('word'))


if __name__ == '__main__':
    print(obtain_syllable_parameters(get_word_by_syllable('а')))
