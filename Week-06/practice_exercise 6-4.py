employees = ['John', 'Sarah', 'Michael', 'Jennifer', 'David']
sales = [5200, 6800, 4500, 7200, 5800]

def calculate_total(sales):
    total_sales = 0
    for sale in sales:
        print(sale)
        total_sales = total_sales + sale
    return total_sales

total = calculate_total(sales)
print(f"The total amount of sales amount to: ${total: ,.2f}")

def calculate_average(total, number_of_employees):
    avg_employee = total / len(employees)
    return avg_employee

average = calculate_average(total,5)
print(f"The average sales of the employees is: ${average: ,.2f}")