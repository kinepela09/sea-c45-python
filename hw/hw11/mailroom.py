donor_list = [
    ['Bill Gates', 1.00, 10.00, 100.00],
    ['John Doe', 2.00, 4.00, 6.00],
    ['Jane Doe', 3.00, 6.00, 10.00]
]

def print_intro():
    """
    """
    print()
    print("Welcome to Mailroom Madness")
    print()
    print("Choose from the following:")
    print()
    print("T - Send a (T)hank You Letter")
    print()
    print("R - Create a (R)eport")
    print()
    print("quit - Quit the program")
    print()


def main_menu():
    """

    """
    print_intro()

    user_input = input(" ")
    user_input = user_input.upper()

    if user_input == "T":
        send_thank_you()
    elif user_input == "R":
        create_report()
    elif user_input == "QUIT":
        return False
    else:
        print("Invalid input, please try again.")
        return main_menu()

def send_thank_you():
    """
    Prompts user for a full name.
    If name is not in list, name will be added to donor list.

    Input "list" will output list of donor names.
    """
    user_input = input("Please enter a donor's full name, 'list', or 'quit': ")
    str_input = str(user_input)

    if str_input.upper() == "LIST":
        for i in donor_list:
            print(i[0])
        return send_thank_you()
    elif user_input == "QUIT":
        return False
    else:
        if isDonor(user_input):

        else:
            addDonor(user_input)


def print_donor_list(dl):
    for donor in dl:
        print(donor[0])
    return send_thank_you()

def get_donation_amt():
    amt = input("Please enter donation amount: ")
    if float(donation):
        return amt
    else:
        print("Invalid donation amount.")
        return get_donation_amt()

def create_letter(s, f):
    """
    """
    print()
    print("Dear %s," % s)
    print()
    print("Thank you so much for your kind donation of $%f. We here at the Foundation "
        "for Homeless Whales greatly appreciate it. Your money will go towards creating "
        "new oceans on the moon for whales to live in." % d)
    print()
    print("Thanks again,")
    print()
    print("Jim Grant")
    print()
    print("Director, F.H.W.")
    print()

while True:
  main_menu()
