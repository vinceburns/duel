#Each function takes in the player that built it, the opposing player, and the game instance. 
def add_3_points(game):
    build_player = game.active_player()
    build_player.n_points += 3 


def no_action(game):
    return


if __name__ == '__main__':
    main()
