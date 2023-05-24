class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    
    def __init__(self,speed : int = SLOW, state : bool = False, radius : int = 5, colour : str = 'blue'):
        self.__speed = speed
        self.__state = state
        self.__radius = radius
        self.__colour = colour

    # Getters

    def get_speed(self):
        return self.__speed
    
    def get_state(self):
        return self.__state
    
    def get_radius(self):
        return self.__radius
    
    def get_colour(self):
        return self.__colour
    
    # Setters

    def set_speed(self, new_speed : int):
        if new_speed == Fan.SLOW or new_speed == Fan.MEDIUM or new_speed == Fan.FAST:
            self.__speed = new_speed
            print("The speed of your fan has been changed")
            return False
        else:
            return True
        
    def set_state(self, new_state : bool):
        self.__state = new_state

    def set_radius(self, new_radius : int):
        self.__radius = new_radius

    def set_colour(self, new_colour : str):
        self.__colour = new_colour

    def __str__(self) -> str:
        if self.__state == True:
            return f"The Fan is On, \nColour:{self.__colour} \nSpeed:{self.__speed} \nRadius:{self.__radius} \n"
        
        if self.__state == False:
            return f"The Fan is Off, \nColour:{self.__colour}   \nRadius:{self.__radius} \n"
    
        
    
if __name__ == "__main__":
    Fan1 = Fan(Fan.FAST,True,12,'green')
    Fan2 = Fan(Fan.MEDIUM,False,6,'red')
    print(Fan1)
    print(Fan2)