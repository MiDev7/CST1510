from enum import Enum

def main():
    class Type(Enum):
        PSYCHIC = "psychic"
        GRASS = "grass"
        FIRE = "fire"
        LIGHTNING = "lightning"
        DARKNESS = "darkness"
        DRAGON = "dragon"
        METAL = "metal"
        COLORLESS = "colorless"
        WATER = "water"
        FIGHTING = "fighting"
        FAIRY = "fairy"

    class TrainerType(Enum):
        ITEM = "item"
        SUPPORT = "support"
        STADIUM = "stadium"

    class Card:
        def __init__(self, name : str) -> None:
            self.__name = name

        def get_name(self):
            return self.__name 
        
        def __str__(self) -> str:
            return f"\tCard Name: {self.__name}\n"
        

    class Pokemon(Card):
        def __init__(self, name: str, healthPoint : int, type : Type, ability) -> None:
            super().__init__(name)
            self.__healthPoint = healthPoint
            self.__type = type
            self.__ability = ability


        def get_health_point(self):
            return self.__healthPoint
            
        def get_type(self):
            return self.__type   
        
        def get_ability(self):
            return self.__ability

        def __str__(self) -> str:
            return super().__str__() + f"Card Type: Pokemon \nHP: {self.__healthPoint} \nPokemon Type: {self.__type.value} \nPokemon Ability: {self.__ability}\n"


    class Energy(Card):
        def __init__(self, name: str, symbol : Type) -> None:
            super().__init__(name)
            self.__symbol = symbol

        def get_symbol(self):
            return self.__symbol

        def __str__(self) -> str:
            return super().__str__() + f"Card Type: Energy \nSymbol: {self.__symbol.value}\n"

    class Trainer(Card):
        def __init__(self, name: str, type : TrainerType, text : str, rule : str) -> None:
            super().__init__(name)
            self.__type = type
            self.__text = text
            self.__rule = rule

        def get_type(self):
            return self.__type
        
        def get_text(self):
            return self.__text
        
        def get_rule(self):
            return self.__rule
        
        def __str__(self) -> str:
            return super().__str__() + f"Card Type: Trainer \nTrainer Type: {self.__type.value} \nText: {self.__text} \nRule: {self.__rule}"
        
    #Pokemon
    alakazam = Pokemon("Alakazam", 80,Type.PSYCHIC, "Confuse Ray")
    blastoise = Pokemon("Blastoise", 100, Type.WATER, "Hydro Pump")
    chansey = Pokemon("Chansey", 120, Type.COLORLESS, "Double-edge")
    charizard = Pokemon("Charizard", 120, Type.FIRE, "Fire Spin")
    clefairy = Pokemon("Clefairy", 40, Type.COLORLESS, "Metronome")
    gyarados = Pokemon("Gyarados", 100, Type.WATER, "Dragon Rage")
    hitmonchan = Pokemon("Hitmonchan", 70, Type.FIGHTING, "Special Punch")
    machamp = Pokemon("Machamp", 100, Type.FIGHTING, "Seismic Toss")
    magneton = Pokemon("Magneton", 60, Type.LIGHTNING, "Selfdestruct")
    mewtwo = Pokemon("Mewtwo", 60, Type.PSYCHIC, "Barrier")
    nidoking = Pokemon("Nidoking", 90, Type.GRASS, "Toxic")
    ninetales = Pokemon("Ninetales", 80, Type.FIRE, "Fire Blast")
    poliwrath = Pokemon("Poliwrath", 90, Type.WATER, "Whirlpool")
    raichu = Pokemon("Raichu", 80, Type.LIGHTNING, "Thunder")
    venusaur = Pokemon("Venusaur", 100, Type.GRASS, "Solarbeam")
    zapdos = Pokemon("Zapdos", 90, Type.LIGHTNING, "Thunderbolt")
    beedrill = Pokemon("Beedrill", 80, Type.GRASS, "Poison Sting")
    dragonair = Pokemon("Dragonair", 80, Type.COLORLESS, "Hyper Beam")
    dugtrio = Pokemon("Dugatrio", 70, Type.LIGHTNING, "Earthquake")
    electabuzz = Pokemon("Electabuzz", 70, Type.LIGHTNING, "Thunderpunch")


    # Trainers
    clefairyDoll = Trainer("Clefairy Doll",TrainerType.SUPPORT,"Play Clefairy Doll as if it were a Basic Pokémon. While in play, Clefairy Doll counts as a Pokémon (instead of a Trainer card)","Clefairy Doll has no attacks, can't retreat, and can't be Asleep, Confused, Paralyzed, or Poisoned. If Clefairy Doll is Knocked Out, it doesn't count as a Knocked Out Pokémon. At any time during your turn before your attack, you may discard Clefairy Doll." )
    computerSearch = Trainer("Computer Search", TrainerType.ITEM,"Discard 2 of the other cards from your hand in order to search your deck for any card and put it into your hand. Shuffle your deck afterward.","\
    Discard 2 cards from your hand. (If you can't discard 2 cards, you can't play this card.) Search your deck for a card and put it into your hand. Shuffle your deck afterward.You may play as many Item cards as you like during your turn (before your attack).")
    devolutionSpray = Trainer("Devolution Spray", TrainerType.ITEM,"Devolve 1 of your evolved Pokémon and put the highest stage Evolution card on it into your hand. (That Pokémon can't evolve this turn.)","Choose 1 of your own Pokémon in play and a Stage of Evolution. Discard all Evolution cards of that Stage or higher attached to that Pokémon. That Pokémon is no longer Asleep, Confused, Paralyzed, Poisoned, or anything else that might be the result of an attack (just as if you had evolved it).")
    imposterProfessorOak = Trainer("Imposter Professor Oak", TrainerType.SUPPORT, "Your opponent shuffles his or her hand into his or her deck, then draws 7 cards.","Your opponent shuffles his or her hand into his or her deck, then draws 7 cards.")
    itemFinder = Trainer("Item Finder",TrainerType.SUPPORT,"Discard 2 of the other cards from your hand in order to put a Trainer card from your discard pile into your hand.","Discard 2 of the other cards from your hand in order to put a Trainer card from your discard pile into your hand.")
    lass = Trainer("Lass", TrainerType.SUPPORT,"You and your opponent show each other your hands, then shuffle all the Trainer cards from your hands into your decks.","You and your opponent show each other your hands, then shuffle all the Trainer cards from your hands into your decks.")
    pokemonBreeder = Trainer("Pokemon Breeder", TrainerType.SUPPORT, "Put a Stage 2 Evolution card from your hand on the matching Basic Pokémon. You can only play this card when you would be allowed to evolve that Pokémon anyway.","Put a Stage 2 Evolution card from your hand on the matching Basic Pokémon. You can only play this card when you would be allowed to evolve that Pokémon anyway.")


    # Energy
    doubleColorlessEnergy = Energy("Double Colorless Energy", Type.COLORLESS)
    fightingEnergy = Energy("Fighting Energy", Type.FIGHTING)
    fireEnergy = Energy("Fire Energy", Type.FIRE)
    grassEnergy =  Energy("Grass Energy", Type.GRASS)
    lightingEnergy =  Energy("Lighting Energy", Type.LIGHTNING)
    psychicEnergy = Energy("Psychic Energy", Type.PSYCHIC)
    waterEnergy = Energy("Water Energy", Type.WATER)


if __name__ =="__main__":
    main