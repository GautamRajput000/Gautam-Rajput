import json
import datetime
All_Bank_Data = {}
transfer_history ={}

def menu():
    print("=" * 40)
    print("        1. OPEN ACCOUNT")
    print("        2. DEPOSIT AMOUNT")
    print("        3. WITHDRAW AMOUNT")
    print("        4. TRANSFER AMOUNT")
    print("        5. CHECK AMOUNT")
    print("        6. CHECK ACCOUNT DETAILS")
    print("        7. STATEMENT")
    print("        8. TRANSFER AMOUNT HISTORY")
    print("        9. CHANGE PASSWORD")
    print("        10. DELETE ACCOUNT")
    print("        11. EXIT")

def save_Account_information():
    with open("Account_Information.json", "w") as file:
        json.dump(All_Bank_Data,file,indent=4)

def load_Bank_Information():
    try:
        with open("Account_Information.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_transfer_history():
    with open("Transfer_History.json", "w") as file:
        json.dump(transfer_history,file,indent=4)

def load_transfer_history():
    try:
        with open("Transfer_History.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def Add_Account():
    date = datetime.datetime.now().strftime("%d-%m-%y  %H:%M")
    name = input("Enter your name:- ").upper()
    if not name.strip():
        print("ERROR: Name cannot be empty.")
        return
    if not name.replace(" ","").isalpha():
        print("ERROR: Invalid name. Please enter a valid name using letters and spaces only.")        
        return
    
    account_no =input("Enter Account no(10 digits):- ")
    if not account_no.strip():
        print("ERROR: Account number cannot be empty.")
        return
    if not account_no.isdigit():
        print("ERROR: Account number must contain digits only.")
        return
    if len(account_no) != 10:
        print("ERROR: Account number must contain exactly 10 digits.")
        return
    if account_no in All_Bank_Data:
        print("ERROR: Account number already exists. Please use a different account number.")
        return

    city = input("Enter current city name:- ")
    if not city.strip():
        print("ERROR: City cannot be empty.")
        return
    if not city.replace(" ","").isalpha():
        print("ERROR: Invalid city name. Please enter a valid city name using letter only.")
        return
    
    pin_code = input("Enter city pin no(6 digits):- ")
    if not pin_code.strip():
        print("ERROR: Pin code cannot be empty.")
        return
    if not pin_code.isdigit():
        print("ERROR: Pin code must contain digits only.")
        return
    if len(pin_code) != 6:
        print("ERROR: Pin code must cotain exactly 6 digits.")
        return
    
    password =input("Enter password:- ")
    if not password.strip():
        print("ERROR: Password cannot be empty.")
        return
    All_Bank_Data[account_no]={
        "name":name,
        'city':city,
        'pin_code':pin_code,
        'password':password,
        'date':date,
        'amount':0,
        'Information' :[]
    }
    
    save_Account_information()
    print("ACCOUNT OPEN SUCCESSFULLY")

def deposit_amount():
    date = datetime.datetime.now().strftime("%d-%m-%y  %H:%M")
    account_no = input("Enter your current account no:- ")
    if not account_no.strip():
        print("ERROR: Account no cannot be empty.")
        return

    if account_no not in All_Bank_Data:
        print("ERROR: Invalid account number. Please enter a valid account number.")
        return
    
    amount = input("Enter your amount            :- ₹")
    if not amount.strip():
        print("ERROR: Amount cannot be empty.")
        return
    if not amount.isdigit():
        print("ERROR: Amount must contain digits only")
        return

    amount = int(amount)
    if amount <=0:
        print("ERROR: Amount must be greater than 0.")
        return

    password = input("Enter your current password  :- ")
    if not password.strip():
        print("ERROR: Password cannot be empty.")
        return
    if All_Bank_Data[account_no]['password'] != password:
        print("ERROR: Invalid password. Please enter a valid password.")
        return
    
    All_Bank_Data[account_no]['amount'] += amount 

    All_Bank_Data[account_no]['Information'].append({
        'type':'Deposit_amount',
        'amount':amount,
        'date':date
    })
    print(f"Name                          :- {All_Bank_Data[account_no]['name']}")
    print(f"Total amount                  :- ₹{All_Bank_Data[account_no]['amount']}")
    print(f"Date                          :- {date}")
    save_Account_information()
    print("AMOUNT SUCCESSFULLY DEPOSITED")

def withdrawal_amount():
    
    date = datetime.datetime.now().strftime("%d-%m-%y  %H:%M")
    account_no = input("Enter your account no:- ")
    if not account_no.strip():
        print("ERROR: Account number cannot be empty.")
        return
    if account_no not in All_Bank_Data:
        print("ERROR: Invalid account number. Please enter a valid account number.")
        return
    amount = input("Enter your amount   :- ₹")
    if not amount.strip():
        print("ERROR: Amount cannot be empty.")
        return
    if not amount.isdigit():
        print("ERROR: Amount must contain digits only.")
        return

    amount = int(amount)
    if amount<=0:
        print("ERROR: Amount must be greater than 0.")
        return

    if All_Bank_Data[account_no]['amount'] < amount:
        print("ERROR: Insufficient balance.")
        return
    password = input("Enter your password:- ")
    if not password.strip():
        print("ERROR: Password cannot be empty.")
        return
    if All_Bank_Data[account_no]['password'] != password:
        print("ERROR: Invalid password. Please try again.")
        return
    
    All_Bank_Data[account_no]['amount'] -= amount 

    All_Bank_Data[account_no]['Information'].append({
        'type':'Withdrawal_amount',
        'amount':amount,
        'date':date
    })
     
    print(f"Name              :- {All_Bank_Data[account_no]['name']}")
    print(f"Total amount      :- ₹{All_Bank_Data[account_no]['amount']}")
    print(f"Date              :- {date}")
    save_Account_information()
    print("AMOUNT SUCCESSFULLY WITHDRAWN")

def check_amount():
    account_no = input("Enter your current account no:- ")
    if not account_no.strip():
        print("ERROR: Account no cannot be empty.")
        return
    if account_no not in All_Bank_Data:
        print("ERROR: Invalid accoutn number. Please enter a valid account number.")
        return

    password = input("Enter your current password  :- ")
    if not password.strip():
        print("ERROR: Password cannot be empty.")
        return
    if All_Bank_Data[account_no]['password'] != password:
        print("ERROR: Invalid password. Please enter a valid password")
        return

    print(f"Name                         :- {All_Bank_Data[account_no]['name']}")
    print(f"Amount                       :- ₹{All_Bank_Data[account_no]['amount']}")

def amount_transfer():
    date = datetime.datetime.now().strftime("%d-%m-%y  %H:%M")
    sender_account = input("Enter from account no:- ")
    if not sender_account.strip():
        print("ERROR: From account number cannot be empty.")
        return
    if sender_account not in All_Bank_Data:
        print("ERROR: Invalid from account number. Please enter a valid from account number")
        return
    if sender_account not in transfer_history:
        transfer_history[sender_account] = []
        
    receiver_account = input("Enter to account no:- ")
    if not receiver_account.strip():
        print("ERROR: To account number cannot be empty.")
        return
    if receiver_account not in All_Bank_Data:
        print("ERROR: Invalid to account number. Please enter a valid account number.")
        return
    if sender_account == receiver_account:
        print("ERROR: From and to account numbers cannot be the same.")
        return

    amount = input("Enter your amount:- ₹")
    if not amount.strip():
        print("ERROR: Amount cannot be empty.")
        return
    if not amount.isdigit():
        print("ERROR: Amount must contain digits only.")
        return
    amount =int(amount)
    if amount <=0:
        print("ERROR: Amount must be greater than 0.")
        return
    if All_Bank_Data[sender_account]['amount'] < amount:
        print("ERROR: Insufficient balance.")
        return
    if amount >10000:
        print("ERROR: Amount cannot exceed 10,000.")
        return
    
    password = input("Enter your current password:- ")
    if not password.strip():
        print("ERROR: Password cannot be empty.")
        return
    if All_Bank_Data[sender_account]['password'] != password:
        print("ERROR: Invalid password. Please enter a valid password.")
        return
    
    All_Bank_Data[sender_account]['amount'] -= amount
    All_Bank_Data[receiver_account]['amount'] += amount
    

    All_Bank_Data[sender_account]['Information'].append({
        "type": "sender_account",
        "receiver_account": receiver_account,
        "amount": amount,
        "date": date
    })
    All_Bank_Data[receiver_account]['Information'].append({
    "type": "receiver_account",
    "sender_account": sender_account,
    "amount": amount,
    "date": date
    })
    transfer_history[sender_account].append({
    "receiver_account": receiver_account,
    "amount": amount,
    "date": date
    })
    save_Account_information()
    save_transfer_history()
    print("AMOUNT TRANSFERRED SUCCESSFULLY")
        
def amount_transfer_history():
    sender_account = input("sender account number:- ")
    if not sender_account.strip():
        print("ERROR: Sender account number cannot be empty.")
        return
    if sender_account not in transfer_history:
        print("ERROR: Invalid sender account number. Please enter a valid sender account number.")
        return

    for data in transfer_history[sender_account]:
        print(f"Receiver account number     :- {data['receiver_account']}")
        print(f"Amount                      :- ₹{data['amount']}")
        print(f"Date                        :- {data['date']}")

def statment():
    account_no = input("Ener current account no:- ")
    if not account_no.strip():
        print("ERROR: Account number cannot be empty.")
        return
    if account_no not in All_Bank_Data:
        print("ERROR: Invalid account number. Please enter a valide account number.")
        return
    password = input("Enter current password:- ")
    if not password.strip():
        print("ERROR: Password cannot be empty.")
        return
    if All_Bank_Data[account_no]['password'] != password:
        print("ERROR: Invalide password. Please enter a valid password.")
        return
    

    print(f"{'Deposit':<15}{'Withdrawal':<22}{'Date':<25}{'Amount':<16}{'Total Amount'}")
    Information= All_Bank_Data[account_no]['Information']
    if not Information:
        print(f"{'-':<15}{'-':22}{'-':<22}{'-':<25}{'₹0':<16}{'₹0'}")
        return
    else:
        balance = 0
        for data in Information:
            
            if data["type"]=="Deposit_amount":
                balance += data['amount']
                print(f"{'Deposit':<20}{'-':<17}{data['date']:<25}₹{data['amount']:<15}₹{balance}")
            
            elif data["type"]=="Withdrawal_amount":
                balance -= data['amount']
                print(f"{'-':<15}{'Withdrawal':<22}{data['date']:<25}₹{data['amount']:<15}₹{balance}")
                
            elif data["type"]== "receiver_account":
                balance += data['amount']
                print(f"{'Deposit':<20}{'-':<22}{data['date']:<25}₹{data['amount']:<15}₹{balance}")
                
            elif data["type"]== "sender_account":
                balance -= data['amount']
                print(f"{'-':<15}{'Withdrawal':<22}{data['date']:<25}₹{data['amount']:<15}₹{balance}")
                    
def change_password():
    account_no = input("Enter your current account no:- ")
    if not account_no.strip():
        print("ERROR: Current account no cannot be empty.")
        return
    if account_no not in All_Bank_Data:
        print("ERROR: Invalide account no.")
        return
    
    new_password = input("Enter new password:- ")
    if not new_password.strip():
        print("ERROR: New password cannot be empty.")
        return
    conform_password = input("Enter conform password:- ")
    if not conform_password.strip():
        print("ERROR: Canform password cannot be empty.")
        return
    if new_password != conform_password:
        print("ERROR:  New passwords and Conform password do not match.") 
        return
    All_Bank_Data[account_no]['password'] = new_password
    save_Account_information()
    print("Password changed successfully")

def delete_account():
    account_no = input("Enter yout current account no:- ")
    if not account_no.strip():
        print("ERROR: Account number cannot be empty.")
        return
    if account_no not in All_Bank_Data:
        print("ERROR: Invalide Account number. Please enter a valide account number.")
        return
    
    password = input("Emter your passowrd:- ")
    if not password.strip():
        print("ERROR: Password cannot be empty.")
        return
    if All_Bank_Data[account_no]['password'] != password:
        print("ERROR: Invalide password. Please enter a valide password.")
        return
    del All_Bank_Data[account_no]
    
    save_Account_information()
    print("Account delete successfully.")

def account_detail():
    account_no = input("Enter your account no:- ")
    if not account_no.strip():
        print("ERROR: Account number cannot be empty.")
        return
    if account_no not in All_Bank_Data:
        print("ERROR: Invalid account number.")
        return
    
    password = input("Enter your password  :- ")
    if not password.strip():
        print("ERROR: password cannot be empty.")
        return
    if All_Bank_Data[account_no]['password'] != password:
        print("ERROR: Invalid password. Please enter a valide password.")
        return
    if account_no in All_Bank_Data:
        # for data in All_Bank_Data:
        print(f"Name                 :- {All_Bank_Data[account_no]['name']}")
        print(f"Amount               :- {All_Bank_Data[account_no]['amount']}")
        print(f"City                 :- {All_Bank_Data[account_no]['city']}")
        print(f"Pin code             :- {All_Bank_Data[account_no]['pin_code']}")
        print(f"Account opening Date :- {All_Bank_Data[account_no]['date']}")
        return
All_Bank_Data = load_Bank_Information()
transfer_history= load_transfer_history()
while True:
    menu()
    Chaoise = input('Enter your choice(1-11):- ') 
    if Chaoise == '1':
        Add_Account()
    elif Chaoise == '2':
        deposit_amount()
    elif Chaoise == '3':
        withdrawal_amount()
    elif Chaoise == '4':
        amount_transfer()
    elif Chaoise == '5':
        check_amount()
    elif Chaoise == '6':
        account_detail()
    elif Chaoise == '7':
        statment()
    elif Chaoise == '8':
        amount_transfer_history()
    elif Chaoise == '9':
        change_password()
    elif Chaoise == '10':
        delete_account()
    elif Chaoise == '11':
        print("Thank you for using the Bank Management System.")
        break

