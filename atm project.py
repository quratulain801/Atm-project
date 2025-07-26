import sys
# dictionary
Accounts = { 
    "123434":{"name": "Alice", "pin": "1111", "balance": 1200.0},
    "1334776":{"name": "Bob", "pin": "2222", "balance": 850.5},
    "657598":{"name": "Charlie", "pin": "3333", "balance": 430.75}
}

#Login function
def login(Accounts):
       ac_no=input("enter account number")
       if ac_no in Accounts:
              pin=input("enter your pin")
              if pin==Accounts[ac_no]["pin"]:
                     print(f"Welcome, {Accounts[ac_no]['name']}!")
                     return ac_no  
              else:
               print("Incorrect PIN.")
       else:
        print("Account not found.")
        return None
              
# check  balance funtion
def check_balance(Accounts,ac_no):
       print(f"Your balance is: ${Accounts[ac_no]['balance']:.2f}")

#Deposit function
def deposit(Accounts, acc_no):
    withdraw_limit_perday=1000
    try:
        deposit_amount = float(input("Enter deposit amount (between $10 to $5000): "))
    except ValueError:
        print("❌ Invalid input. Please enter a numeric value.")
        return
    if 10 <= deposit_amount <= 5000:
        Accounts[acc_no]["balance"] += deposit_amount
        print(f"✅ Deposit successful! Your new balance is: ${Accounts[acc_no]['balance']:.2f}")
    else:
        print("❌ Amount must be between $10 and $5000.")

#widhdraw function
for account in Accounts.values():
    account['withdrawn_today'] = 0.0 
def withdraw(Accounts,acc_no):
    DAILY_LIMIT = 1000.0
    try:
        withdraw_amount = float(input("Enter Withdraw amount (between $20 to $500): "))
    except ValueError:
        print("❌ Invalid input. Please enter a numeric value.")
        return
    if 20 <= withdraw_amount <= 500:
         if withdraw_amount % 20 != 0:
            print("❌ Amount must be a multiple of $20. (ATM dispenses $20 bills only)")
            return
         if withdraw_amount<=Accounts[acc_no]['balance']:
              Accounts[acc_no]['balance']-=withdraw_amount
              Accounts[acc_no]['withdrawn_today'] += withdraw_amount
              print(f"✅ Withdraw successful! Your new balance is: ${Accounts[acc_no]['balance']:.2f}")
         else:
            print("❌ Insufficient balance.")
    else:
        print("❌ Amount must be between $20 and $500.")
    
#transfer function
def transfer(Accounts, sender, receiver):
    pin = input("🔐 Enter your PIN to confirm: ")
    if Accounts.get(sender) and Accounts[sender]["pin"] == pin:
        if sender == receiver:
            print("❌ You cannot transfer money to the same account.")
            return
        if Accounts.get(receiver):
            try:
                amount = float(input("Enter amount (between $10 to $2000): "))
            except ValueError:
                print("❌ Invalid amount. Please enter a numeric value.")
                return            
            if 10 <= amount <= 2000:
                if Accounts[sender]["balance"] >= amount:
                    Accounts[sender]["balance"] -= amount
                    Accounts[receiver]["balance"] += amount
                    print("✅ Transfer successful!")
                    print(f"💰 ${amount:.2f} transferred to {Accounts[receiver]['name']}.")
                    print(f"Your new balance is: Rs {Accounts[sender]['balance']:.2f}")
                else:
                    print("❌ Insufficient balance.")
            else:
                print("❌ Amount must be between $10 and $2000.")
        else:
            print("❌ Receiver account not found.")
    else:
        print("❌ Invalid sender account or incorrect PIN.")

#change pin function
def change_pin(ac_no):
    current_pin = input("Enter your current PIN: ")
    
    if current_pin == Accounts[ac_no]["pin"]:
        while True:
            new_pin = input("Enter your new 4-digit PIN: ")
            if new_pin.isdigit() and len(new_pin) == 4 and new_pin != current_pin:
                confirmation_pin = input("Re-enter your new PIN for confirmation: ")
                if confirmation_pin == new_pin:
                    Accounts[ac_no]["pin"] = new_pin
                    print("✅ PIN changed successfully.")
                    break
                else:
                    print("❌ Confirmation does not match. Try again.")
            else:
                print("❌ Invalid PIN. Must be 4 digits and different from current.")
    else:
        print("❌ Incorrect current PIN.")
                       
# exit menu
def exit_atm():
    print("👋 Exiting ATM. Thank you!")
    sys.exit()
                              
#display menu
def main_menu(Accouonts):
    acc_no = login(Accounts)
    if not acc_no:
        return
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Transfer money")
        print("5. change pin")
        print("6. Exit")
        choice=input("enter your choice betweem 1-6")
        if choice == "1":
            check_balance(Accounts, acc_no)
        elif choice == "2":
            deposit(Accounts, acc_no)
        elif choice == "3":
            withdraw(Accounts, acc_no)
        elif choice == "4":
            receiver = input("Enter receiver account number: ")
            transfer(Accounts, acc_no, receiver)
        elif choice == "5":
            change_pin(acc_no)
        elif choice == "6":
            exit_atm()
# -------- Start Program -------- #                                                          
main_menu(Accounts)





4