from unittest.mock import patch
import pytest
import random


from app import get_random_number, Game

# Basically mocks the method on the specified object within the function
# Pretty much spyOn() in jasmine


@patch.object(random, 'randint')
def test_get_random_number(mocked_class):
    mocked_class.return_value = 17
    assert get_random_number() == 17

# Mocks the returns for input function
# side effects will return the next value each time input is run


@patch("builtins.input", side_effect=[11, '12', 'bob', 12, 5, -1])
def test_guess(inputs):
    game = Game()
    assert game.guess() == 11
    assert game.guess() == 12
    # as bob is a string
    with pytest.raises(ValueError):
        game.guess()
    # as 12 was already tried
    with pytest.raises(ValueError):
        game.guess()
    assert game.guess() == 5
    # -1 is not valid
    with pytest.raises(ValueError):
        game.guess()

# capfd is used to capture output from print


def test_validate_guess(capfd):
    game = Game()
    game._answer = 2

    assert not game._validate_guess(1)
    # unpacks capfd return
    out, _ = capfd.readouterr()
    assert out == '1 is too low\n'

    assert not game._validate_guess(3)
    out, _ = capfd.readouterr()
    assert out == '3 is too high\n'

    assert game._validate_guess(2)
    out, _ = capfd.readouterr()
    assert out == '2 is correct!\n'
