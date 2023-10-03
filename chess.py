def print_board():
    chess_board = 9
    numbering = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    letter = ["   a", "b", "c", 'd', "e", "f", "g", "h"]

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


def second_and_other_move():
    chess_board = 9
    numbering = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    letter = ["   a", "b", "c", 'd', "e", "f", "g", "h"]

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

    default_position_number = 4
    default_position_letter = 'd'

    user_move_number = 4
    user_move_letter = "d"

    try:
        print("""\nIf you want a horizontal move, enter 1. If you want a vertical move, enter 2.
What are you want (horizontal or vertical): 
""")
        user_move = int(input())

        if user_move == 1:
            user_move_number = int(input("\nYour move by number: "))
            user_move_number = user_move_number - 1

            if user_move_number >= default_position_number:
                print("You can't move that!")
                return

        elif user_move == 2:
            user_move_letter = str(input("Your move by letter: ")).lower()

            if user_move_letter not in "abcdefgh":
                print("You can't move that!")
                return

    except ValueError:
        print("Please enter a valid input.")

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

            elif i == user_move_number and j == letters_and_numbers[user_move_letter]:
                print(end="  ")
                continue

            elif (i + j) % 2 != 0:
                print("■", end=" ")

            elif (i + j) % 2 == 0:
                print("□", end=" ")
        print()

    again = str(input("Do you want another move? (y/n): "))
    if again == "y":
        default_position_number = user_move_number
        default_position_letter = user_move_letter
        second_and_other_move()

    elif again == "n":
        print("Bye!")


def rook_move():
    print_board()
    second_and_other_move()


# rook_move()

def king():
    chess_board = 9
    numbering = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    letter = ["   a", "b", "c", 'd', "e", "f", "g", "h"]

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


def king_move():
    default_position_letter = 4
    default_position_number = 4

    boundary = 4

    numbering = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    letter = ["   a", "b", "c", 'd', "e", "f", "g", "h"]

    print("""\nIf you want a vertical move, enter 1. If you want a horizontal move, enter 0.
    What do you want (horizontal or vertical): """)

    user = int(input())

    if user != 0 and user != 1:
        print("Invalid input. The king cannot go more than one square.")
        king_move()

    move = int(input("You want to move backward or forward? (0 for backward, 1 for forward): "))

    if move != 0 and move != 1:
        print("Invalid input. The king cannot go more than one square.")
        king_move()

    if user == 1:
        if move == 1:
            boundary += 1
        elif move == 0:
            boundary -= 1

        if boundary < 0 or boundary > 8:
            print("You leave board boundary")
            king_move()

    elif user == 0:
        if move == 1:
            default_position_number += 1
        elif move == 0:
            default_position_number -= 1

        if default_position_number < 0 or default_position_number >= 9:
            print("You leave board boundary")
            return None

    chess_board = 9

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
            elif i == default_position_number and j == boundary:
                print(" ", end=" ")
            elif (i + j) % 2 != 0:
                print("■", end=" ")
            elif (i + j) % 2 == 0:
                print("□", end=" ")
        print()


def start():
    king()
    king_move()
