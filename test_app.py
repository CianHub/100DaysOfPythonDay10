from unittest.mock import patch
import random


from app import get_random_number, Game

# Basically mocks the method on the specified object within the function
# Pretty much spyOn() in jasmine
@patch.object(random, 'randint')
def test_get_random_number(mocked_class):
    mocked_class.return_value = 17
    assert get_random_number() == 17
