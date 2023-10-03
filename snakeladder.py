import random

def roll_dice():
    return random.randint(1, 6)

def snake_ladder(position):
    snakes_and_ladders = {
        16: 6,
        47: 26,
        49: 11,
        56: 53,
        62: 19,
        64: 60,
        87: 24,
        93: 73,
        95: 75,
        98: 78
    }
    if position in snakes_and_ladders:
        new_position = snakes_and_ladders[position]
        if new_position < position:
            print(f"Snake! You go down from {position} to {new_position}.")
        else:
            print(f"Ladder! You climb up from {position} to {new_position}.")
        return new_position
    else:
        return position

def snake_ladder_game():
    player_position = 1
    while player_position < 100:
        input("Press Enter to roll the dice...")
        dice_value = roll_dice()
        print(f"You rolled a {dice_value}.")
        player_position += dice_value
        player_position = snake_ladder(player_position)
        print(f"You are now at square {player_position}.\n")

    print("Congratulations! You reached square 100. You won!")

if __name__ == "__main__":
    print("Welcome to Snake and Ladder Game!")
    snake_ladder_game()
