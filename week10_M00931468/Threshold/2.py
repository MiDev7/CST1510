sizes = tuple(['XS', 'S', 'M', 'L', 'XL', 'XXL'])

filedir = '/home/midev/Desktop/Python/CST1510/week10_M00931468/clothing_stock.txt'
sizesDict = {}
xs, s, m, l, xl, xxl = 0, 0, 0, 0, 0, 0

with open(filedir, 'r') as lines:

    for line in lines:
        size = line.split(',')[-1]
        match size.strip():
            case 'XS':
                xs += 1
                sizesDict[sizes[0]] = xs
            case 'S':
                s += 1
                sizesDict[sizes[1]] = s
            case 'M':
                m += 1
                sizesDict[sizes[2]] = m
            case 'L':
                l += 1
                sizesDict[sizes[3]] = l
            case 'XL':
                xl += 1
                sizesDict[sizes[4]] = xl 
            case 'XLL':
                xxl += 1
                sizesDict[sizes[5]] = xxl

print("Here is the total of wears in each sizes:")

for keys, values in sizesDict.items():
    print(f"{keys}: {values}")