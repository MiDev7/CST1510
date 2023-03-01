import math

# Area of Pentagon
side = int(input('Enter the length of the side of your pentagon:\n '))

area  = (5 * math.pow(side,2))/(4 * math.tan(math.pi/5))

print(f'THe area of your pentagon of {side} of side is {round(area,2)} .')