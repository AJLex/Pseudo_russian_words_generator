def write_syllables(letter_number, current_letter_number, word, word_by_syllable,
                    second_condition=False):
    syllable = ''
    if second_condition == False:
        for letter in range(current_letter_number, letter_number + 1):
            syllable = syllable + word_list[letter]
    else:
        for letter in range(current_letter_number, letter_number + 2):
            syllable = syllable + word_list[letter]
    word = word + syllable
    current_letter_number = len(word)
    word_by_syllable.append(syllable)
    return current_letter_number, word, word_by_syllable


if __name__ == '__main__':
    word_list = list(input('> '))
    current_letter_number = 0
    word = ''
    word_by_syllable = []
    vowel = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    for letter_number in range(0, len(word_list) - 1):
        print('letter_number ', letter_number)
        if word_list[letter_number] in vowel and word_list[letter_number + 1] in vowel:
            current_letter_number, word, word_by_syllable = write_syllables(letter_number,
                                                                     current_letter_number,
                                                                     word,
                                                                     word_by_syllable)

        elif word_list[letter_number] in vowel and word_list[letter_number + 1] \
             not in vowel and word_list[letter_number + 2] in vowel:
            current_letter_number, word, word_by_syllable = write_syllables(letter_number,
                                                                     current_letter_number,
                                                                     word,
                                                                     word_by_syllable)

        elif word_list[letter_number] in vowel and word_list[letter_number + 1] \
             not in vowel and word_list[letter_number + 2] not in vowel:
            current_letter_number, word, word_by_syllable = write_syllables(letter_number,
                                                                     current_letter_number,
                                                                     word,
                                                                     word_by_syllable,
                                                                     second_condition=True) # first condition: v|v or v|cv, second condition: vc|c...cv
                                                                                            # where v - vowel, c - consonant
    print('current_letter_number', current_letter_number)
    if word_list[-1] in vowel:
        syllable = ''
        for letter_number in range(current_letter_number, len(word_list)):
            syllable = syllable + word_list[letter_number]
        word_by_syllable.append(syllable)
    else:
        word_by_syllable[-1] = word_by_syllable[-1] + word_list[-1]
    print(word_by_syllable)
