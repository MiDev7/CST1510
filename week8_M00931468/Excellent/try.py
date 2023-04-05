# def test_input(error=0):
#     while True:
#         try:
#             binary = int(input("Enter a binary number: "))
#         except ValueError:
#             print("Input only binary digits")
#             continue
#         else:
#             for bit in str(binary):
#                 if bit != "0" and bit != "1":
#                     error+=1

#             print(error)
#             if error != 0:
#                 print("Binary number should consists of only 0 and 1, Please try again ...")
#                 return test_input(error)
#             else:
#                 return binary



# print(test_input())
while True:
    try:
        binary = input("Enter a binary number: ")
        int(binary, 2)
    except:
        print("Binary number should consists of only 0 and 1, Please try again ...")
        continue
    else:
        break