import math

# Length
def m_to_ft(meter):
    return round(meter * 3.3,2)

def in_to_cm(inches):
    return round(inches * 2.43,2)

def mi_to_km(mi):
    return round(mi * 1.61,2)

# Temperature
def Celsius_to_Fahr(Celsius):
    return round(((9/5)*Celsius) + 32,1)

def Fahr_to_Celsius(Fahr):
    return round((5/9)*(Fahr - 32,1))

def Celsius_to_Kel(Celsius):
    return round(Celsius + 273.15,1)

def Fahr_to_Kel(Fahr):
    return round(((5/9)*(Fahr-32))+273,1)

# Mass
def kg_to_lb(kg):
    return round(kg * 2.2,2)

def oz_to_g(oz):
    return round(oz * 28.55,2)

def ft_to_m(ft):
    return round(ft * 0.028,2)

# Volume
def ml_to_cc(ml):
    return round(ml * 1,2)

def cup_to_ml(cup):
    return round(cup * 257,2)

def gal_to_c(gal):
    return round(gal * 16,2)

def m3_to_ft3(m3):
    return round(m3 * 35.31,2)

# Pressure
def atm_to_kPa(atm):
    return round(atm * 101.3,2)

def atm_to_mmHg(atm):
    return round(atm * 760,2)

def bar_to_Pa(bar):
    return round(bar * math.pow(10,5),2)

def psi_to_mbar(psi):
    return round(68.948 * psi,2)

# Energy
def joule_to_kcal(joule):
    return round(joule * (2.39*math.pow(10,-4)),2)

def eV_to_K(eV):
    return round(eV * (1.602 * math.pow(10,19)),2)


def main():
    while True:
        topic = int(input("""
Welcome user to the Scientific Calculator:

Here is the converter option:
    1.  Length
    2.  Temper
    3.  Mass
    4.  Volume
    5.  Pressure
    6.  Energy

Enter you unit number:

"""))
        match topic:
            # The start of each case for each unit
            # ............................................................
            case 1:
                while True:
                    choice = int(input("""

Length Converter:

Choose the unit conversion you want from the option below:
    1.  m/ft
    2.  in/cm
    3.  mi/km

Enter you choice number:

"""))
                    if choice != 1 and choice != 2 and choice !=3:
                        print("Please try again")
                    else:
                        break

                match choice:
                    case 1: 
                        userValue = eval(input("Enter your length in ft: "))
                        value = m_to_ft(userValue)
                        print(f"{userValue} ft is {value} m ")
                    case 2:
                        userValue = eval(input("Enter your length in in: "))
                        value = in_to_cm(userValue)
                        print(f"{userValue} in is {value} cm ")
                    case 3:
                        userValue = eval(input("Enter your length in mi: "))
                        value = mi_to_km(userValue)
                        print(f"{userValue} mi is {value} km ")
                
            case 2: 
                while True:
                    choice = int(input("""

Temperature Converter:

Choose the unit conversion you want from the option below:
    1.  °C/°F
    2.  °F/°C
    3.  °C/K
    4.  °F/K

Enter you choice number:

"""))
                    if choice != 1 and choice != 2 and choice !=3 and choice != 4:
                        print("Please try again")
                    else:
                        break

                match choice:
                    case 1: 
                        userValue = eval(input("Enter your temperature in °C: "))
                        value = Celsius_to_Fahr(userValue)
                        print(f"{userValue} °C is {value} °F ")
                    case 2:
                        userValue = eval(input("Enter your temperature in °F: "))
                        value = Fahr_to_Celsius(userValue)
                        print(f"{userValue} °F is {value} °C")
                    case 3:
                        userValue = eval(input("Enter your temperature in °C: "))
                        value = Celsius_to_Kel(userValue)
                        print(f"{userValue} °C is {value} K")
                    case 4:
                        userValue = eval(input("Enter your temperature in °F: "))
                        value = Fahr_to_Kel(userValue)
                        print(f"{userValue} °F is {value} K")
            case 3:
                while True:
                    choice = int(input("""

Mass Converter:

Choose the unit conversion you want from the option below:
    1.  kg/lb
    2.  oz/g
    3.  ft/m

Enter you choice number:

"""))
                    if choice != 1 and choice != 2 and choice !=3:
                        print("Please try again")
                    else:
                        break

                match choice:
                    case 1: 
                        userValue = eval(input("Enter your Mass in kg: "))
                        value = kg_to_lb(userValue)
                        print(f"{userValue} kg is {value} lb ")
                    case 2:
                        userValue = eval(input("Enter your Mass in oz: "))
                        value = oz_to_g(userValue)
                        print(f"{userValue} oz is {value} g")
                    case 3:
                        userValue = eval(input("Enter your Mass in ft: "))
                        value = ft_to_m(userValue)
                        print(f"{userValue} ft is {value} m")
            case 4:
                while True:
                    choice = int(input("""

Volume Converter:

Choose the unit conversion you want from the option below:
    1.  ml/cc
    2.  cup/ml
    3.  gal/c
    4.  m³/ft³

Enter you choice number:

"""))
                    if choice != 1 and choice != 2 and choice !=3 and choice != 4:
                        print("Please try again")
                    else:
                        break

                match choice:
                    case 1: 
                        userValue = eval(input("Enter your volume in ml: "))
                        value = ml_to_cc(userValue)
                        print(f"{userValue} ml is {value} cc ")
                    case 2:
                        userValue = eval(input("Enter your volume in cup: "))
                        value = cup_to_ml(userValue)
                        print(f"{userValue} cup is {value} ml")
                    case 3:
                        userValue = eval(input("Enter your volume in gal: "))
                        value = gal_to_c(userValue)
                        print(f"{userValue} gal is {value} c")
                    case 4:
                        userValue = eval(input("Enter your volume in m³: "))
                        value = m3_to_ft3(userValue)
                        print(f"{userValue} m³ is {value} ft³")
            case 5:
                while True:
                    choice = int(input("""

Pressure Converter:

Choose the unit conversion you want from the option below:
    1.  atm/kPa
    2.  atm/mm Hg
    3.  bar/Pa
    4.  psi/mbar

Enter you choice number:

"""))
                    if choice != 1 and choice != 2 and choice !=3 and choice != 4:
                        print("Please try again")
                    else:
                        break

                match choice:
                    case 1: 
                        userValue = eval(input("Enter your pressure in atm: "))
                        value = atm_to_kPa(userValue)
                        print(f"{userValue} atm is {value} kPa")
                    case 2:
                        userValue = eval(input("Enter your pressure in atm: "))
                        value = atm_to_mmHg(userValue)
                        print(f"{userValue} atm is {value} mm Hg")
                    case 3:
                        userValue = eval(input("Enter your pressure in bar: "))
                        value = bar_to_Pa(userValue)
                        print(f"{userValue} bar is {value} Pa")
                    case 4:
                        userValue = eval(input("Enter your pressure in psi: "))
                        value = psi_to_mbar(userValue)
                        print(f"{userValue} psi is {value} mbar")
            case 6:
                while True:
                    choice = int(input("""

Energy Converter:

Choose the unit conversion you want from the option below:
    1.  J/kcal
    2.  eV/K

Enter you choice number:
"""))               
                    if choice != 1 and choice != 2:
                        print("Please try again")
                    else:
                        break
                    
                match choice:
                    case 1: 
                        userValue = eval(input("Enter your energy in Joule: "))
                        value = joule_to_kcal(userValue)
                        print(f"{userValue} J is {value} kcal ")
                    case 2:
                        userValue = eval(input("Enter your energy in eV: "))
                        value = eV_to_K(userValue)
                        print(f"{userValue} eV is {value} K")
        finalChoice = str(input("Would you like to convert something else (Y/N): ")).lower()
        if finalChoice != "y":
            break 


main()