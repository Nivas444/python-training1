import json
import os
DATA_FILE="data.json"
data={}

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return data
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
print(load_data())

def add_account(data):
    username = input("Enter username: ").strip()
    if username in data:
        print("Username already exists.")
        return data
    password = input("Enter password: ").strip()
    balance=input("Enter initial balance: ").strip()
    data[username] = {"username": username,
                      "password": password,
                      "balance": balance}
    save_data(data)
    print("Account added successfully.")

if __name__ == "__main__":
    data = load_data()
    print("Current data:", data)
    while True:
        choice = input("Do you want to add an account? (y/n): ").strip().lower()
        if choice == 'y':
            add_account(data)
        else:
            break