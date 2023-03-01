# excellent

# ...........Constants................
birthRate = 7
deathRate = 13
ImmigrantRate = 45
currentPopulation = 312032486

# Operation
# number of seconds in one year
totalSecond = 365 * 24 * 60 * 60
totalBirthperYear = totalSecond // 7
totalDeathperYear = totalSecond // 13
totalImmigrantperYear = totalSecond // 45

newPopulationperYear = (totalBirthperYear + totalImmigrantperYear ) - totalDeathperYear

print(f'The new population number each year : {newPopulationperYear}')

newPopulationperFiveYear = newPopulationperYear * 5

print(f"The number of population after five year is {newPopulationperFiveYear + currentPopulation}")
