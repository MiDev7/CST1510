import math

# Length
m_to_ft = lambda meter: round(meter * 3.3,2)
in_to_cm = lambda inches: round(inches * 2.43,2)
mi_to_km = lambda mi: round(mi * 1.61,2)

# Temperature
Celsius_to_Fahr = lambda Celsius: round(((9/5)*Celsius) + 32,1)
Fahr_to_Celsius = lambda Fahr: round((5/9)*(Fahr - 32,1))
Celsius_to_Kel = lambda Celsius: round(Celsius + 273.15,1)
Fahr_to_Kel = lambda Fahr: round(((5/9)*(Fahr-32))+273,1)

# Mass
kg_to_lb = lambda kg: round(kg * 2.2,2)
oz_to_g = lambda oz: round(oz * 28.55,2)
ft_to_m = lambda ft: round(ft * 0.028,2)

# Volume
ml_to_cc = lambda ml: round(ml * 1,2)
cup_to_ml = lambda cup: round(cup * 257,2)
gal_to_c = lambda gal: round(gal * 16,2)
m3_to_ft3 = lambda m3: round(m3 * 35.31,2)

# Pressure
atm_to_kPa = lambda atm: round(atm * 101.3,2)
atm_to_mmHg = lambda atm: round(atm * 760,2)
bar_to_Pa = lambda bar: round(bar * math.pow(10,5),2)
psi_to_mbar = lambda psi: round(68.948 * psi,2)

# Energy
joule_to_kcal = lambda joule: round(joule * (2.39*math.pow(10,-4)),2)
eV_to_K = lambda eV: round(eV * (1.602 * math.pow(10,19)),2)

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