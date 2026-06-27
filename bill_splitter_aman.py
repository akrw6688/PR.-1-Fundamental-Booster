print("Welcome to the Bill Splitter App")
print("                                ")
bill_amount = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people to split the bill: "))
if num_people <= 0:
    print("Number of people should be more than 0")
else:
    pass
tip = int(input("Enter the tip percentage: (0/5/10/15/20) "))
print("                                ")
tip_amount = (tip / 100) * bill_amount
print("Tip amount: $", tip_amount)
total_bill = bill_amount + tip_amount
print("Total bill amount including tip: $", total_bill)
per_person = total_bill / num_people
print("Each person should pay: $", per_person)

while True:
    choice = input("would you like to calculate another bill? (yes/no)? ")
    if choice == "yes":
        bill_amount = float(input("Enter the total bill amount: "))
        num_people = int(input("Enter the number of people to split the bill: "))
        if num_people <= 0:
            print("Number of people should be more than 0")
        else:
            pass        
        tip = int(input("Enter the tip percentage: (0/5/10/15/20) "))
        print("                                ")
        tip_amount = (tip / 100) * bill_amount
        print("Tip amount: $", tip_amount)
        total_bill = bill_amount + tip_amount
        print("Total bill amount including tip: $", total_bill)
        per_person = total_bill / num_people
        print("Each person should pay: $", per_person)
    else:
        print("Thank you for visiting")
        break
        

