import json 
import os

print("Customer Management System")

if os.path.exists("customers.json"):
    with open("customers.json", "r" , encoding= "utf-8") as file:
        customers = json.load(file)
else:
    customers = []

while True:
    print("1. Add customer")
    print("2. Show customers")
    print("3. Exit")
    print("4. Search customer")
    print("5. Show customer details")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter customer name: ").strip().capitalize ()

        if name == "":
            print("Customer name cannot be empty!")
        
        elif name in customers:
            print("Customer already exist!")

        else:
            customers.append(name)

            with open("customers.json", "w", encoding="utf-8") as file:
                json.dump(customers, file, ensure_ascii=False, indent=4)

            print("Customer added!")

    elif choice == "2":
        print("Customers:")
        for number, customer in enumerate(customers, start = 1):
            print(f"{number}. {customer}")

    elif choice == "5":
        customer_number = input("Enter customer number: ")
        if customer_number.isdigit():
            index = int(customer_number) - 1
            if 0 <= index < len(customers):
                print(f"Customer: {customers[index]}")

    elif choice == "3":
        print("Goodbye!")
        break


    elif choice == "4":
        search_name = input("Enter customer name to search: ").strip().lower()

        found_customer = None

        for customer in customers:
            if customer.lower() == search_name:
                found_customer = customer
                break

        if found_customer is not None:
            print("Customer found:", found_customer)
        else:
            print("Customer not found!")

    else:
        print("Invalid option")