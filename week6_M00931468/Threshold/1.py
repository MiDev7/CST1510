def main():
    num_list = []
    num = int(input("Enter an integer (enter 0 to end input): "))

    while num != 0:
        num_list.append(num)
        num = int(input("Enter an integer (enter 0 to end input): "))

    print("\nInput values (in reverse order):")
    for integer in range(len(num_list)-1, -1, -1):
        print(num_list[integer])

main()