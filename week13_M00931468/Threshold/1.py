import random

class Pokemon:
    def __init__(self,type,hp,name,collector_no=0000,stage=1,evolves=''):
        self.type =  type
        self.hp = hp
        self.name = name
        self.collector_no = collector_no
        self.stage = stage
        self.evolves = evolves

def generate_unique_num(cache, lower_bound, upper_bound):
    num = random.randint(lower_bound, upper_bound)
    while (num in cache):
        num = random.randint(lower_bound, upper_bound)
    cache.append(num)

class Player:
    active = ''
    prize_cards = []
    cache = []
    
    def __init__(self, deck=[]):
        self.deck = deck
        self.__prize_cards_no = 6

    def get_prize_cards(self):
        for index in range(self.__prize_cards_no):
            generate_unique_num(Player.cache,0,59)

        for num in Player.cache:
            pokemon = self.deck[num]
            Player.prize_cards.append(pokemon)
            del self.deck[num]
     

class Game:
    deck_no = 60
    bench = [0, 0, 0, 0, 0, 0]
    hand = [0, 0, 0, 0, 0, 0, 0]





    