donor_list = [
    ['Bill Gates', 1.00, 10.00, 100.00],
    ['John Doe', 2.00],
    ['Jane Doe', 3.00, 6.00, 10.00]
]

def print_intro():
    """
    Introduction output
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

def print_donors(d):
  """
  Print donor history in table format.
  Displays name, total, number, and average donations.
  """
  for curr in d:
    curr_name = curr[0]
    donation_count = len(curr) - 1
    donation_total = 0
    j = 1
    while j <= donation_count:
      donation_total = donation_total + curr[j]
      j = j + 1

    print(curr_name, donation_total, donation_count, donation_total/donation_count)

def send_thank_you():
    """
    """
    donor_name = input("Please enter a donor's full name: ")
    str_donor = str(donor_name).upper

    if str_donor == "LIST":
        print_donor_list(donor_list)
    elif donor_name == "QUIT":
        return False
    else:
        donation_amt = get_donation_amt()
        create_letter(donor_name, donation_amt)

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


def main_menu():
    """

    """
    print_intro()

    user_input = input("> ")
    user_input = user_input.upper()

    if user_input == "T":
      send_thank_you()
    elif user_input == "R":
      create_report(donor_list)
    elif user_input == "QUIT":
        return False
    else:
      print("Invalid input.")
      main_menu()


main_menu()
