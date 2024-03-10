# Imports...

import pandas as pd
import random as rnd

# Functions...


# Main routine...

# Lists that hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket price": all_ticket_costs,
    "Surcharge": surcharge
}

mini_movie_data = pd.DataFrame(mini_movie_dict)
# mini_movie_data = mini_movie_data.set_index("Name")

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_data["Total"] = mini_movie_data["Surcharge"] \
                           + mini_movie_data["Ticket price"]

# Calculate the profit made for each ticket sold
mini_movie_data["Profit"] = mini_movie_["Ticket price"] - 5

# Choose a winner from our name list
winner_name = rnd.choice(all_names)

# Get position of the winner's name in the list
win_index = all_names.index(winner_name)

# Look up the total amount lost