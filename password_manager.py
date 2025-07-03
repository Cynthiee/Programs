from cryptography.fernet import Fernet
'''This script is a simple password manager that allows users to add and view passwords securely.
It uses the cryptography library to encrypt and decrypt passwords.
The user can add a new password or view existing passwords. The passwords are stored in a text file.  '''

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key  


master_pwd = input('What is the master password? ')
key = load_key() + master_pwd.encode()
# The master password is appended to the key for additional security
fer = Fernet(key)
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print('User:', user, ',Password:',str(fer.encrypt(passw.encode())))

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + ' |' + str(fer.encrypt(pwd.encode())) + '\n')

while True:
    mode = input('Would you like to add a new password or view existing ones (view, add), press q to quit? ').lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode!')
        continue


