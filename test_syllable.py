#test function fot pytest

from syllable import obtain_syllable, get_word_by_syllable,\
                     obtain_syllable_parameters



'''
obtain_syllable
'''
def test_obtain_syllable():
    current_letter_number=3
    letter_number=4
    word_by_letters=list('объезд')
    assert obtain_syllable(current_letter_number, letter_number,
                           word_by_letters) == 'ез'


def test_obtain_syllable():
    current_letter_number=4
    letter_number=5
    word_by_letters=list('бакалаврский')
    assert obtain_syllable(current_letter_number, letter_number,
                           word_by_letters, third_condition=True) == 'лав'


'''
get_word_by_syllable
'''
def test_get_word_by_syllable():
    word_incoming='бледность'
    assert get_word_by_syllable(word_incoming) == ['блед', 'ность']


def test_get_word_by_syllable():
    word_incoming='бакалаврский'
    assert get_word_by_syllable(word_incoming) == ['ба', 'ка', 'лав', 'рский']


def test_get_word_by_syllable():
    word_incoming='а-яй'
    assert get_word_by_syllable(word_incoming) == None


'''
obtain_syllable_parameters
'''
def test_obtain_syllable_parameters():
    word_by_syllable=['ба', 'ка', 'лав', 'рский']
    assert obtain_syllable_parameters(word_by_syllable) == [
                                                    ('ба', 'BEG', 0, 4),
                                                    ('ка', 'ба', 1, 4),
                                                    ('лав', 'ка', 2, 4),
                                                    ('рский', 'лав', 3, 4)
                                                    ]
