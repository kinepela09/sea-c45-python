donor_list = {
    "Bill Gates": [1.00, 11.00, 111.00],
    "Elon Musk": [2.00],
    "Paul Allan": [3.00, 6.00, 9.00]
}


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
        if not(thank_you_input in donor_list.keys()):
            donor_list[thank_you_input] = []

        get_donation_amt(thank_you_input)
        donation = last_donation(thank_you_input)
        thank_you_template(thank_you_input, donation)


def thank_you_template(d, donation):

    outfile = open((d.replace(' ', '_') + '.txt'), 'w')

    print()
    print("Dear %s," % d)
    print()
    print("Thank you so much for your kind donation of $%s. We here at "
            "the Foundation for Homeless Whales greatly appreciate it. "
            "Your money will go towards creating new oceans on the moon for"
            "whales to live in." % format(donation, '.2f'))
    print()
    print("Thanks again,")
    print()
    print("Jim Grant")
    print()
    print("Director, F.H.W.")
    print()

    outfile.close


def donation_sum(d):
    amt = 0
    for i in range(len(donor_list[d])):
        amt = amt + donor_list[d][i]

    return amt


def last_donation(d):

    return int(donor_list[d][len(donor_list[d]) - 1])


def get_donation_amt(d):

    donation_amt = input("Enter donation amount: ")

    if donation_amt.upper() == "QUIT":
        print("Returning to Main Menu")
        main_menu()

    try:
        donation_amt = float(donation_amt)
        add_donation(d, donation_amt)

    except ValueError:
        print("Invalid amount")
        get_donation_amt(d)


def add_donation(d, a):

    donor_list[d].append(a)


def print_donor_names(dl):

    for i in dl:
        print(i)

    return thank_you()


def create_report():
    print("{0:<15}".format("Name"), "{0:<10}".format("Total"), "{0:<4}".format("#"), "{0:<10}".format("Average"))
    for i in donor_list:
        name = i
        total = donation_sum(i)
        donation_count = len(donor_list[i])
        print("{0:<15}".format(name), "${0:<10}".format(total), "{0:<4}".format(donation_count), "${0:<10}".format(total / donation_count))
    print()


if __name__ == '__main__':
    main_menu()
