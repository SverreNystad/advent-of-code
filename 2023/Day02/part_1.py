from dataclasses import dataclass

file_name = "input.txt"

with open(file_name, "r") as f:
    data: list[str] = f.readlines()

max_cubes_for_colors = {
    "red":   12,
    "green": 13,
    "blue":  14,
}



@dataclass()
class Subset:
    cubes: dict[str, int]

    def __init__(self, cubes: set[str]):
        """
        Cubes are in the form "x red" where x, y, z are integers
        """
        self.cubes = {}
        for cube in cubes:
            count, color = cube.strip().split(" ")
            self.cubes[color] = int(count)

@dataclass(frozen=True)
class Game:
    id: int
    subsets: list[Subset]

def parse_game(line: str) -> Game:
    """
    Games are in the form "Game <id>: x red, y green, z blue" where x, y, z are integers
    But they can be in any order and there can be several batches of cubes for the same color
    They can also use several separators (semicolons, commas)
    """
    id: str
    batches: str
    id, batches = line.split(":")
    # Id is in the form "Game <id>"
    id_index = 1
    id = int(id.split(" ")[id_index])
    # Cubes are in the form "x red, y green, z blue" where x, y, z are integers
    # But a game gan have several batches of cubes separated by semicolons or commas
    batches: list[str] = batches.strip().split(";")
    
    cubes = [cubes.strip().split(",") for cubes in batches]

    subsets = []
    for subset in cubes:
        subsets.append(Subset(subset))

    return Game(int(id), subsets)

def is_possible_game(game: Game, rules: dict[str, int]) -> bool:
    
    for cubes in game.subsets:
        for color, count in cubes.cubes.items():
            if count > rules[color]:
                return False
    return True

def id_of_all_possible_games(games: list[Game], rules: dict[str, int]) -> list[int]:
    possible_games = []
    for game in games:
        if is_possible_game(game, rules):
            possible_games.append(game.id)
    return possible_games

if __name__ == "__main__":
    all_games = []
    for line in data:
        game = parse_game(line)
        all_games.append(game)
    
    total = sum(id_of_all_possible_games(all_games, max_cubes_for_colors))
    print(f"total = {total}")