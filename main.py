def ratio():
    try:
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
    except ValueError:
        print("Please, enter down your old")
    except TypeError:
        print("Please, enter number!")


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
    except TypeError:
        print("Please, enter number!")


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
    except TypeError:
        print("Please, enter number!")


def average_number():
    try:
        user_input_first = int(input("Your first number: "))
        user_input_second = int(input("Your second number: "))
        user_input_third = int(input("Your third number: "))

        list_sort = [user_input_first, user_input_second, user_input_third]

        list_sort.sort()

        print(list_sort[1])

    except ValueError:
        print("Please, enter number!")
    except TypeError:
        print("Please, enter number!")


# average_number()


def number_of_days():
    try:
        month = int(input("Month: "))

        list31 = [1, 3, 5, 7, 8, 10, 12]

        if month > 12 or month <= 0:
            print("Xaxaxaxaxxaxaxaxaxxa, you are prankster. There are only 12 months in a year")
        elif month in list31:
            print("31")
        elif month == 2:
            print("28")
        else:
            print("30")

    except ValueError:
        number_of_days()
    except TypeError:
        print("Xaxaxaxaxxaxaxaxaxxa, you are prankster")


# number_of_days()


def weigh_in_ceremony():
    try:
        weight = int(input("Weight: "))

        if weight < 60:
            print("Light weight")
        elif 60 <= weight <= 64:
            print("First welterweight")
        elif 64 < weight <= 69:
            print("Welterweight")
    except ValueError:
        print("Come on, in function number of day, we saw that you're a prankster, very funny.")
    except TypeError:
        print("Come on, in function number of day, we saw that you're a prankster, very funny.")


# weigh_in_ceremony()

def password():
    user_password = input("Password: ")
    again = input("Repeat the password: ")

    if user_password == again:
        print("Password accepted")
    elif user_password != again:
        print("Password not accepted")
        password()


# password()

def odd_and_even():
    try:
        number = int(input("Number: "))

        if number in range(1, 10000, 2):
            print("Odd number")
        elif number in range(2, 1000, 2):
            print("Even number")

    except ValueError:
        print("If you don't stop do that, I'll stop start the functions!")
    except TypeError:
        print("If you don't stop do that, I'll stop start the functions!")


def the_smallest_of_two_numbers():
    try:
        first_number = int(input("First number: "))
        second_number = int(input("Second number: "))

        lists = [first_number, second_number]

        for list_for_request in lists:
            if list_for_request == '\n':
                print("I'm not gonna ask you twice.")
                print("If you don't stop doing this, I'll stop running functions!,"
                      " I think you have learned your lesson")
                return None

        print(min(lists))

    except ValueError:
        print("I'm not gonna ask you twice.")
    except TypeError:
        print("If you don't stop doing this, I'll stop running functions!")


# the_smallest_of_two_numbers()

def age_group():
    try:
        age = int(input("Weight: "))

        if age <= 13:
            print("Inclusive-childhood;")
        elif 14 <= age <= 24:
            print("Adolescence")
        elif 25 <= age <= 59:
            print("Maturity")
        elif 60 <= age:
            print("Old age")

    except ValueError:
        print("You're an idiot!")
    except TypeError:
        print("You're an idiot in square one.")


# age_group()

def triangle_view():
    try:
        triangle_edges_first = int(input("Triangle edges: "))
        triangle_edges_second = int(input("Triangle edges: "))
        triangle_leg = int(input("Triangle: "))

        if triangle_edges_first == triangle_edges_second:
            print("Isosceles")

        elif triangle_edges_first == triangle_leg == triangle_edges_second:
            print("Equilateral")

        else:
            print("Versatile")
    except ValueError:
        print("'Call the nuthouse'"
              "\n'Hello'."
              "\n'Home for the mentally ill, what can I do for you?'"
              "\n'We have a patient for you.'")


triangle_view()
