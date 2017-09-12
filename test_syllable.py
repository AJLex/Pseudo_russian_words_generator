#test function fot pytest

from syllable import obtain_syllable, get_word_by_syllable,\
                     obtain_syllable_parameters, get_index_table, \
                     last_letters_handler, pseudo_word_generator


'''
test_obtain_syllable
'''
def test_obtain_syllable():
    word_by_letters = list('объезд')
    current_letter_number = 3
    letter_number = 4
    assert obtain_syllable(current_letter_number, letter_number,
                           word_by_letters) == 'ез'
    word_by_letters = list('­бакалаврский')
    current_letter_number = 5
    letter_number = 6
    assert obtain_syllable(current_letter_number, letter_number,
                           word_by_letters, third_condition=True) == 'лав'

'''
test_get_word_by_syllable
'''
def test_get_word_by_syllable(word_incoming='бледность'):
    assert get_word_by_syllable(word_incoming) == ['блед', 'ность']


def test_get_word_by_syllable(word_incoming='­бакалаврский'):
    assert get_word_by_syllable(word_incoming) == ['ба', 'ка', 'лав', 'рский']


def test_get_word_by_syllable(word_incoming='а-яй'):
    assert get_word_by_syllable(word_incoming) == None


'''
obtain_syllable_parameters
'''
def test_obtain_syllable_parameters(word_by_syllable=['ба', 'ка', 'лав', 'рский']):
    assert obtain_syllable_parameters(word_by_syllable) == [
                                                    ('ба', 'BEG', 0, 4),
                                                    ('ка', 'ба', 1, 4),
                                                    ('лав', 'ка', 2, 4),
                                                    ('рский', 'лав', 3, 4)
                                                    ]
