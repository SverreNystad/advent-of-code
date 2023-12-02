
from part_1 import parse_game
from part_2 import find_least_count_for_subsets, power

def test_power_of_least_count_for_subsets():
    """
    Take the test cases from the problem statement
    """
    # Arrange
    expected_power_game_1 = 48
    expected_power_game_2 = 12
    expected_power_game_3 = 1560
    expected_power_game_4 = 630
    expected_power_game_5 = 36

    game_1 = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    game_2 = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
    game_3 = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    game_4 = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    game_5 = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"

    # Act
    game_1 = parse_game(game_1)
    game_2 = parse_game(game_2)
    game_3 = parse_game(game_3)
    game_4 = parse_game(game_4)
    game_5 = parse_game(game_5)
    
    # Assert
    assert power(find_least_count_for_subsets(game_1.subsets)) == expected_power_game_1
    assert power(find_least_count_for_subsets(game_2.subsets)) == expected_power_game_2
    assert power(find_least_count_for_subsets(game_3.subsets)) == expected_power_game_3
    assert power(find_least_count_for_subsets(game_4.subsets)) == expected_power_game_4
    assert power(find_least_count_for_subsets(game_5.subsets)) == expected_power_game_5