import stdiomask
import hashlib
import datetime

### Configuration

log_file = "workspace/tmp/login.log" # Le fichier de journalisation
users_file = "workspace/tmp/userInfo.txt" # Le fichier de sotckage des info utilisateur

def main():
    """Fonction principale"""
    print_log('start', 'main()')
    # Afficher le menu
    print("MAIN MENU")
    print("---------")
    print()
    print("1 - Register")
    print("2 - Login")
    print()
    # Recuperer le choix de l'utilisateur et lancer la fonction associée
    while True: 
        print()
        user_choice = input("Choose An Option: ")
        if user_choice in ['1', '2']:
            break
    if user_choice == '1':
        register()
    else:
        login()

    print_log('stop', 'main()')

def print_log(msg, params):
    
    # Recuperer la date courante
    dateISOFormat = datetime.datetime.now()
    date = dateISOFormat.isoformat("-", "minutes")
    
    log_msg = date + ';' + msg + ';' + params + '\n'
    
    with open(log_file, "a") as filout:
        filout.write(log_msg)
    

def pwd_is_ok(pwd):
    if len(pwd) < 8:
        print("Mot de passe trop faible !!!")
        return False
    return True


def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def register():
    """Enregister un nouvel utilisateur dans la base de donnée"""

    print_log('start', 'register()')

    print("REGISTER")
    print("--------")
    print()
    while True:
        user_name = input("Enter Your Name: ")
        if user_name != '':
            break
     
    while True:
        #user_pwd = input("Enter Your Password: ")
        user_pwd = stdiomask.getpass("Enter Your Password: ")
        if pwd_is_ok(user_pwd):
            break
        print_log('mot de passe trop faible', user_name)

    while True:
        #confirm_pwd = input("Confirm Your Password: ")
        confirm_pwd = stdiomask.getpass("Confirm Your Password: ")
        if confirm_pwd == user_pwd:
            break
        else:
            print_log('password don\'t match', user_name)
            print("Passwords Don't Match")
            print()


    # Ajouter les infos du nouvel utilisateur dans le fichier
    add_user_info(user_name, hash_password(user_pwd))
    print_log('registered', user_name)
    print_log('stop', 'register()')
    print()
    print("Registered!")


def login():
    """Authentifier un utilisateur pour le connecter"""
    print_log('start', 'login()')
    print("LOGIN")
    print("-----")
    print()

    # Recuperer la liste des utilisateurs connus et leur mot de passe
    user_info = {}
    with open(users_file, 'r') as file:
        users_tab = file.readlines()

    for line in users_tab:
        user_data = line.split()
        user_info.update({user_data[0]: user_data[1]})

    # Recuperer le nom et le mot de passe de l'utilisateur voulant se
    # connecter
    while True:
        user_name = input("Enter Your Name: ")

        if user_name not in user_info:
            print_log('not registered', user_name)
            print("You Are Not Registered")
            print()
        else:
            break
    while True:
        #user_pwd = input("Enter Your Password: ")
        user_pwd = stdiomask.getpass("Confirm Your Password: ")
        
        # Verifier la correspondance des mots de passe
        if hash_password(user_pwd) != user_info[user_name]:
            print_log('incorrect password', user_name)
            print("Incorrect Password")
            print()
        else:
            break
        
    print_log('logged in', user_name)    
    print_log('stop', 'login()')
    print()
    print("Logged In!")


def add_user_info(user_name, user_pwd):
    """Ecrire le nom d'utilisateur et le mot de passe dans le fichier
        d'enregistrement"""

    with open(users_file, 'a') as file:
        file.write(user_name + " " + user_pwd)
        file.write('\n')

    print_log('add user', user_name)
    
# ============================================================================

if __name__ == '__main__':
    main()