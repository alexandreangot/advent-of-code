file = open("input", "r")

# Day 1 #
print("----- Day 1 -----")

### Part 1 ###
print("\n• Part 1 •")

games = file.read().splitlines()

max_values = {"red": 12, "green": 13, "blue": 14}

def is_valid_game(game: str) -> int:
    """ Return the game number if the game is valid, 0 otherwise.

    Args:
        game (str): The game to check.

    Returns:
        int: Number of the game if valid, 0 otherwise.
    """
    game, sets = game.split(": ")
    sets = sets.split("; ")
    game_number = int(game.split(" ")[1])
    for set in sets:
        set = set.split(", ")
        for cube_list in set:
            nb_cubes, color = cube_list.split(" ")   
            nb_cubes = int(nb_cubes)
            if nb_cubes > max_values[color]:
                return 0
    
    return game_number

total_nb_games = 0
for game in games:      
    total_nb_games += is_valid_game(game)

print(f"The total number of games is {total_nb_games}.")

### Part 2 ###
print("\n• Part 2 •")

power = 0
for game in games:      
    fewest_cubes = {"red": 0, "green": 0, "blue": 0}
    game, sets = game.split(": ")
    sets = sets.split("; ")
    for set in sets:
        set = set.split(", ")
        for cube_list in set:
            nb_cubes, color = cube_list.split(" ")   
            nb_cubes = int(nb_cubes)
            if nb_cubes > fewest_cubes[color]:
                fewest_cubes[color] = nb_cubes
                
    power += (fewest_cubes["red"] * fewest_cubes["green"] * fewest_cubes["blue"])

print(f"The sum of the power of these sets is {power}.")