while True:
    print("Welcome to Patern Generator and number analyzer")
    print("Select an option:")
    print("1. Right-angled Triangle")
    print("2. Pyramid")
    print("3. Left-angled Triangle")
    print("4. Ananlyze a range of number")
    choice = int(input("Enter your choice:"))
    if choice <= 0:
        print("invalid choice")
        continue
    elif choice == 1:
        print("You choose 1")
        rows = int(input("Enter number of rows:"))
        if rows <= 0:
            print("invalid rows")
            continue
        for i in range(1, rows +1):
            for j in range(1, i+1):
                print("*", end=" ")
            print()
    elif choice == 2:
        print("You choose 2")
        rows = int(input("Enter number of rows:"))
        if rows <= 0:
            print("invalid rows")
            continue  
        for i in range(rows):
            for space in range(rows - i - 1):
                print(" ", end=" ")
            for j in range(2 * i + 1):
                print("*", end=" ")
            print()
    elif choice == 3:
        print("You choose 3")
        rows = int(input("Enter number of rows:"))
        if rows <= 0:
            print("invalid rows")
            continue
        for i in range(1, rows + 1):
            for space in range(rows - i + 1):
                print(" ", end=" ")
            for j in range(i):
                print("*", end=" ")
            print()
    
    elif choice == 4:
        print("You choose 4")
        start = int(input("Enter your starting number:"))
        end = int(input("Enter your ending number:"))
        if end < start:
            print("Starting number should be greater")
            continue
        total = 0
        for i in range(start, end + 1):
            if i == 0:
                pass
            elif i % 2 == 0:
                print(f"number {i} is even")
            else:
                print(f"number {i} is odd")
            total += i
        print(f"sum of  numbers from {start} and {end} is: {total}")
    elif choice == 5:
        print("Thank You")
        break
    else:
        print("invalid choice")    
    

        



    
    
    


















    break


