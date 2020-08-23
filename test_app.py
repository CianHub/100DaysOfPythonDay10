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


@patch("builtins.input", side_effect=[4, 22, 9, 4, 6])
def test_game_win(input, capfd):
    game = Game()
    game._answer = 6

    game()

    # it ran the game with every input item and afterwards checked if win had been set to true
    assert game._win is True

    out = capfd.readouterr()[0]
    expected = ['4 is too low', 'Number not in range', '9 is too high',
                'Already guessed', '6 is correct!', 'It took you 3 guesses']
   # remove any new lines or blank outputs
    output = [line.strip() for line in out.split('\n') if line.strip()]

# zip will allow code to iterate through both lists at once so can compare both first items, second items etc with each other
    for line, expected_output in zip(output, expected):
        assert line == expected_output


@patch("builtins.input", side_effect=[None, 2, 3, 4, 5, 6, 7])
def test_game_lose(input, capfd):
    game = Game()
    game._answer = 12

    game()
    assert game._win is False
