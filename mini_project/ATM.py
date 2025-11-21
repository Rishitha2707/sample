# -------------------------------

# Simple ATM Application in Python

# -------------------------------
 
# Pre-defined user data (you can replace with database values)

users = {

    "nikki": {"pin": "1234", "balance": 5000},

    "admin": {"pin": "0000", "balance": 10000}

}
 
def login():

    print("\n--- LOGIN ---")

    username = input("Enter username: ").lower()

    pin = input("Enter PIN: ")
 
    if username in users and users[username]["pin"] == pin:

        print("Login successful!\n")

        return username

    else:

        print("Invalid username or PIN.\n")

        return None
 
def atm_menu(username):

    while True:

        print(f"\n--- ATM MENU ({username.upper()}) ---")

        print("1. Check Balance")

        print("2. Deposit Cash")

        print("3. Withdraw Cash")

        print("4. Exit")
 
        choice = input("Select option: ")
 
        if choice == "1":

            print(f"Your Balance: ₹{users[username]['balance']}")
 
        elif choice == "2":

            amount = int(input("Enter amount to deposit: ₹"))

            users[username]["balance"] += amount

            print(f"₹{amount} deposited successfully!")
 
        elif choice == "3":

            amount = int(input("Enter amount to withdraw: ₹"))

            if amount <= users[username]["balance"]:

                users[username]["balance"] -= amount

                print(f"₹{amount} withdrawn successfully!")

            else:

                print("Insufficient balance.")
 
        elif choice == "4":

            print("Thank you for using ATM!")

            break
 
        else:

            print("Invalid option! Try again.")
 
# Main Program

print("===== WELCOME TO PYTHON ATM =====")
 
user = login()

if user:

    atm_menu(user)

else:

    print("Exiting program...")
