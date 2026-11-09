# Bean & Brew - Week 5, Module 1
print('Python is ready!')

# Task 1.1: Say hello
print('Welcome to Bean & Brew Coffee Co.!')
print("Today's special: Caramel Latte")
print('Stores:', 3)

# Task 1.2: Store the store's facts in variables
store_name = 'Back Bay'
open_hour = 7
latte_price = 4.95
is_open = True
manager = None
MAX_SEATS = 40
 
print(store_name, open_hour, latte_price, is_open, manager, MAX_SEATS)

# Task 1.3: Comment your code
# Author: Your Name
print('Comments are ignored by Python')   # this note is not printed

# Task 1.4: Check the data types
print(type(store_name))
print(type(open_hour))
print(type(latte_price))
print(type(is_open))
print(type(manager))
print(type('7'))

# Task 1.5: Predict, then run
cups_sold = 120
# print('Cups sold today: ' + cups_sold)   # broken: commented out
# TypeError happens here

print('Cups sold today: ' + str(cups_sold))
print(cups_sold + cups_sold)
print('120' + '120')

# Task 2.1: Predict, then run
# print(store_nme)   # broken: commented out
# NameError happens here

print(store_name)

# Task 2.2 (a): Predict, then run
# print('Back Bay opens at', open_hour
# SyntaxError

# Task 2.2 (b): Predict, then run
"""
print('Line one')
    print('Line two')
"""
# IndentationError happens here

# Fixed versions of (a) and (b)
print('Back Bay opens at', open_hour)
print('Line one')
print('Line two')

# Task 2.3: Predict, then run
# qty = int('twelve')   # broken: commented out
# ValueError happens here
qty = int('12')
print(qty + 1)

# class = 'VIP'
# SyntaxError happens here: cant use class as variable name

# 2nd_store = 'Kendall Square'
# SyntaxError happens here: invalid decimal literal

# Task 3.1 (c): valid names
customer_class = 'VIP'
store_2 = 'Kendall Square'
print(customer_class, store_2)


# Reflection Questions:
# 1.) An unclosed bracket (SyntaxError) or an unexpected indent (IndentationError) 
# means it can't understand the file, so it runs none of it. 
# A TypeError or NameError only happens when Python reaches that line, 
# so everything above it has already printed.

# 2.) The last line is what actually tells you what went wrong while the ones 
# above show where the error happened

# 3.) You can add 7 + 7 together to make 14 but you cant add '7' and 7 together as it 
# will result in an error and you have to change the '7' into an int to add it 
# numerically to 7 to make 14 or the other way around and change 7 to a string to make 77

# 4.) Error types:
        # Syntax Error: Missing ")"
        # IndentationError: Extra or missing spaces at the start of the line
        # NameError: Typo in a variable name
        # TypeError: Adding a string and a integer with typecasting
        # ValueError: text cant be converted into an integer




