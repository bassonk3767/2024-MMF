# Functions...

def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("\nPlease answer yes / no")

# Main routine...

while True:
    want_instructions = yes_no("\n\nWould you like to read"
                               "the instructions?\n~~~ ")

    if want_instructions == "yes":
        print("\nInstructions go here...")

    print("\nProgram continues...")