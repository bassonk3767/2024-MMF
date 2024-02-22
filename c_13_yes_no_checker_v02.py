# Functions...

# Yes no checker
def yes_no(question):

    # Looping to get the user's answer
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("\nPlease answer yes / no")
