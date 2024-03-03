# Functions...

# Calculate the ticket price based on user's age
def calc_ticket_price(user_age):

    # Ticket price is $7.50 for users under 16
    if user_age < 16:
        price = 7.5

    # Ticket price is $10.50 for users between 16 and 64
    elif 16 < user_age < 65:
        price = 10.5

    # Ticket price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price


# Main routine...

# Loop for testing
while True:

    # Get age from user ( assuming the user entered a valid integer
    age = int(input("\nAge: "))
    # Calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print("\nage: {}, ticket price: ${:.2f}".format(age, ticket_cost))
