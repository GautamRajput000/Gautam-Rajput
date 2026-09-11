import json
All_Student = {}

def menu():
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    # print("2. View Students")
    print("2. Search Student")
    # print("4. Update Student")
    print("3. Delete Student")
    print("4. STUDENT MARKS CALCULATOR")
    print("5. UPDATE STUDENT INFORMATION")
    print("6. Exit")

def get_unique_id():
    while True:
        unique_id = input("Enter your unique id:- ")  
        if not unique_id.strip():
            print("ERROR: Unoque id number connecct be empty.")
            continue
        if unique_id not in All_Student:
            print("Error: Invalid unique id number. Please enter a valid unique id number.") 
            continue
        
        return unique_id
 
def save_student_data():
    with open("students.json","w") as file:
        json.dump(All_Student,file,indent=4)

def load_student():
    global All_Student
    try:
        with open("students.json","r") as file:
            All_Student=json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def Add_students():
    print("="*40)
    unique_id = input("Create your unique id number:- ")
    if not unique_id.strip():
        print("ERROR: Unique id connect be empty.")
        return
    if unique_id in All_Student:
        print("ERROR: This unique ID already exists.")
        return

    
    name = input("Enter student name:- ")
    if not name.strip():
        print("ERROR: Name connect be empty.")
        return
    if not name.replace(" ","").isalpha():
        print("ERROR: Invalid name. Please enter a valid name using letters and spaces only.")
        return
    
    clas = input("Enter your class/branch:- ")
    if not clas.strip():
        print("ERROR: Class connect be empty.")
        return
    
    roll = input("Enter roll number:- ")
    if not roll.strip():
        print("ERROR: Roll number connect be empty.")
        return
    if not roll.isdigit():
        print("ERROR: Roll number connect be empty.")
        return

    age = input("Enter student age:- ")
    if not age.strip():
        print("ERROR: Age connect be empty.")
        return
    if not age.isdigit():
        print("ERROR: Invalid age. Please enter a valid age using degits only.")
        return
    if int(age) == 0 :
        print("ERROR: Age cannot be 0.")
        return

    marks = input("Enter student marks:- ")
    if not marks.strip():
        print("ERROR: Marks connect be enpty.")
        return
    if not marks.isdigit():
        print("ERROR: Invalid Marks. Please enter a valid Marks using digits only.")
        return
    
    phone = input("Enter your Mobile number:- ")
    if not phone.strip():
        print("ERROR: Mobile number connect be empty.")
        return
    if not phone.isdigit():
        print("ERROR: Invalid Mobile number. Pleease enter a valid Mobile number using degits only.")
        return
    if len(phone) !=10:
        print("ERROR: Mobile number must contain exactly 10 digits.")
        return

    email = input("Enter your email id:- ")
    if not email.strip():
        print("ERROR: Email id connect be empty.")    
        return
    if '@' not in email or '.' not in email :
        print("ERROR: Invalid email id. Please enter a valid email id.")
        return

    city = input("Enter your city:- ")
    if not city.strip():
        print("ERROR: City connect be empty.")
        return
    if not city.replace(" ","").isalpha():
        print("ERROR: Invalid city. Please enter a valid city name using letters and spaces only.")
        return

    
    All_Student[unique_id] = {
        'name':name,
        'roll':roll,
        'age':age,
        'phone':phone,
        'email':email,
        'city':city,
        'marks':marks,
        'clas':clas
    }
    save_student_data()
    print("="*40)
    print(f"{name} Successfully added")
    print("="*40)

def search_student():
    print("="*40)
    uniqe_id = get_unique_id()

    name = input("Enter student name:- ")
    if not name.strip():
        print("ERROR: Name connect be empty.")
        return
    if All_Student[uniqe_id]['name'] != name:
        print("ERROR: Invalid student name. Please enter a valid name.")
        return
    
    roll = input("Enter student roll number:- ")
    if not roll.strip():
        print("ERROR: Roll number connect be empty.")
        return
    if All_Student[uniqe_id]['roll'] != roll:
        print("ERROR: Invalid roll number. Please enter a valid roll number.") 
        return

    if uniqe_id in All_Student:
       
        print("-"* 40)
        print(f"Name                     :- {All_Student[uniqe_id]['name']}")
        print(f"Roll number              :- {All_Student[uniqe_id]['roll']}")
        print(f"Class/Branch             :- {All_Student[uniqe_id]['clas']}")
        print(f"Age                      :- {All_Student[uniqe_id]['age']}")
        print(f"Marks                    :- {All_Student[uniqe_id]['marks']}")
        print(f"Phone number             :- {All_Student[uniqe_id]['phone']}")
        print(f"Email id                 :- {All_Student[uniqe_id]['email']}")
        print(f"City                     :- {All_Student[uniqe_id]['city']}")
        print("="*40)

def delete_student():
    print("="*40)
    unick_id = get_unique_id()

    del All_Student[unick_id]
    save_student_data()
    print("="*40)
    print("STUDENT DELETE SUCCESSFULLY")
    print("="*40)

def Total_marks_percentage():
    def marks_percentage():
        print("="*40)
        marks = input("Enter marks:- ")
        if not marks.strip():
            print("ERROR: Marks connect be empty.")
            return
        if not marks.isdigit():
            print("ERROR: Marks must contain digits only")
            return
        
        total_marks = input("Enter total marks:- ")
        if not total_marks.strip():
            print("ERROR: Total marks connect be empty.")
            return
        if not total_marks.isdigit():
            print("ERROR: Marks must contain digits only.")
            return
        if int(total_marks) == 0:
            print("ERROR: Total marks cannot be 0.")
            return
        percentage = int(marks)/int(total_marks)*100
        print("="*40)
        print(f"percentage:- {percentage}%")
        print("="*40)

    def Total_percentage_marks():
        print("="*40)
        percentage = input("Enter your percentage:- ")
        if not percentage.strip():
            print("ERROR: Percentage connect be empty.")
            return
        if not percentage.isdigit():
            print("ERROR: percentage must contain digits only.")
            return
        total_markse = input("Enter your total marksL:- ")
        if not total_markse.strip():
            print("ERROR: Total marks connect be empty.")
            return
        if not total_markse.isdigit():
            print("ERROR: Total marks must contain digits only")
            return
        if int(total_markse) == 0:
            print("ERROR: Total marks cannot be 0.")
            return
        markse = int(percentage)/100*int(total_markse)
        print("="*40)
        print(f"Marks:- {markse}")
        print("="*40)
    while True:
        print("="*40)
        print("1. marks to percentage")
        print("2. percentage to marks")
        print("3. exit")
        print("="*40)
        Choice = input("Enter your choice(1-3):- ")
        if Choice == '1':
            marks_percentage()
        elif Choice == '2':
            Total_percentage_marks()
        elif Choice == '3':
            break

def update_student_details():
    def  menu():
        print("="*40)
        print("1. Name")                    
        print("2. Roll number")                    
        print("3. age")                    
        print("4. Mobile number")                    
        print("5. Gmail")                    
        print("6. City")                    
        print("7. Marks")                    
        print("8. Class/Branch")    
        print("9. Exit")    

    def name():
        print("="*40)

        unique_id = get_unique_id()
        new_name = input("Enter your new name:- ")
        if not new_name.strip():
            print("ERROR: Name connect be empty.")
            return
        if not new_name.replace(" ","").isalpha():
            print("ERROR: Invalid new name. Please enter a valid name using letters and spaces only")
            return
        confrom_name = input("Enter confrom name:- ")
        if not confrom_name.strip():
            print("Confrom name connect be empty.")
            return
        if not confrom_name.replace(" ","").isalpha():
            print("ERROR: Invalid confrom name. Please enter a valid confrom name using letters and spaces only")
            return

        if confrom_name != new_name:
            print("ERROR: Confrom name and new name does not match. Please enter the same name.")
            return
        All_Student[unique_id]['name'] = new_name 
        print("="*40)
        print("Name Successfully Update")
        print("="*40)

    def roll_number():
        print("="*40)
        unique_id = get_unique_id()
        
        new_roll = input("Enter your new Roll number:- ")
        if not new_roll.strip():
            print("ERROR: Roll number connect be empty.")
            return
        if not new_roll.isdigit():
            print("ERROR: Invalid new roll number. Please enter a valid roll number using digit only")
            return
        confrom_roll = input("Enter confrom roll number:- ")
        if not confrom_roll.strip():
            print("Confrom roll number connect be empty.")
            return
        if not confrom_roll.isdigit():
            print("ERROR: Invalid confrom roll number. Please enter a valid confrom roll number using digit only")
            return
        if confrom_roll != new_roll:
            print("ERROR: Confrom roll number and new roll number does not match. Please enter the same roll number.")
            return
        All_Student[unique_id]['roll'] = new_roll 
        print("="*40)
        print("Roll number Successfully Update")
        print("="*40)

    def age():
        print("="*40)
        unique_id = get_unique_id()
        
        Age = input("Enter your new age:- ")
        if not Age.strip():
            print("ERROR: Age connect be empty.")
            return
        if not Age.isdigit():
            print("ERROR: Age must contain digits only.")
            return
        if not 3 <= int(Age) <=100:
            print("ERROR: Age must be between 3 and 100.") 
            return
        confrom_age = input("Enter confrom age:- ")
        if not confrom_age.strip():
            print("Confrom age connect be empty.")
            return
        if not confrom_age.isdigit():
            print("ERROR: Invalid confrom age. Please enter a valid confrom age using digit only")
            return
        if confrom_age != Age:
            print("ERROR: Confrom age and new age does not match. Please enter the same age.")
            return
        All_Student[unique_id]['age'] = Age 
        print("="*40)
        print("Age Successfully Update")
        print("="*40)

    def mobile_number():
        print("="*40)
        unique_id = get_unique_id()
        
        New_mobile_number = input("Enter your new mobile number:- ")
        if not New_mobile_number.strip():
            print("ERROR: mobile number connect be empty.")
            return
        if not New_mobile_number.isdigit():
            print("ERROR: Invalid new mobile number. Please enter a valid mobile number using digit only")
            return
        if len(New_mobile_number) != 10:
            print("ERROR: Mobile number must contain exactly 10 digits.")
            return
        
        confrom_mobile = input("Enter confrom mobile number:- ")
        if not confrom_mobile.strip():
            print("Confrom mobile number connect be empty.")
            return
        if not confrom_mobile.isdigit():
            print("ERROR: Invalid confrom mobile number. Please enter a valid confrom mobile number using digit only")
            return
        if confrom_mobile != New_mobile_number:
            print("ERROR: Confrom mobile number and new mobile does not match. Please enter the same mobile number.")
            return
        All_Student[unique_id]['phone'] = New_mobile_number 
        print("="*40)
        print("Mobile Number Successfully Update")
        print("="*40)



    def gmail():
        print("="*40)
        unique_id = get_unique_id()
        
        New_Gmail = input("Enter your new gmail:- ")
        if not New_Gmail.strip():
            print("ERROR: gmail connect be empty.")
            return
        if "@" not in New_Gmail and "." not in New_Gmail:
            print("ERROR: Invalid new gmail.")
            return
        
        confrom_gmail = input("Enter confrom gmail:- ")
        if not confrom_gmail.strip():
            print("Confrom gmail connect be empty.")
            return
        if "@" not in confrom_gmail or "." not in confrom_gmail:
            print("ERROR: Invalid confrom gmail.")
            return
        if confrom_gmail != New_Gmail:
            print("ERROR: Confrom gmail and new gmail does not match. Please enter the same gmail.")
            return
        All_Student[unique_id]['email'] = New_Gmail 
        print("="*40)
        print("Gmail Successfully Update")
        print("="*40)

    def city():
        print("="*40)
        unique_id = get_unique_id()
        
        New_city = input("Enter your new city:- ")
        if not New_city.strip():
            print("ERROR: city connect be empty.")
            return
        
        confrom_city = input("Enter confrom city:- ")
        if not confrom_city.strip():
            print("Confrom city connect be empty.")
            return
        if confrom_city != New_city:
            print("ERROR: Confrom city and new city does not match. Please enter the same city.")
            return
        All_Student[unique_id]['city'] = New_city 
        print("="*40)
        print("City Successfully Update")
        print("="*40)

    def marks():
        print("="*40)
        unique_id = get_unique_id()
        
        New_marks = input("Enter your new marks:- ")
        if not New_marks.strip():
            print("ERROR: marks connect be empty.")
            return
        if not New_marks.isdigit():
            print("ERROR: Invaild marks. Please enter a valid marks using digit only.")
            return
        
        confrom_marks = input("Enter confrom marks:- ")
        if not confrom_marks.strip():
            print("Confrom marks connect be empty.")
            return
        if confrom_marks != New_marks:
            print("ERROR: Confrom marks and new marks does not match. Please enter the same marks.")
            return
        All_Student[unique_id]['marks'] = New_marks 
        print("="*40)
        print("Marks Successfully Update")
        print("="*40)


    def branch():
        print("="*40)
        unique_id = get_unique_id()
        
        New_class = input("Enter your new class/branch:- ")
        if not New_class.strip():
            print("ERROR: class/branch connect be empty.")
            return
        if not New_class.replace(" ","").isalpha():
            print("ERROR: Invalid new class. Please enter a valid class using letters and spaces only")
            return
        
        confrom_class = input("Enter confrom class/branch:- ")
        if not confrom_class.strip():
            print("Confrom class/branch connect be empty.")
            return
        if not confrom_class.replace(" ","").isalpha():
            print("ERROR: Invaild confrom class/branch. Please enter a valid class/branch using latters only.")
            return
    
        if confrom_class != New_class:
            print("ERROR: Confrom class/branch and new city does not match. Please enter the same class/branch.")
            return
        All_Student[unique_id]['clas'] = New_class 
        print("="*40)
        print("Class/Branch Successfully Update")
        print("="*40)


    while True:
        menu()
        
        Choice = input("Enter your choice(1-9):- ")
        if Choice =='1':
           name()
        elif Choice =='2':
            roll_number()
        elif Choice =='3':
            age()
        elif Choice =='4':
            mobile_number()
        elif Choice =='5':
            gmail()
        elif Choice =='6':
            city()
        elif Choice =='7':
            marks()
        elif Choice =='8':
            branch()
        elif Choice =='9':
            break
        else:
            print("In-valid choice. Please try again.")

    save_student_data()

load_student()
        
while True:
    menu()
    Choice = input("Enter your choice:- ")
    if Choice =="1":
        Add_students()
    elif Choice == '2':
        search_student()
    elif Choice == '3':
        delete_student()
    elif Choice == '4':
        Total_marks_percentage()
    elif Choice == '5':
        update_student_details()
    elif Choice == '6':
        break
    else:
        print("In-valid choice. Please try again.")