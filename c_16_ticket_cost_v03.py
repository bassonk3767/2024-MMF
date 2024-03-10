# Imports...
import pandas as pd

# Functions...


# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Main routine...

# Dictionaries used to hold ticket details
all_names = ["a ", "b ", "c ", "d ", "e "]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

# History of the users that bought a ticket
mini_movie_dict = {
    "Name": all_names,
    "Ticket price": all_ticket_costs,
    "Surcharge": surcharge,
}

# Plugging in the data into a data frame/sheet
mini_movie_data = pd.DataFrame(mini_movie_dict)
mini_movie_data = mini_movie_data.set_index("Name")

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_data["Total"] = mini_movie_data["Surcharge"] \
                           + mini_movie_data["Ticket price"]

# Calculate the profit for each ticket
mini_movie_data["Profit"] = mini_movie_data["Ticket price"] - 5

# Calculate total values of tickets and profits
total = mini_movie_data["Total"].sum()
profit = mini_movie_data["Profit"].sum()

# Currency formatting (uses currency)
add_dollars = ["Ticket price", "Surcharge", "Total", "Profit"]

# Adding dollar signs
for var_item in add_dollars:
    mini_movie_data[var_item] = mini_movie_data[var_item].apply(currency)

print("\n~~~~~ Ticket data ~~~~~")

# Output ticket data in a table
print(mini_movie_data)

# Output total ticket sales and profit
print("\nTotal ticket sales: ${:.2f}".format(total))
print("Total profit: ${:.2f}".format(profit))