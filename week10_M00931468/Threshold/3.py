# Case insensitive
# def count_unique(text):
#     count = 0
#     unique = []
#     for char in text:
#         if char.upper() not in unique and char.lower() not in unique:
#             unique.append(char)
#             count+=1
    
#     return count

# def main(): 
#     word = input("Enter a word:")
#     print(count_unique(word))

# main()

# def count_unique(text):
#     count = 0
#     chars = set()
#     for char in text:
#         chars.add(char)
    
#     return len(chars)

# def main(): 
#     word = input("Enter a word:")
#     print(count_unique(word))

# main()

def count_unique(text):

    chars = set()
    for char in text:
        chars.add(char)
    
    return len(chars)

def main(): 
    word = input("Enter a word:")
    print(count_unique(word))

main()

