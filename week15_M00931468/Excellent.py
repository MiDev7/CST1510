doors = { f"Door{key}":False for key in range(1,101)}


for index in range(1,101):
    for door_key, door_value in doors.items():
        if door_value == False:
            doors[door_key] = True
        elif door_value == True:
            doors[door_key] = False
print(doors)


