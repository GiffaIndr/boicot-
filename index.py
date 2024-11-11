import sys

def auth():
    print("1. Login")
    print("2. Register")
    print("3. Out")
 
def login():
    global logged_user
    email = input("Email: ")
    password = input("Password: ")
    
    with open("data-user.txt", "r") as data_user:
        users = data_user.read().strip().split("\n\n") 
        login_success = False
        
        for user in users:
            if user.strip():
                user_data = user.splitlines()
                user_name = user_data[0].split(": ")[1].strip()
                user_role = user_data[2].split(": ")[1].strip()
                user_email = user_data[3].split(": ")[1].strip()
                user_password = user_data[4].split(": ")[1].strip()
                    
                if user_email == email and user_password == password:
                        print("Login successful!")
                        login_success = True
                        logged_user = user_name 
                        if user_role == "admin":
                            admin_menu()  
                        elif user_role == "user":
                            user_menu()   
                        elif user_role == "superadmin":
                            superadmin_menu()
                        break
        if not login_success:
            print("Username or password does not exist, please check again.")
            
def register():
    name = input("Name: ")
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")
    
    if not name or not username or not email or not password:
        print("Please fill all fields!")
    else:
        with open("data-user.txt", "r") as data_user:
            users = data_user.read().split("\n\n")
            
            for user in users:
                if user.strip():
                    user_data = user.splitlines()
                    existing_email = user_data[3].split(": ")[1].strip()
                    existing_username = user_data[1].split(": ")[1].strip()
                    if username == existing_username:
                        print("Username already exists")
                        return
                    if email == existing_email:
                        print("Email already registered")
                        return
                    
        role = "user"
        data = "Name: {}\nUsername: {}\n Role: {}\n Email: {}\n Password: {}\n\n".format(name, username, role, email, password)
        with open("data-user.txt", "a") as data_user:
            data_user.write(data)
        print("Registration success please login!")
        auth_menu()

def read_user():
    data_user = open("data-user.txt", "r")
    user = data_user.read()
    print("-" * 20)
    print(user)
    print("-" * 20)
    print(list_user_menu())

def create_user():
    name = input("Name: ")
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")
    role = input("Role (superadmin/admin/user): ")
    
    if not name or not username or not email or not password:
        print("Please fill all fields!")
    else:
        with open("data-user.txt", "r") as data_user:
            users = data_user.read().split("\n\n")
            
            for user in users:
                if user.strip():
                    user_data = user.splitlines()
                    existing_email = user_data[3].split(": ")[1].strip()
                    existing_username = user_data[1].split(": ")[1].strip()
                    if username == existing_username:
                        print("Username already exists")
                        return
                    if email == existing_email:
                        print("Email already registered")
                        return
                    
        data = "Name: {}\nUsername: {}\n Role: {}\n Email: {}\n Password: {}\n\n".format(name, username, role, email, password)
        with open("data-user.txt", "a") as data_user:
            data_user.write(data)
        print("Success added user!")
        superadmin_menu()
    
def update_user():
    search_name = input("Type name to update: ")
    user_found = False
    with open("data-user.txt", 'r') as data_user:
        users = data_user.read().split("\n\n")    
        
    updated_users = []
    for user in users:
        if user.strip():
            user_data = user.splitlines()
            name = user_data[0].split(": ")[1].strip()
            
            if name.lower() == search_name.lower():
                print("User found! please input this field (click enter for continue):")
                
                new_name = input(f"Name ({name}): ") or name
                new_username = input(f"Username ({user_data[1].split(': ')[1].strip()}): ") or user_data[1].split(": ")[1].strip()
                new_role = user_data[2].split(": ")[1].strip()  # Role tetap sama
                new_email = input(f"Email ({user_data[3].split(': ')[1].strip()}): ") or user_data[3].split(": ")[1].strip()
                new_password = input(f"Password ({user_data[4].split(': ')[1].strip()}): ") or user_data[4].split(": ")[1].strip()
                
                updated_user = f"Name: {new_name}\nUsername: {new_username}\n Role: {new_role}\n Email: {new_email}\n Password: {new_password}"
                updated_users.append(updated_user)
                user_found = True
                print("Successfully update user!")
            else:
                updated_users.append(user)
                
        if not user_found:
            print(f"User with name '{search_name}' not found")
        
        with open("data-user.txt", "w") as data_user:
            data_user.write("\n\n".join(updated_users))
            
def update_profile():
    global logged_user
    if not logged_user:
        print("You need to login first.")
        return

    user_found = False

    with open("data-user.txt", "r") as data_user:
        users = data_user.read().split("\n\n")

    updated_users = []  

    for user in users:
        if user.strip():
            user_data = user.splitlines()
            name = user_data[0].split(": ")[1].strip()

            if name == logged_user: 
                print("Please enter new data (click enter for continue):")

                new_name = input(f"Nama ({name}): ") or name
                new_username = input(f"Username ({user_data[1].split(': ')[1].strip()}): ") or user_data[1].split(": ")[1].strip()
                new_role = user_data[2].split(": ")[1].strip()  
                new_email = input(f"Email ({user_data[3].split(': ')[1].strip()}): ") or user_data[3].split(": ")[1].strip()
                new_password = input(f"Password ({user_data[4].split(': ')[1].strip()}): ") or user_data[4].split(": ")[1].strip()
                updated_user = f"Name: {new_name}\nUsername: {new_username}\n Role: {new_role}\n Email: {new_email}\n Password: {new_password}"
                updated_users.append(updated_user)
                user_found = True
                print("Data Anda berhasil diperbarui!")
            else:
                updated_users.append(user)
    if user_found:
        with open("data-user.txt", "w") as data_user:
            data_user.write("\n\n".join(updated_users))
    else:
        print("Data pengguna tidak ditemukan.")
        
        
def search_user():
    search_name = input("Search name: ").strip()
    with open("data-user.txt", "r") as data_user:
        users = data_user.read().split("\n\n")
        user_found = False
        
        for user in users:
            if user.strip():
                user_data = user.splitlines()
                name = user_data[0].split(": ")[1].strip()
                
                if name.lower() == search_name.lower():
                    print("User found")
                    print(user)
                    user_found = True
                    break
        if not user_found:
            print(f"No user found with the name '{search_name}'")
            
def filter_user_by_role():
     selected_role = input("choose role for shorting (admin/user/superadmin): ").strip().lower()
     
     if selected_role not in ["admin", "user", "superadmin"]:
        print("Role that you choose is not valid, please choose 'admin', 'user', 'superadmin'.")
        return
     with open("data-user.txt", "r") as data_user:
        users = data_user.read().strip().split("\n\n")
        selected_role_users = []
        for user in users:
          if user.strip(): 
            user_data = user.splitlines()
            role = user_data[2].split(": ")[1].strip() 
            
            if role == selected_role:
                selected_role_users.append(user)  
                
        if selected_role_users:
            print(f"\nUsers with role '{selected_role}':")
        for user in selected_role_users:
            print(user)
            print("-" * 20)
        else:
          print(f"No user with role '{selected_role}'.")

def delete_user():
    name = input("name: ")

    with open("data-user.txt", "r") as data_user:
        users = data_user.readlines()
        
    found = False
    with open("data-boicot.txt", "w") as data_user:
      i = 0
      while i < len(users):
            if users[i].strip() == f"name: {name}":
              found = True
              i += 5
            else:
              data_user.write(users[i])
              i += 1
    if found:
         print(f"Data untuk '{name}' telah dihapus")
    else:
        print(f"Data untuk '{name}' tidak ada")

def read_product():
    data_boicot = open("data-boicot.txt", "r")
    boicot = data_boicot.read()
    print("-" * 20)
    print(boicot)
    print("-" * 20)
    print(list_product_menu())
    
def create_product():
    name = input("Name: ")
    proof = input("Proof: ")
    proofurl = input("Proof Url: ")
    
    if not name or not proof or not proofurl:
        print("Please fill all fields!")
    else:      
        with open("data-boicot.txt", "r") as data_boicot:
         boicots = data_boicot.read().split("\n\n")

        for boicot in boicots:
            if boicot.strip():
                data_boicot = boicot.splitlines()
                existing_name = data_boicot[0].split(": ")[1].strip()
                existing_proof = data_boicot[1].split(": ")[1].strip()
                existing_proofurl = data_boicot[2].split(": ")[1].strip()
                if name == existing_name:
                    print("Name already exists")
                    return
                if proof == existing_proof:
                    print("Proof already exists")
                    return
                if proofurl == existing_proofurl:
                    print("Proofurl already exists")
                    return
                
        teks = "Name: {}\nProof: {}\nProofurl: {}\n\n".format(name, proof, proofurl)
        with open("data-boicot.txt", "a") as data_boicot:
            data_boicot.write(teks)
            print("Successfully added boicot product!")
            
def update_product(): 
    search_product = input("Type name to update: ")
    product_found = False
    with open("data-boicot.txt", 'r') as data_product:
        products = data_product.read().split("\n\n")    
        
    updated_products = []
    for product in products:
        if product.strip():
            product_data = product.splitlines()
            name = product_data[0].split(": ")[1].strip()
            
            if name.lower() == search_product.lower():
                print("product found! please input this field (click enter for continue):")
                
                new_name = input(f"Name ({name}): ") or name
                new_proof = input(f"Proof ({product_data[1].split(': ')[1].strip()}): ") or product_data[1].split(": ")[1].strip()
                new_proofurl = input(f"Proofurl ({product_data[2].split(': ')[1].strip()}): ") or product_data[2].split(": ")[1].strip()
              
                updated_product = f"Product: {new_name}\nProof: {new_proof}\n Proofurl: {new_proofurl}"
                updated_products.append(updated_product)
                product_found = True
                print("Successfully update product!")
            else:
                updated_products.append(product)
                
        if not product_found:
            print(f"product with name '{search_product}' not found")
        
        with open("data-boicot.txt", "w") as data_product:
            data_product.write("\n\n".join(updated_products))

def search_product():
     search_name = input("Search name: ").strip()
     with open("data-boicot.txt", "r") as data_product:
        products = data_product.read().split("\n\n")
        product_found = False
        
        for product in products:
            if product.strip():
                product_data = product.splitlines()
                name = product_data[0].split(": ")[1].strip()
                
                if name.lower() == search_name.lower():
                    print("product found")
                    print(product)
                    product_found = True
                    break
        if not product_found:
            print(f"No product found with the name '{search_name}'")


def delete_product():
    name = input("name: ")

    with open("data-boicot.txt", "r") as data_boicot:
        boicots = data_boicot.readlines()
        
    found = False
    with open("data-boicot.txt", "w") as data_boicot:
      i = 0
      while i < len(boicots):
            if boicots[i].strip() == f"name: {name}":
              found = True
              i += 3
            else:
              data_boicot.write(boicots[i])
              i += 1
    if found:
         print(f"Data untuk '{name}' telah dihapus")
    else:
        print(f"Data untuk '{name}' tidak ada")
        


       
def list_user_menu():
    while True:
        print("Choose one option:")
        print("1. Search user ")
        print("2. filter by role ")
        print("3. Main menu")
        pilihan = input("Choose (1/2/3): ")
        if pilihan == "1":
            print(search_user())
        elif pilihan == "2":
            print(filter_user_by_role())
        elif pilihan == "3":
            print(superadmin_menu())
        else:
            print("Invalid Input, please try again")
            
def list_product_menu():
    while True:
        print("Choose one option:")
        print("1. Search product ")
        print("2. Main menu")
        pilihan = input("Choose (1/2/3): ")
        if pilihan == "1":
            print(search_product())
        elif pilihan == "2":
            print(user_menu())
        else:
            print("Invalid Input, please try again")
        
def auth_menu(): 
    while True:
        auth()
        pilihan = input("Choose (1/2/3): ")
        if pilihan == "1":
            print(login())
        elif pilihan == "2":
            print(register())
        elif pilihan == '3':
            print("Thank you for using our app!!\nNever stop BOICOT!!!")
            print(sys.exit())
        else:
            print("Invalid input, please try again.")

def superadmin_menu():
    while True:
        print(f"Welcome {logged_user}!!")
        print()
        print("1. See user list ")
        print("2. Create user ")
        print("3. edit user ")
        print("4. Delete user ")
        print("5. Logout")
        pilihan = input("Choose (1/2/3/4/5/6/7): ")
          
        if pilihan == '1':
            print(read_user())
        elif pilihan == '2':
            print(create_user())
        elif pilihan == '3':
            print(update_user())
        elif pilihan == '4':
            print(delete_user())
        elif pilihan == '5':
            print("Logging out...")
            auth_menu()
        else:
            print("Invalid input, please try again.")
        
def admin_menu():
    while True:
        print(f"Welcome {logged_user}!!")
        print()
        print("1. Create Product Boicot ")
        print("2. See list boicot ")
        print("3. edit product boicot ")
        print("4. Delete product boicot ")
        print("5. Logout")
        pilihan = input("Choose (1/2/3/4/5/6): ")
        
        if pilihan == '1':
            print(create_product())
        elif pilihan == '2':
            print(read_product())
        elif pilihan == '3':
            print(update_product())
        elif pilihan == '4':
            print(delete_product())
        elif pilihan == '5':
            print("Logging out...")
            auth_menu()
        else:
            print("Invalid input, please try again.")

def user_menu():
    while True:
        print(f"Welcome {logged_user}!!")
        print()
        print("1. List boicot ")
        print("2. Update user profile ")
        print("3. Logout")
        pilihan = input()
        if pilihan == '1':
            print(read_product())   
        elif pilihan == '2':
            print(update_profile())
        elif pilihan == '3':
            print("Logging out...")
            auth_menu()
        else:
            print("Invalid input, please try again.")

            
auth_menu()