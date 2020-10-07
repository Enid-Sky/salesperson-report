# create a function to find the total of melons sold
# create another function to print out the sales report

def melon_sales_report(file_path):

    # create an empty dictionary for total melons sold by salesperson
    melon_sales = {}

    # open the file and loop through
    with open(file_path) as f:
        for line in f:
            line = line.rstrip()

    # unpackage lines and split
    sales_person, _, quantity_sold = line.split('|')

    # loop through melon_sales data
    # determine if salesperson is in dictionary, set or incemement quantity_sold
    if sales_person in melon_sales:
        melon_sales[sales_person] += int(quantity_sold)
    else:
        melon_sales[sales_person] = int(quantity_sold)

    return melon_sales


def print_sales_report(melon_sales_report):
    for sales_person, melons_sold in melons_sales_report:

        print(f'{sales_person} sold a total of {melon_sales}')


print_sales_report(melon_sales_report('sales-report.txt'))
