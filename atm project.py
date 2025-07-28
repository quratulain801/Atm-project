
Accounts = {
    "123456": {"pin": "1111", "balance": 5000},
    "1334776": {"pin": "2222", "balance": 3000}
}

MAX_ATTEMPTS = 3
MAX_TRANSFERS_PER_DAY = 3
transfer_count = {}

def login(accounts):
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        acc_no = input("Enter your account number: ")
        pin = input("Enter PIN: ")
        if acc_no in accounts and accounts[acc_no]["pin"] == pin:
            print("\n✅ Login successful.")
            return acc_no
        else:
            print("❌ Invalid account number or PIN.")
            attempts += 1
    print("\n🚫 Too many incorrect attempts. Access denied.")
    return None

def check_balance(accounts, acc_no):
    print(f"\nYour current balance is: Rs {accounts[acc_no]['balance']}")

def deposit(accounts, acc_no):
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        accounts[acc_no]['balance'] += amount
        print(f"\n✅ Rs {amount} deposited successfully.")
    else:
        print("❌ Invalid amount.")

def withdraw(accounts, acc_no):
    amount = float(input("Enter amount to withdraw: "))
    if 0 < amount <= accounts[acc_no]['balance']:
        accounts[acc_no]['balance'] -= amount
        print(f"\n✅ Rs {amount} withdrawn successfully.")
    else:
        print("❌ Insufficient funds or invalid amount.")

def transfer(accounts, sender, receiver):
    if sender not in transfer_count:
        transfer_count[sender] = 0
    if transfer_count[sender] >= MAX_TRANSFERS_PER_DAY:
        print("\n🚫 Daily transfer limit reached.")
        return

    if receiver not in accounts:
        print("❌ Receiver account not found.")
        return

    pin_attempts = 0
    while pin_attempts < MAX_ATTEMPTS:
        pin = input("Enter your PIN for transfer: ")
        if pin == accounts[sender]['pin']:
            amount = float(input("Enter amount (between $10 to $2000): "))
            if 10 <= amount <= 2000 and accounts[sender]['balance'] >= amount:
                accounts[sender]['balance'] -= amount
                accounts[receiver]['balance'] += amount
                transfer_count[sender] += 1
                print("\n✅ Transfer successful.")
            else:
                print("❌ Invalid amount or insufficient balance.")
            return
        else:
            pin_attempts += 1
            print("❌ Incorrect PIN.")

    print("\n🚫 Transfer cancelled after 3 incorrect PIN attempts.")

def change_pin(acc_no):
    current_pin = input("Enter your current PIN: ")
    if current_pin == Accounts[acc_no]["pin"]:
        while True:
            new_pin = input("Enter your new 4-digit PIN: ")
            if new_pin.isdigit() and len(new_pin) == 4 and new_pin != current_pin:
                confirm_pin = input("Re-enter your new PIN: ")
                if confirm_pin == new_pin:
                    Accounts[acc_no]["pin"] = new_pin
                    print("\n✅ PIN changed successfully.")
                    break
                else:
                    print("❌ Confirmation does not match.")
            else:
                print("❌ Invalid PIN.")
    else:
        print("❌ Incorrect current PIN.")

def exit_atm():
    print("\nThank you for using our ATM. Goodbye!")
    exit()

def main_menu(accounts):
    acc_no = login(accounts)
    if not acc_no:
        return

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Change PIN")
        print("6. Exit")
        choice = input("Enter your choice between 1-6: ")

        if choice == "1":
            check_balance(accounts, acc_no)
        elif choice == "2":
            deposit(accounts, acc_no)
        elif choice == "3":
            withdraw(accounts, acc_no)
        elif choice == "4":
            receiver = input("Enter receiver account number: ")
            transfer(accounts, acc_no, receiver)
        elif choice == "5":
            change_pin(acc_no)
        elif choice == "6":
            exit_atm()
        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
main_menu(Accounts)
