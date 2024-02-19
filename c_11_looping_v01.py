# Functions...

# Main routine...

# Set maximum number of tickets
MAX_TICKETS = 3

# Loop to sell tickets to user
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("\nPlease enter your name"
                 "or 'xxx' to quite.\n~~~ ")

    if name == "xxx" or name == "XXX":
        break

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("\nCongratulations! You have sold all the tickets,")
else:
    print("\nYou have sold {} tickets. There is {} tickets "
          "remaining.".format(tickets_sold,MAX_TICKETS-tickets_sold))
