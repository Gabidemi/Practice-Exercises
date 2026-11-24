import numpy as np


sales = np.array([
    [
        [1200, 1500, 1800],
        [2000, 2200, 2500]
    ],

    [
        [1400, 1600, 1900],
        [2100, 2300, 2600]
    ]
])

print("Displaying the entire sales array")
# Displays the entire Sales array
print(sales)
print()

print("For Loop using np.nditer")
# For loop using np.nditer
for sale in np.nditer(sales):
    print(sale)

print()
print("Nested For Loops")
# Nested For Loops
for layer in sales:
    for row in layer:
        for col in row:
            print(col)

print()
print("Total Sales: ")
# Calculating total sales
total_sales = 0
for sale in np.nditer(sales):
    total_sales = total_sales + sale
print(f"The total amount is: ${total_sales:,.2f}")
print()

print("Average Sales: ")
# Calculating Average sales
avg_sales = 0
total_sales = 0
for sale in np.nditer(sales):
    total_sales = total_sales + sale

avg_sales = total_sales/sales.size
print(f"The Average sale is about: ${avg_sales: ,.2f}")
print()


# Calculating Highest Sale
Highest_Sale = 0
for sale in np.nditer(sales):
    if sale > Highest_Sale:
        Highest_Sale = sale

print(f"The Highest Sale is: ${Highest_Sale: ,.2f}")






