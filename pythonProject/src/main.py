from game import Game


def main():
    input_file = open('input.txt', 'r')
    game_list = input_file.readlines()

    count = 0
    # Strips the newline character
    for game in game_list:
        game_instance = Game(game)
        #if game_instance.check_validity(game_instance.split_sets()):
            #count += game_instance.id
        game_instance.set_minimum(game_instance.split_sets())
        count += game_instance.minimum_green * game_instance.minimum_red * game_instance.minimum_blue
    print(count)


if __name__ == "__main__":
    main()
