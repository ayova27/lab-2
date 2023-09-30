def ratio():
    user_input = int(input("Input: "))
    default_number = 999

    if user_input > default_number:
        thousand = user_input // 1000
        hundred = (user_input // 100) % 10
        ten = (user_input - ((hundred * 100) + (thousand * 1000))) // 10
        one = user_input - ((ten * 10) + (hundred * 100) + (thousand * 1000))
        if (thousand + one) == (hundred - ten):
            print("Yes!")
        else:
            print("No!")

# ratio()

def roskomnadzor():
    try:
        user_age = int(input("How old are you: "))
        if user_age >= 18:
            print("Access denied!")
        elif user_age < 18:
            print("Access is allowed!")
    except ValueError:
        print("Please, enter down your old")


# roskomnadzor()

def 