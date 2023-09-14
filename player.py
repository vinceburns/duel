
import sys
import time
from os import fsync,system,_exit


class Player():
    def __init__(self):
        self.n_coin = 7
        #brown cards
        self.n_wood = 0
        self.n_brick = 0
        self.n_stone = 0
        self.n_brown = 0
        #grey cards
        self.n_glass = 0
        self.n_paper = 0
        self.n_grey = 0
        #blue
        self.n_blue = 0
        #green
        self.n_green = 0
        self.n_globe_looking_thingy = 0
        self.n_globe_looking_thingy = 0
        self.n_scale = 0
        self.n_map = 0
        self.n_mortle_and_pestle = 0
        self.n_triangles = 0
        self.n_feather = 0
        self.n_wheel = 0
        self.n_army = 0
        self.stone_post = 0
        self.clay_post = 0
        self.wood_post = 0
        self.paper_and_glass_post = 0
        # a wild of wood/brick/stone
        self.wild_normal = 0
        # a wild of a paper/glass
        self.wild_pap_glass = 0
        self.special_tokens = []
        self.wonders = []


    

if __name__ == '__main__':
    main()
