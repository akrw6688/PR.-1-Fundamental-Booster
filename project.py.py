print("Welcome to the Interactive Personal Data Collector")
name = (input("Enter your Name :"))
age = int(input("Enter your age :"))
height = float(input("Enter your height in meters :"))
num = input("Enter your favourite number :")
birth_year = 2026 - age



print("Thank you! Here is the information we collected:")


print(f"Name: ",(name),("Type:",type(name),"Memory Address:",id(name)))
print(f"Age: ",(age),("Type:",type(age),"Memory Address:",id(age)))
print(f"height: ",(height),("Type:",type(height),"Memory Address:",id(height)))
print(f"Favourite Number: ",(num),("Type:",type(num),"Memory Address:",id(num)))
print("Your birth year is approximately:",birth_year)


print("Thank you for using the Personal Data Collector. Goodbye!")






          

