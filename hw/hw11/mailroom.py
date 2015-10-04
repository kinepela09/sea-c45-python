donor_list = [
    ["Bill Gates", [1.00, 11.00, 111.00]],
    ["Elon Musk", [2.00]],
    ["Paul Allan", [3.00, 6.00, 9.00]]
]


def main_menu():

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

    user_input = input("> ")
    user_input = user_input.upper()

    if user_input == "T":
        thank_you()
    elif user_input == "R":
        create_report()
    elif user_input == "QUIT":
        return False
    else:
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
            print("name not in list. need to add")
            donor_list.append([thank_you_input, []])
            last = len(donor_list) - 1
            print(donor_list[last])

        get_donation_amt(thank_you_input_str, donor_list)
        total = donation_sum(thank_you_input_str, donor_list)
        print(total)
        thank_you_template(thank_you_input, total)


def thank_you_template(d, t):

    print()
    print("Dear %s," % d)
    print()
    print("Thank you so much for your kind donation of $%s. We here at "
            "the Foundation for Homeless Whales greatly appreciate it. "
            "Your money will go towards creating new oceans on the moon for"
            "whales to live in." % format(t, '.2f'))
    print()
    print("Thanks again,")
    print()
    print("Jim Grant")
    print()
    print("Director, F.H.W.")
    print()


def donation_sum(d, dl):
    amt = 0
    for i in dl:
        if d == i[0].upper():
            for j in i[1]:
                print(j)
                amt = amt + j

    return amt


def get_donation_amt(d, dl):

    donation_amt = input("Enter donation amount: ")

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
    pass

main_menu()
