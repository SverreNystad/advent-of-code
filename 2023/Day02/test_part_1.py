
from part_1 import Game, is_possible_game


def test_possible_game():
    possible_game = Game(0, {"red": 10, "green": 10, "blue": 10})
    rules = {"red": 12, "green": 13, "blue": 14}
    assert is_possible_game(possible_game, rules)


def test_non_possible_game():
    non_possible_game = Game(0, {"red": 100, "green": 100, "blue": 100})
    rules = {"red": 0, "green": 0, "blue": 0}
    assert not is_possible_game(non_possible_game, rules)