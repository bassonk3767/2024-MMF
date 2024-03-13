# Functions...

# A function that checks if user input is blank
def not_blank(question):

    # Looping to get user's answer
    while True:

        # The user's input
        response = input(question).strip()

        # Checking if user has entered empty text
        if response == "":
            print("\nSorry, this can't be blank. please try again")
        else:
            return response

# Main routine...

# Loop to get user's name
while True:

    # User gets asked for their name
    name = not_blank("\nEnter your name (or 'xxx' to quite)\n~~~ ")

    if name == "xxx":
        break

    print("\nProgram continues...")

print("\nWe are done")