# Imports...
import pandas as pd

# Functions...

# Main routine...

# Dictionaries used to hold ticket details
all_names = ["a ", "b ", "c ", "d ", "e "]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

# History of the users that bought a ticket
mini_movie_dict = {
    "Name(s): ": all_names,
    "Ticket price: ": all_ticket_costs,
    "Surcharge ": surcharge
}

# Plugging in the data into a data frame/sheet
mini_movie_data = pd.DataFrame(mini_movie_dict)

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_data["Total"] = mini_movie_data["Surcharge"] \
                           + mini_movie_data["Ticket price"]

print(mini_movie_data)