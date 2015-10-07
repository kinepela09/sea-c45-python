donor_list = [
<<<<<<< HEAD
    ['Bill Gates', 1.00, 10.00, 100.00],
    ['John Doe', 2.00, 4.00, 6.00],
    ['Jane Doe', 3.00, 6.00, 10.00]
]

def print_intro():
    """
    """
=======
    ["Bill Gates", [1.00, 11.00, 111.00]],
    ["Elon Musk", [2.00]],
    ["Paul Allan", [3.00, 6.00, 9.00]]
]


def main_menu():

>>>>>>> 7175cb62b811746b468700287fd21e68df6465dc
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

<<<<<<< HEAD

def main_menu():
    """

    """
    print_intro()

    user_input = input(" ")
    user_input = user_input.upper()

    if user_input == "T":
        send_thank_you()
=======
    user_input = input("> ")
    user_input = user_input.upper()

    if user_input == "T":
        thank_you()
>>>>>>> 7175cb62b811746b468700287fd21e68df6465dc
    elif user_input == "R":
        create_report()
    elif user_input == "QUIT":
        return False
    else:
<<<<<<< HEAD
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
=======
        print("Invalid input, try again")
        main_menu()

    input("Press Enter to continue...")
    main_menu()


def thank_you():

    print('Enter a full name, "list", or "quit".')
    thank_you_input = input("> ")
    thank_you_input_str = thank_you_input.upper()

    if thank_you_input_str == "QUIT":
        print("Returning to Main Menu.")
        main_menu()
    elif thank_you_input_str == "LIST":
        print_donor_names(donor_list)
    else:
        print(thank_you_input)
        if name_in_list(thank_you_input_str, donor_list):
            print(name_in_list(thank_you_input_str, donor_list))
        else:
            donor_list.append([thank_you_input, []])

        get_donation_amt(thank_you_input_str, donor_list)
        total = donation_sum(thank_you_input_str, donor_list)
        thank_you_template(thank_you_input, total)


def thank_you_template(d, t):

    print()
    print("Dear %s," % d)
    print()
    print("Thank you so much for your kind donation of $%s. We here at "
            "the Foundation for Homeless Whales greatly appreciate it. "
            "Your money will go towards creating new oceans on the moon for"
            "whales to live in." % format(t, '.2f'))
>>>>>>> 7175cb62b811746b468700287fd21e68df6465dc
    print()
    print("Thanks again,")
    print()
    print("Jim Grant")
    print()
    print("Director, F.H.W.")
    print()

<<<<<<< HEAD
while True:
  main_menu()
=======

def donation_sum(d, dl):
    amt = 0
    for i in dl:
        if d == i[0].upper():
            for j in i[1]:
                amt = amt + j

    return amt


def get_donation_amt(d, dl):

    donation_amt = input("Enter donation amount: ")

    if donation_amt.upper() == "QUIT":
        print("Returning to main menu")
        main_menu()

    try:
        donation_amt = float(donation_amt)
        add_donation(d, dl, donation_amt)
    except ValueError:
        print("Invalid amount")
        get_donation_amt(d, dl)


def add_donation(d, dl, a):

    for i in dl:
        if d.upper() == i[0].upper():
            i[1].append(a)


def name_in_list(s, dl):

    for i in dl:
        if i[0].upper() == s:
            return True

    return False


def print_donor_names(dl):

    for i in dl:
        print(i[0])

    return thank_you()


def create_report():
    print("{0:<15}".format("Name"), "{0:<10}".format("Total"), "{0:<4}".format("#"), "{0:<10}".format("Average"))
    for i in donor_list:
        name = i[0]
        total = donation_sum(i[0].upper(), donor_list)
        donation_count = len(i[1])
        print("{0:<15}".format(name), "{0:<10}".format(total), "{0:<4}".format(donation_count), "{0:<10}".format(total/donation_count))
    print()


if __name__ == '__main__':
    main_menu()
>>>>>>> 7175cb62b811746b468700287fd21e68df6465dc
