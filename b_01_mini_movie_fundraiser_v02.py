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

# Main routine...


# Set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

# Ask user if they want to see the instructions
want_instructions = yes_no("\nDo you want to read the "
                           "instructions?\n~~~ ")

if want_instructions == "yes":
    print("\nInstructions go here...")

print("\bProgram continues...\n")

# Loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("\nPlease enter your name"
                     " or 'xxx' to quit.\n~~~ ")

    if name == "xxx":
        break

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("\nCongratulations! You have sold all the tickets,")
else:
    print("\nYou have sold {} tickets. There is {} tickets "
          "remaining.".format(tickets_sold,MAX_TICKETS-tickets_sold))
