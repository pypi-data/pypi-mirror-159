def even_number_count(number):
    count = 0
    for item in range(1, number+1):
        if item % 2 == 0:
            # print(item)
            count += 1

    return(f"There are {count} even numbers")


number = int(input("Enter the number: "))
output = even_number_count(number)
print(output)
