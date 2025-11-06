print("Welcome to the Tip calcultor")


bill=int(input("Enter the bill you get after dinner"))
tip=int(input("Enter the percentage of total bill tip you would like to provide"))
people=int(input("Enter the number of people you are"))


tip_amt=bill*(tip/100)
total_bill=bill+tip_amt
print("So the total bill came out to be: ", round(total_bill,2))
individual_paid=total_bill/people
print("Bill paid will be:", round(individual_paid,2))