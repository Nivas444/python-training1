import json
import os
DATA_FILE="data1.json"

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data,f,indent=4)
    print("Data saved successfully.")

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Error: JSON file is corrupted. Starting with empty data.")
                return {}
    else:
        return {}
    
def create_account(data):
    name=input("Enter your name: ").strip()
    if name in data:
        print("Account already exists.")
        return data
    password=input("Enter your password: ").strip()
    balance=int(input("Enter initial balance: "))
    data[name]={"account_holder":name,"password":password,"balance":balance}
    print("Account created successfully.")
    
def display_data():
    data=load_data()
    if not data:
        print("No accounts found.")
        return
    for account in data.values():
        print(f"Account Holder: {account['account_holder']}, Password: {account['password']}, Balance: {account['balance']}")

def update_account(data):
    name=input("Enter your name: ").strip()
    if name not in data:
        print("Account not found.")
        return data
    password=input("Enter your password: ").strip()
    if data[name]['password'] != password:
        print("Incorrect password.")
        return data
    new_password=input("Enter new password (leave blank to keep current): ").strip()
    if new_password:
        data[name]['password']=new_password
    try:
        new_balance=int(input("Enter new balance (leave blank to keep current): ").strip() or data[name]['balance'])
        data[name]['balance']=new_balance
    except ValueError:
        print("Invalid balance input. Balance not updated.")
    print("Account updated successfully.")

def delete_account(data):
    name=input("Enter your name: ").strip()
    if name not in data:
        print("Account not found.")
        return data
    password=input("Enter your password: ").strip()
    if data[name]['password'] != password:
        print("Incorrect password.")
        return data
    del data[name]
    print("Account deleted successfully.")

def main():
    data=load_data()
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Display Accounts")
        print("3. Update Account")
        print("4. Delete Account")
        print("5. Exit")
        choice=input("Enter your choice: ").strip()
        if choice=='1':
            create_account(data)
            save_data(data)
        elif choice=='2':
            display_data()
        elif choice=='3':
            update_account(data)
            save_data(data)
        elif choice=='4':
            delete_account(data)
            save_data(data)
        elif choice=='5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()