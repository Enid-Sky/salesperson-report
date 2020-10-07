
"""Generate sales report showing total melons each salesperson sold."""

# initiate salespeople empty list
salespeople = []
# initiate variable list for total melon's sold
melons_sold = []

# open sales report file
f = open('sales-report.txt')

# loop over each line in the file(object)
for line in f:
    # remove trailing whitespace
    line = line.rstrip()
    # split the string into a data list
    entries = line.split('|')

    # get the name of the salesperson and how many melons they sold(integer)
    salesperson = entries[0]
    melons = int(entries[2])

    # if the salesperson is already in salespeople
    # increment the amount of melons sold

    if salesperson in salespeople:
        # find the position that salesperson is stored in salespeople
        position = salespeople.index(salesperson)
        # use the position to find the melons sold and incement by one
        melons_sold[position] += melons
    else:  # otherwise, salesperson is not on salespeople list
        salespeople.append(salesperson)  # append the salesperson to the list
        melons_sold.append(melons)  # append melons to total melons sold

# loop over the entire salespeople list and print each salesperson and the total melons the sold.
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
