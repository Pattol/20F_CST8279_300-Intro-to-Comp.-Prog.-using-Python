import csv


while True:

    print(""" 
    welcome to Popular Names 
    1- Boys Names
    2- Girls Names
    3- Exit 
    """)

    choice = input("Please make a choice:")

    if choice =="1":
        with open('2000_boysNames.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    elif choice =="2":
        with open('2000_GirlsNames.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    elif choice =="3":
        exit()
        break
    else:
        print("Invalid option")