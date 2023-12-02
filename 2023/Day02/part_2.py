
import math
from part_1 import Subset, parse_game


def find_least_count_for_subsets(subsets: list[Subset]) -> Subset:
    """
    Find the smallest parts of the subsets
    """
    smallest_part = Subset({})
    for subset in subsets:
        for color, count in subset.cubes.items():
            if smallest_part.cubes.get(color, -math.inf) < count:
                smallest_part.cubes[color] = count
    return smallest_part

file_name = "input.txt"

with open(file_name, "r") as f:
    data: list[str] = f.readlines()

def power(subset: Subset) -> int:
    """
    Compute the power of a subset
    """
    power = 1
    for color, count in subset.cubes.items():
        power *= count
    return power

if __name__ == "__main__":

    # test
    game = parse_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    print(power(find_least_count_for_subsets(game.subsets)))
    

    all_games = []
    for line in data:
        game = parse_game(line)
        all_games.append(game)
    # print(all_games[0])
    # print(find_least_count_for_subsets(all_games[0].subsets))

    # Find the smallest parts of the subsets
    smallest_parts = []
    for game in all_games:
        smallest_parts.append(find_least_count_for_subsets(game.subsets))
    
    powers_of_smallest_parts = [power(subset) for subset in smallest_parts]
    print(f"The sum of the power of the minimum sets {sum(powers_of_smallest_parts)}")