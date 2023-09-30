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

def arithmetic_progression():
    try:
        user_input_number = int(input("First number: "))
        user_input_number2 = int(input("Second number: "))
        user_input_number3 = int(input("Third number: "))

        if (user_input_number + user_input_number2) == user_input_number3:
            print("Yes!")
        else:
            print("No!")
    except ValueError:
        print("Please, enter number!")


def rook_move():
    chess_board = 8

    for i in range(chess_board):
        for j in range(chess_board):
            if i == 5 and j == 4:
                continue
            if (i + j) % 2 == 0:
                print("■", end=" ")
            else:
                print("□", end=" ")
        print()

rook_move()