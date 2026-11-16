# TODO 1: Add a header comment
# Name: Gbolahan Abidemi
# Date: 11/16/2026
# Description: Income Tax Calculator

# TODO 2: Define the constants
# TAX_RATE = 20%
# STANDARD_DEDUCTION = $10,000
# DEPENDENT_DEDUCTION = $2,000 for each
Tax_Rate = 0.20
Standard_Deduction = 10000
Dependent_Deduction = 2000

# TODO 3: Display the program title and a divider line
print("-" * 20)
print("INCOME TAX CALCULATOR")
print("-" * 20)
# TODO 4: Prompt for gross annual income and convert it to a float
Annual_Income = float(input("How much do you make in a Year?: "))
# TODO 5: Prompt for the number of dependents and convert it to an int
Dependents = int(input("Input the number of Dependents in your household: "))
# TODO 6: Calculate the dependent deductions and the total deductions
Total_Dependent_Deduction = Dependents * Dependent_Deduction
Total_Deduction = Standard_Deduction + (Dependents * Dependent_Deduction)
# TODO 7: Calculate the taxable income
Taxable_Income = float(Annual_Income - Total_Deduction)
# TODO 8: Calculate the estimated income tax
Income_Tax = Taxable_Income * Tax_Rate
# TODO 9: Display the income tax summary
print("-" * 20)
print("INCOME TAX SUMMARY")
print("-" * 20)
print(f"Gross Income: ${Annual_Income: ,.2f}\n\
Standard Deduction: ${Standard_Deduction: ,.2f}\n\
Dependent Deduction: ${Total_Dependent_Deduction: ,.2f}\n\
Total Deduction: ${Total_Deduction: ,.2f}\n\
Taxable Income: ${Taxable_Income: ,.2f}\n\
Tax Rate: {Tax_Rate: .2%}\n\
Estimated Income Tax: ${Income_Tax: ,.2f}")
# Show: gross income, standard deduction, dependent deductions,
# total deductions, taxable income, tax rate, and estimated income tax.
# Use f-strings and format monetary values with .2f

# REFLECTION QUESTIONS:
# 1: It needs to be converted because if it deals with money, there are bound to be decimals
# 2: Its converted into an Int because you can only have a whole number of dependents
# 3: The .2f format is so that the output does not display too much decimals and limit it to 2
# 4: I used multiplication to find the total Dependat deductions, addition to add to find the 
    # Total deductions and subtraction to calculate the income vs the deductions
# 5: Probably adding some error handling code