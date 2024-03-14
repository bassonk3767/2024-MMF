# imports...
import pandas as pd
import random as rnd
from datetime import date as dte

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
mini_movie_data["Profit"] = mini_movie_data["Ticket price"] - 5

# Calculate thge ticket and profit totals
total = mini_movie_data["Total"].sum()
profit = mini_movie_data["Profit"].sum()

# Choose a winner from our name list
winner_name = rnd.choice(all_names)

# Get position of the winner's name in the list
win_index = all_names.index(winner_name)

# Look up the total amount won
total_won = mini_movie_data.at[win_index, "Total"]


# Set index at end (before printing)
mini_movie_data = mini_movie_data.set_index("Name")
print(mini_movie_data)

today = dte.today()

# Get day, month and year as separate strings
day = today.strftime("xd")
month = today.strftime("xm")
year = today.strftime("xy")

heading = "The current data is {}/{}/{}".format(day, month, year)
filename = "MMF.{}.{}.{}".format(year, month, day)

sales_status = "\n*** All the tickets have been sold ***"

winner_heading = "\n---- Raffle winner ----"
winner_text = "The winner of the raffle is {}. " \
               "They have won ${}. ie: Their ticket is " \
               "free!".format(winner_name, total_won)

# Change the frame to a string so that it can be exported to a file
mini_movie_string = pd.DataFrame.to_string(mini_movie_data)

# Create strings for printing
ticket_cost_heading = "\n---- Ticket cost / profit"
total_ticket_sales = "\nTotal ticket sales: ${}".format(total_won)
total_profit = "Total profit: ${}".format(profit)

to_write = {heading, mini_movie_string, total_ticket_sales,
            total_profit, winner_heading, winner_text}

# write output to file
# Create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")