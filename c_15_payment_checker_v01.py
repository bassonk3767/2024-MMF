# Functions...

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
            print("\nPlease choose a valid payment method")


# Main routine...

while True:
    payment_method = cash_credit("\nChoose a payment method (cash"
                                 "or credit)\n~~~ ")
