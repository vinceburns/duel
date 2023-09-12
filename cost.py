
import sys
import time
from os import fsync,system,_exit

#These ened to be somewhere game, player, and card all understand. Placeholder for now here. 
wps = { "hammer", "horseshoe", "dagger", "wall", "target", "helmet", "book", "gear", "harp", "lamp", "mask", "pillar", "moon", "sun", "droplet", "senate", "jug", "barrel" }

class Cost():
    def __init__(self, n_coins = 0, n_wood = 0, n_stone = 0, n_brick = 0, n_glass = 0, n_paper = 0):
        self.n_coins = n_coins
        self.n_wood = n_wood
        self.n_stone = n_stone
        self.n_brick = n_brick
        self.n_glass = n_glass
        self.n_paper = n_paper

if __name__ == '__main__':
    main()
