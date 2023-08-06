def fizz_buzz_game(number):

    if number % 15 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return 'buzz'
    elif number % 5 == 0:
        return"fizz"
    else:
        return number


if __name__ == "__main__":
    number = int(input("enter the value: "))
    output = fizz_buzz_game(number)
    print(output)
