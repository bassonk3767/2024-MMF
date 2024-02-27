# Functions...

# Checks if a user enters an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("\nPlease enter an integer")


# Main routine..

tickets_sold = 0

while True:

    # Get user's name
    name = input("\nEnter your name or 'xxx' to quite\n~~~ ")

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

    tickets_sold += 1