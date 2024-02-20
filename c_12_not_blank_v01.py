# Functions...

# A function that checks if user input is blank
def not_blank(question):

    # The user's input
    response = input(question)

    # Checking if user has entered empty text
    if question == "":
        print("\nSorry, this can't be blank. please try again")
    else:
        return response

# Main routine...

while True:
    name = not_blank("\nEnter your name (or 'xxx' to quite)\n~~~ ")