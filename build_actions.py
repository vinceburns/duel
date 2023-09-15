#Each function takes in the player that built it, the opposing player, and the game instance. 
def single_wood_build(game):
    build_player = game.active_player()
    build_player.n_wood += 1
    build_player.n_brown += 1
    return

def single_brick_build(game):
    build_player = game.active_player()
    build_player.n_brick += 1
    build_player.n_brown += 1
    return

def single_stone_build(game):
    build_player = game.active_player()
    build_player.n_stone += 1
    build_player.n_brown += 1
    return

def single_glass_build(game):
    build_player = game.active_player()
    build_player.n_glass += 1
    build_player.n_grey += 1
    return

def single_paper_build(game):
    build_player = game.active_player()
    build_player.n_paper += 1
    build_player.n_grey += 1
    return

def double_wood_build(game):
    build_player = game.active_player()
    build_player.n_wood += 2
    build_player.n_brown += 1
    return

def double_brick_build(game):
    build_player = game.active_player()
    build_player.n_brick += 2
    build_player.n_brown += 1
    return

def double_stone_build(game):
    build_player = game.active_player()
    build_player.n_stone += 2
    build_player.n_brown += 1
    return

def piraeus(game):
    build_player = game.active_player()
    build_player.wild_pap_glass += 1
    return

def appian_way(game):
    build_player = game.active_player()
    inactive_player = game.inactive_player()
    build_player.n_coin += 3
    inactive_player.remove_coins(3)
    #todo go again
    return

def mausoleum(game):
    build_player = game.active_player()
    return

def sphinx(game):
    build_player = game.active_player()
    return

def zeus(game):
    build_player = game.active_player()
    build_player.n_army += 1
    return

def artemis(game):
    build_player = game.active_player()
    build_player.n_coin += 12
    return

def no_action(game):
    return


if __name__ == '__main__':
    main()
