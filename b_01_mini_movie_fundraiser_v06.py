# Imports...
import pandas as pd

# Functions...

# Checks if user has entered yes / no to a question
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("\nPlease answer yes / no")


# Calculate the ticket price based on user's age
def calc_ticket_price(user_age):

    # Ticket price is $7.50 for users under 16
    if user_age < 16:
        price = 7.5

    # Ticket price is $10.50 for users between 16 and 64
    elif 16 <= user_age < 65:
        price = 10.5

    # Ticket price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price


# Checks for a blank user name
def not_blank(question):

    while True:

        # The user's input
        response = input(question)

        # Checking if user has entered empty text
        if response == "":
            print("\nSorry, this can't be blank. please try again")
        else:
            return response


# Checks if a user enters an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("\nPlease enter an integer")


# Asks user if they would like to use cash or credit
def cash_credit(question):

    while True:
        response = input(question).lower()

        # If the user enters the cash option
        if response == "cash" or response == "ca":
            return "cash"

        # If the user enters the credit option
        elif response == "credit" or response == "cr":
            return "credit"

        # If the user doesn't enter any of the payment options
        else:
            print("\nPlease choose a valid payment method.")


# Checks that users enter a valid response (e.g yes / no
# Cash / credit) based on a list of options
def string_checker(question, num_letters, valid_response):

    # Error message
    error = f"\nPlease choose {valid_response[0]} or {valid_response[1]}"

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:

        # User's response to the question
        response = input(question).lower()

        # Looks for matches in the user's
        # response and the desired response
        for item in valid_response:
            if response == item[:short_version] or response == item:
                return item

        # Prints message if there were no matches found.
        print(error)


# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Main routine...


# Set maximum number of tickets below
MAX_TICKETS = 100
tickets_sold = 0

# Options listed
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Dictionaries used to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# History of the users that bought a ticket
mini_movie_dict = {
    "Name": all_names,
    "Ticket price": all_ticket_costs,
    "Surcharge": all_surcharge,
}

# Ask user if they want to see the instructions
want_instructions = string_checker("\nDo you want to read the "
                                   "instructions?\n~~~ ", 1, yes_no_list)

if want_instructions == "yes":
    print("\nInstructions go here...")

print("\bProgram continues...\n")

# Loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("\nPlease enter your name"
                     " or 'xxx' to quit.\n~~~ ")

    # If user types xxx
    if name == "xxx":
        break

    # Age of user
    age = num_check("\nAge: ")

    # User age conditional checking
    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("\nSorry, you are too young for this movie")
        continue
    else:
        print("\n?? That looks like a type, please try again")
        continue

    # Calculate ticket cost
    ticket_cost = calc_ticket_price(age)

    print("\nage: {}, ticket price: ${:.2f}".format(age, ticket_cost))

    # Get payment method
    payment_method = cash_credit("\nChoose a payment method (cash"
                                 " or credit)\n~~~ ")

    if payment_method == "cash":
        surcharge = 0
    else:
        # Calculate 5% surcharge if users are paying by credit card
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    # add ticket name, cost and surcharge to lists
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

    # Plugging in the data into a data frame/sheet
    mini_movie_data = pd.DataFrame(mini_movie_dict)
    mini_movie_data = mini_movie_data.set_index("Name")

    # Calculate the total ticket cost (ticket + surcharge)
    mini_movie_data["Total"] = mini_movie_data["Surcharge"] \
                               + mini_movie_data["Ticket price"]

    # Calculate the profit for each ticket
    mini_movie_data["Profit"] = mini_movie_data["Ticket price"] - 5

    # Calculate total values of tickets and profits
    total = mini_movie_data["Total"].sum()
    profit = mini_movie_data["Profit"].sum()

    # Currency formatting (uses currency)
    add_dollars = ["Ticket price", "Surcharge", "Total", "Profit"]

    # Adding dollar signs
    for var_item in add_dollars:
        mini_movie_data[var_item] = mini_movie_data[var_item].apply(currency)

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("\nCongratulations! You have sold all the tickets,")
else:
    print("\nYou have sold {} tickets. There is {} tickets "
          "remaining.".format(tickets_sold, MAX_TICKETS-tickets_sold))
