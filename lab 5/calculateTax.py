#design a program that will calculate the sales tax in North Carolina for an item with a price of $75.34.
# Your program should accruately calculate the saLes tax and print the item price, sales tax and total cost
# of the item neatly to the console.
# Hint: Assume N.C sales tax is 7.25%

#Constants and variables
item_price = 75.34

sales_tax_rate = 0.0725

#Calculations

sales_tax = item_price * sales_tax_rate

total_cost = item_price + sales_tax

#results is formatted to 2 decimal places

print(f'Item Price: ${item_price:.2f}')

print(f'Sales Tax: ${sales_tax:.2f}')

print(f'Total Cost: ${total_cost:.2f}')
