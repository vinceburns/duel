
import sys
import time
from os import fsync,system,_exit

#wp == 
class Card():
    def __init__(self, age, name, color, cost, free_build = None, wp = None, build_exec = None, endgame_exec = None, image = None):
        self.age = age
        self.name = name
        self.color = color
        self.cost = cost
        self.free_build = free_build
        #white privelege or white power-up 
        self.wp = wp
        #function pointer to call when this card is built. This will allow for the builder to collect its spoils
        self.build_exec = build_exec
        #function pointer to call at the end of the game. 
        self.endgame_exec = endgame_exec
        # I imagine this will be some jpeg file or something for the front end to use. This can be left empty until front-end development begins
        self.image_file = image


def parse_card_file(filename):
    with open
if __name__ == '__main__':
    main()
