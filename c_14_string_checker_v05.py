# Functions...

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
            if response == item[:num_letters] or response == item:
                return item

        # Prints message if there were no matches found.
        print(error)


# Main routine...

# Options listed
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

for case in range(0, 5):
    want_instructions = string_checker("\nDo you want to read the"
                                       "instructions?", 1, yes_no_list)
    print(f"You chose {want_instructions}")
