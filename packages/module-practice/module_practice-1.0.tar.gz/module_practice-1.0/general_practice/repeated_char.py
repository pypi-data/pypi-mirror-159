def most_repeated_char(char):
    emptydict = {}
    for item in char:

        count = emptydict.get(item, 0)
        count += 1
        emptydict[item] = count

    list = sorted(emptydict.items(), key=lambda item: item[1], reverse=True)
    return f" the most repeated character is {list[0]}"


char = input("enter the string : ")
character = most_repeated_char(char)
print(character)
