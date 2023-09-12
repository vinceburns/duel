#Each function takes in the player that built it, the opposing player, and the game instance. 
def single_wood_build(build_player, opposing_player, game):
    build_player.n_wood += 1

def single_brick_build(build_player, opposing_player, game):
    build_player.n_brick += 1

def single_stone_build(build_player, opposing_player, game):
    build_player.n_stone += 1

def single_glass_build(build_player, opposing_player, game):
    build_player.n_glass += 1

def single_paper_build(build_player, opposing_player, game):
    build_player.n_paper += 1

def double_wood_build(build_player, opposing_player, game):
    build_player.n_wood += 2

def double_brick_build(build_player, opposing_player, game):
    build_player.n_brick += 2

def double_stone_build(build_player, opposing_player, game):
    build_player.n_stone += 2


if __name__ == '__main__':
    main()
