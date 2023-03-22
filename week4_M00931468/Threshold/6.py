def multTable():
    for num in range(0,10):
        for index in range(0,10):
            print(f"{index* num}", end="\t")
        print("\n")


def main():
    multTable()

main()