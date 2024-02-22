# Functions...

# Checks if a user enters an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("\nPlease enter an integer")


# Main routine...
