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
    chess_board = 9
    numbering = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    letter = ["   a", "b", "c", 'd', "e", "f", "g", "h"]

    def first_move():
        for i in range(chess_board):
            numbers = numbering[i]

            if i == 8:
                for a in letter:
                    print(a, end=" ")
                break

            for j in range(chess_board):
                if numbers == numbering[i]:
                    print(numbers, end=". ")
                    numbers += 1

                elif i == 4 and j == 4:
                    print(end="  ")
                    continue

                elif (i + j) % 2 != 0:
                    print("■", end=" ")

                elif (i + j) % 2 == 0:
                    print("□", end=" ")
            print()

    first_move()

    letters_and_numbers = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8
    }

    def second_and_other_move(user_move_number, user_move_letter):

        try:
            user_move_number = int(input("\nYour move by number: "))
            user_move_letter = str(input("Your mover by letter: ")).lower()
            user_move_number = user_move_number - 1
        except ValueError:
            print("Please do what is written in input")

        if user_move_number <= 8 and user_move_letter is not letters_and_numbers.keys():
            print("You can't move")
            dauletsuper = False
            return

        for i in range(0, chess_board):
            numbers = numbering[i]

            if i == 8:

                for a in letter:
                    print(a, end=" ")
                break

            for j in range(chess_board):

                if numbers == numbering[i]:
                    print(numbers, end=". ")
                    numbers += 1

                elif i == user_move_number and j == letters_and_numbers[f'{user_move_letter}']:
                    print(end="  ")
                    continue

                elif (i + j) % 2 != 0:
                    print("■", end=" ")

                elif (i + j) % 2 == 0:
                    print("□", end=" ")
            print()


rook_move()
