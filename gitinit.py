import subprocess
import sys
from prettytable import PrettyTable


def switcher(first):

    switcher = {
        # Text editors
        'vim' : 'vim',
        'emacs' : 'emacs',
        'code' : 'code -w',
        'nano' : 'nano -w',
        'atom' : 'atom --wait',
        'sublime' : 'subl -n -w',

        # Operating systems
        'linux' : 'input',
        'macos' : 'input',
        'windows' : 'true'
    }

    return switcher.get(first)


def set_git_info():   

    print('\nPlease enter your information below:\n')
    
    for k in INFO.keys():
        INFO[k].append(input(f'{k}: '))

        if k == 'Dev OS' or k == 'Dev editor':
            INFO[k][1] = switcher(INFO[k][1].lower())

        subprocess.run([
            'git', 'config', '--global', f'{INFO[k][0]}', f'{INFO[k][1]}' 
        ])

    print(get_git_info())


def get_git_info():

    infoTable = PrettyTable(['Variable', 'Value'])
    infoTable.title = 'Global git settings'
    
    for k in INFO.keys():
        infoTable.add_row([f'{k}', subprocess.run(['git', 'config', '--global', f'{INFO[k][0]}'], capture_output=True, text=True).stdout.strip('\n')])
    
    return infoTable


def menu():
    print('\n********* Welcome to GIT init *********\n')
    choice = input(
        '1: Set user information\
         \n2: Get user information\
         \n3: Print help menu\
         \n4: Exit the program\n\
         \nPlease enter an option: '
    )

    if choice == '1':
        set_git_info()
    elif choice == '2':
        print(get_git_info())
    elif choice == '3':
        menu()
    else:
        sys.exit()


if __name__ == "__main__":

    INFO = {
        'Username' : ['user.name'],
        'Email' : ['user.email'],
        'Dev OS' : ['core.autocrlf'],
        'Dev editor' : ['core.editor'],
    }

    menu()