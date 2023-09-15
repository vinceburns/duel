
import pprint
import card
import player
import cost
from os import fsync,system,_exit

class Game():
    def __init__(self):
        self.players = []
        self.players.append(player.Player())
        self.players.append(player.Player())
        self.age = 0
        #postive values means player 0 is winning, negative = player 1 is winning
        self.army_pos = 0
        self.army_zone = 0
        self.discard_pile = []
        self.age_cards = []
        #this is the index in the list to the active player. it is always 0 or 1. 
        self.active_player_index = 0
        #things we will likely need, The active board where the laid out cards to be selected are on

    def play(self):
        #woohoo let's have some fun. 
        #initialize wonders
        #select wonders
        #setup Green token thingys
        self.age = 1
        self.setup_age1()
        self.play_age()

    def play_age(self):
        return
        #while (card in age_cards):
        #select card
        #run action
        #swap player
        #top_o_loop

    def update_army_pos(self):
        #zone 0 == even zone 1 = player winning by 1 or 2 points
        self.army_pos = self.players[0].n_army - self.players[1].n_army
        losing_player_idx = 1 if (self.army_pos > 0) else 0
        if (abs(self.army_pos) > 8):
            print(f"END OF GAME! Player {losing_player_idx ^ 1} won!!")
            exit(1)
        elif (abs(self.army_pos) > 5):
            self.army_zone = 3
        elif (abs(self.army_pos) > 2):
            self.army_zone = 2
            self.players[losing_player_idx].remove_army_coins(self.army_zone)
        elif (abs(self.army_pos) > 0):
            self.army_zone = 1
            self.players[losing_player_idx].remove_army_coins(self.army_zone)
        else:
            self.army_zone = 0

        
    def setup_age1(self):
        self.age_cards = []
        with open("cards/age1.csv", "r") as f:
            lines = f.readlines()
            for line in lines:
                current_card = card.parse_card_fromcsv_line(line, 1)
                if current_card:
                    current_card.build(self)
                    self.age_cards.append(current_card)

    def active_player(self):
        return(self.players[self.active_player_index])
    def inactive_player(self):
        return(self.players[self.active_player_index ^ 1])
def main():
    game = Game()
    game.play()
    return

if __name__ == '__main__':
    main()
