from typing import Any


class Pokemon:
    def __init__(self,type,hp,name,collector_no=0000,stage=1,evolves=''):
        self.__type =  type
        self.__hp = hp
        self.__name = name
        self.__collector_no = collector_no
        self.__stage = stage
        self.__evolves = evolves

    # Accessor
    def get_type(self):
         return self.__type
    
    def get_hp(self):
         return self.__hp
    
    def get_name(self):
         return self.__name
    
    def get_collector_no(self):
         return self.__collector_no
    
    def get_stage(self):
         return self.__stage
    
    def get_evolves(self):
         return self.__evolves

    def __str__(self):
          return f"Pokemon: {self.__name}\n Health: {self.__hp}\n Type: {self.__type} \n Stage: {self.__stage}\n"
    
if __name__ == "__main__":
    cyndaquil =  Pokemon('Fire',60,'Cyndaquil')
    pikachu =  Pokemon('Electric',50,'Pikachu')
    spoink =  Pokemon('Psychic',50,'Spoink')

    print(cyndaquil)
    print(pikachu)
    print(spoink)