
import pprint
import build_actions
import end_game_action
import cost
from cost import wps
import sys
import time
from os import fsync,system,_exit

#probably move this to an exceptions.py file
class MyCustomException(Exception):
    def __init__(self, message="This is a custom exception."):
        self.message = message
        super().__init__(self.message)

class Card():
    def __init__(self, age, name, color, cost, free_build = None, wp = None, build_func = None, endgame_func = None, image = None):
        self.age = age
        self.name = name
        self.color = color
        self.cost = cost
        self.free_build = free_build
        #white privelege or white power-up 
        self.wp = wp
        #function pointer to call when this card is built. This will allow for the builder to collect its spoils
        self.build_func = build_func
        #function pointer to call at the end of the game. 
        self.endgame_func = endgame_func
        # I imagine this will be some jpeg file or something for the front end to use. This can be left empty until front-end development begins
        self.image_file = image

    def print(self):
        pp = pprint.PrettyPrinter(indent = 4)
        pp.pprint(vars(self))

    def build(self, game):
        if self.build_func != None:
            return (self.build_func(game))

def parse_cost(cost_str):
    n_coins = 0
    n_wood = 0
    n_stone = 0
    n_brick = 0
    n_glass = 0
    n_paper = 0
    costs = cost_str.replace(" ", "").split(",")
    for resource in costs:
        if ((resource.split(":", 1)[0]).lower() == "w"):
            n_wood = int(resource.split(":", 1)[0], 10)
        elif ((resource.split(":", 1)[0]).lower() == "s"):
            n_stone = int(resource.split(":", 1)[0], 10)
        elif ((resource.split(":", 1)[0]).lower() == "b"):
            n_brick = int(resource.split(":", 1)[0], 10)
        elif ((resource.split(":", 1)[0]).lower() == "g"):
            n_glass = int(resource.split(":", 1)[0], 10)
        elif ((resource.split(":", 1)[0]).lower() == "p"):
            n_paper = int(resource.split(":", 1)[0], 10)
        elif ((resource.split(":", 1)[0]).lower() == "c"):
            n_coin = int(resource.split(":", 1)[0], 10)
        else:
            raise MyCustomException(f"bad cost added:{resource}")
    return(cost.Cost(n_coins, n_wood, n_stone, n_brick, n_glass, n_paper))




def parse_card_fromcsv_line(line, age):
    if (line.startswith("#")):
        return None
    name = line.split("name=", 1)[1].split(",", 1)[0]
    color = line.split("color=", 1)[1].split(",", 1)[0]
    cost_str = line.split("cost=", 1)[1].split(",", 1)[0]
    if (cost_str == "free"):
        card_cost = cost.Cost()
    else:
        card_cost = parse_cost(cost_str)
    free_build = line.split("free_build=", 1)[1].split(",", 1)[0]
    if (free_build.lower() == "none"):
        free_build = None
    elif free_build not in wps:
        raise MyCustomException(f"bad free build value:{free_build}")
    wp = line.split("wp=", 1)[1].split(",", 1)[0]
    if (wp.lower() == "none"):
        wp = None
    elif wp not in wps:
        raise MyCustomException(f"bad free build value:{wp}")
    build_func = line.split("build_func=", 1)[1].split(",", 1)[0]
    if (build_func.lower() == "none"):
        build_func = None
    elif hasattr(build_actions, build_func):
        action_function = getattr(build_actions, build_func)
        if callable(action_function):
            build_func = action_function
        else:
            raise MyCustomException(f"Bad Build Action {build_func}")
    else:
        raise MyCustomException(f"Couldn't find! {build_func}")
    endgame_func = line.split("endgame_func=", 1)[1].split(",", 1)[0]
    if (endgame_func.lower() == "none"):
        endgame_func = None
    elif hasattr(end_game_action, endgame_func):
        action_function = getattr(end_game_action, endgame_func)
        if callable(action_function):
            endgame_func = action_function
        else:
            raise MyCustomException(f"Bad Build Action {endgame_func}")
    else:
        raise MyCustomException(f"Couldn't find! {endgame_func}")
    image = line.split("image=", 1)[1].strip()
    card = Card(age, name, color, cost, free_build, wp, build_func, endgame_func, image)
    return(card)
    

if __name__ == '__main__':
    main()
