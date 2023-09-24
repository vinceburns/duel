#Each function takes in the player that built it, the opposing player, and the game instance. 
def add_1_points(game):
    build_player = game.active_player()
    build_player.n_points += 1 

def add_2_points(game):
    build_player = game.active_player()
    build_player.n_points += 2 

def add_3_points(game):
    build_player = game.active_player()
    build_player.n_points += 3

def add_4_points(game):
    build_player = game.active_player()
    build_player.n_points += 4 

def add_5_points(game):
    build_player = game.active_player()
    build_player.n_points += 5 

def add_6_points(game):
    build_player = game.active_player()
    build_player.n_points += 6 

def add_7_points(game):
    build_player = game.active_player()
    build_player.n_points += 7 

def add_9_points(game):
    build_player = game.active_player()
    build_player.n_points += 9

def add_1_points_per_max_yellow(game, build_player):
    n_yellow = max(game.inactive_player().n_yellow, build_player.n_yellow)
    build_player.n_points += n_yellow

def add_1_points_per_max_brown_grey(game, build_player):
    n_brown_grey = max(game.inactive_player().n_brown + game.inactive_player().n_grey, build_player.n_brown + build_player.n_grey)
    build_player.n_points += n_brown_grey

def add_1_points_per_max_blue(game, build_player):
    n_blue = max(game.inactive_player().n_blue, build_player.n_blue)
    build_player.n_points += n_blue

def add_1_points_per_max_green(game, build_player):
    n_green = max(game.inactive_player().n_green, build_player.n_green)
    build_player.n_points += n_green

def add_1_points_per_max_red(game, build_player):
    n_red = max(game.inactive_player().n_red, build_player.n_red)
    build_player.n_points += n_red

def add_2_points_per_max_wonder(game, build_player):
    n_wonders = max(numpy.intersect1d(game.inactive_player().wonders, game_inactive_player().built_cards),numpy.intersect1d(build_player.wonders, build_player.built_cards))
    build_player.n_points += 2*n_wonders

def add_1_points_per_max_3_coins(game, build_player):
    n_3_coins = max(game.inactive_player().n_coin // 3, build_player.n_coin // 3)
    build_player.n_points += n_3_coins
    return

def no_action(game):
    return


if __name__ == '__main__':
    main()
