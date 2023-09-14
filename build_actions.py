#Each function takes in the player that built it, the opposing player, and the game instance. 
def single_wood_build(game):
    print("building a wood")
    build_player = game.active_player()
    build_player.n_wood += 1
    build_player.n_brown += 1

def single_brick_build(game):
    build_player = game.active_player()
    build_player.n_brick += 1
    build_player.n_brown += 1

def single_stone_build(game):
    build_player = game.active_player()
    build_player.n_stone += 1
    build_player.n_brown += 1

def single_glass_build(game):
    build_player = game.active_player()
    build_player.n_glass += 1
    build_player.n_grey += 1

def single_paper_build(game):
    build_player = game.active_player()
    build_player.n_paper += 1
    build_player.n_grey += 1

def double_wood_build(game):
    build_player = game.active_player()
    build_player.n_wood += 2
    build_player.n_brown += 2

def double_brick_build(game):
    build_player = game.active_player()
    build_player.n_brick += 2
    build_player.n_brown += 2

def double_stone_build(game):
    build_player = game.active_player()
    build_player.n_stone += 2
    build_player.n_brown += 2


if __name__ == '__main__':
    main()
