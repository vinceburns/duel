
import sys
import time
from os import fsync,system,_exit

#These need to be somewhere game, player, and card all understand. Placeholder for now here. 
#probably move to a "defines" file
wps = { "hammer", "horseshoe", "dagger", "wall", "target", "helmet", "book", "gear", "harp", "lamp", "mask", "pillar", "moon", "sun", "droplet", "senate", "jug", "barrel" }

class Cost():
    def __init__(self, n_coins = 0, n_wood = 0, n_stone = 0, n_brick = 0, n_glass = 0, n_paper = 0):
        self.n_coins = n_coins
        self.n_wood = n_wood
        self.n_stone = n_stone
        self.n_brick = n_brick
        self.n_glass = n_glass
        self.n_paper = n_paper

    def print_cost(self):
        printer = ""
        if self.n_coins:
            printer += f"coins:{self.n_coins} "
        if self.n_wood:
            printer += f"wood:{self.n_wood} "
        if self.n_stone:
            printer += f"stone:{self.n_stone} "
        if self.n_brick:
            printer += f"brick:{self.n_brick} "
        if self.n_paper:
            printer += f"paper:{self.n_paper} "
        if self.n_glass:
            printer += f"glass:{self.n_glass} "
        if len(printer):
            print(printer)
        else:
            print("free")

if __name__ == '__main__':
    main()
