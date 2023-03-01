import math


# Distance between Two Points on Earth
latitude1, longitude1 = map(float, input('Enter the first coordinate:\n').split(sep=','))
latitude2, longitude2 = map(float, input('Enter the second coordinate:\n').split(sep=','))

# constant
avgRadius = 6371.01


distance = avgRadius * (math.acos((math.sin(math.radians(latitude1)) * math.sin(math.radians(
    latitude2))) + math.cos(math.radians(latitude1)) * math.cos(math.radians(latitude2)) * math.cos(math.radians(longitude1 - longitude2))))

print(f'The distance between ({latitude1},{longitude1}) and ({latitude2},{longitude2}) is: {round(distance,0)} km')

# 7.08033,160.82400
# -36.33734,-93.44500