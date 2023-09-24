import numpy

#Each function takes in the player that built it, the opposing player, and the game instance. 
def single_wood_build(game, build_player):
    build_player.n_wood += 1
    return

def single_brick_build(game, build_player):
    build_player.n_brick += 1
    return

def single_stone_build(game, build_player):
    build_player.n_stone += 1
    return

def single_glass_build(game, build_player):
    build_player.n_glass += 1
    return

def single_paper_build(game, build_player):
    build_player.n_paper += 1
    return

def double_wood_build(game, build_player):
    build_player.n_wood += 2
    return

def double_brick_build(game, build_player):
    build_player.n_brick += 2
    return

def double_stone_build(game, build_player):
    build_player.n_stone += 2
    return

def piraeus(game, build_player):
    build_player.wild_pap_glass += 1
    game.write_to_todo("Piraeus: TODO NEED ABILITY TO GO AGAIN")
    return

def appian_way(game, build_player):
    inactive_player = game.inactive_player()
    build_player.n_coin += 3
    inactive_player.remove_coins(3)
    game.write_to_todo("Appian way: TODO NEED ABILITY TO GO AGAIN")
    return

def mausoleum(game, build_player):
    game.write_to_todo("Mausoleum: TODO NEED ABILITY TO SELECT FROM DISCARD PILE")
    return

def sphinx(game, build_player):
    game.write_to_todo("SPHINX: TODO NEED ABILITY TO GO AGAIN")
    return

def zeus(game, build_player):
    build_player.n_army += 1
    game.write_to_todo("ZEUS: TODO NEED TO DESTROY BROWN CARD OF OPPONENT")
    return

def artemis(game, build_player):
    build_player.n_coin += 12
    game.write_to_todo("artemis: TODO NEED ABILITY TO GO AGAIN")
    return

def single_army_build(game, build_player):
    build_player.n_army += 1
    return

def double_army_build(game, build_player):
    build_player.n_army += 2
    return

def triple_army_build(game, build_player):
    build_player.n_army += 3
    return

def triangle(game, build_player):
    build_player.n_triangles += 1
    return

def wheel(game, build_player):
    build_player.n_wheel += 1
    return

def feather(game, build_player):
    build_player.n_feather += 1
    return

def mortleandpestle(game, build_player):
    build_player.n_mortle_and_pestle += 1
    return

def map(game, build_player):
    build_player.n_map += 1
    return

def globe_looking_thingy(game, build_player):
    build_player.n_globe_looking_thingy += 1
    return

def stone_post(game, build_player):
    build_player.stone_post = 1
    return

def clay_post(game, build_player):
    build_player.brick_post = 1
    return

def wood_post(game, build_player):
    build_player.wood_post = 1
    return

def add_4_coins(game, build_player):
    build_player.n_coin += 4
    return

def add_3_coins_per_grey(game, build_player):
    build_player.n_coin += 3*build_player.n_grey
    return

def add_2_coins_per_brown(game, build_player):
    build_player.n_coin += 2*build_player.n_brown
    return

def add_1_coins_per_red(game, build_player):
    build_player.n_coin += build_player.n_red
    return

def add_1_coins_per_yellow(game, build_player):
    build_player.n_coin += build_player.n_yellow
    return

def add_2_coins_per_wonder(game, build_player):
    n_wonders = numpy.intersect1d(build_player.wonders, build_player.built_cards)
    build_player.n_coin += 2*n_wonders
    return

def add_1_coins_per_max_yellow(game, build_player):
    n_yellow = max(game.inactive_player().n_yellow, build_player.n_yellow)
    build_player.n_coin += n_yellow
    return

def add_1_coins_per_max_brown_grey(game, build_player):
    n_brown_grey = max(game.inactive_player().n_brown + game.inactive_player().n_grey, build_player.n_brown + build_player.n_grey)
    build_player.n_coin += n_brown_grey
    return

def add_1_coins_per_max_blue(game, build_player):
    n_blue = max(game.inactive_player().n_blue, build_player.n_blue)
    build_player.n_coin += n_blue
    return

def add_1_coins_per_max_green(game, build_player):
    n_green = max(game.inactive_player().n_green, build_player.n_green)
    build_player.n_coin += n_green
    return

def add_1_coins_per_max_red(game, build_player):
    n_red = max(game.inactive_player().n_red, build_player.n_red)
    build_player.n_coin += n_red
    return

def no_action(game, build_player):
    return

if __name__ == '__main__':
    main()
