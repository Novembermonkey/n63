from service import login ,register, logout,todo_list,todo_add,login_required,is_admin, change_role

def menu():
    print('Login => 1')
    print('Register => 2')
    print('Logout => 3')
    print('Todo List => 4')
    print('Todo Add => 5')
    print('Add Admin => 6')
    print('Delete Admin => 7')
    print('Quit => q')
    return input('Enter: ')



def login_response():
    username = input('Username : ')
    password = input('Password : ')
    response = login(username,password)
    print(response.message)
    
    

def register_response():
    username = input('Username : ')
    password = input('Password : ')
    response = register(username,password)
    print(response.message)
    
    
    

def logout_response():
    response = logout()
    print(response.message)
    

@login_required
@is_admin  
def create_todo():
    title = input('Title : ')
    user_id = int(input('User id: '))
    response = todo_add(title,user_id)
    return response

# ADMIN => admin123 - admin data
@is_admin
@login_required
def promote_to_admin():
    username = input('Username: ')
    response = change_role(username, 'admin')
    return response

@is_admin
@login_required
def delete_admin():
    username = input('Username: ')
    response = change_role(username, 'user')
    return response


    

def run():
    while True:
        choice = menu()
        if choice == '1':
            login_response()
        
        elif choice == '2':
            register_response()
        
        elif choice == '3':
            logout_response()
        
        elif choice == '4':
            todo_list()
        
        elif choice == '5':
            response = create_todo()
            print(response.message)

        elif choice == '6':
            response = promote_to_admin()
            print(response.message)
        elif choice == '7':
            response = delete_admin()
            print(response.message)
            
        elif choice == 'q':
            break
        
        
if __name__ == '__main__':
    run()

# husan => husan2011
# js => 12345678
#ADMIN => admin123
