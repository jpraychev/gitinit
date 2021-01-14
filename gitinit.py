import subprocess
from prettytable import PrettyTable

# autocrlf: input for linux, true for Windows/MacOS, false otherwise
# editor: VSCode = code

INFO = {
    'Username' : ['user.name'],
    'Email' : ['user.email'],
    'Dev OS' : ['core.autocrlf'],
    'Dev editor' : ['core.editor'],
}

def set_git_info():   

    print('Please enter your INFO below:')
    
    for k in INFO.keys():
        INFO[k].append(input(f'\t{k}: '))

        # Basic checks for user provided operating system
        
        if k == 'Dev OS':
            if INFO[k][1].lower() == 'linux':
                INFO[k][1] = 'input'
            elif INFO[k][1].lower() == 'windows':
                INFO[k][1] = 'true'
            else:
                INFO[k][1] = 'false'

        subprocess.run([
            'git', 'config', '--global', f'{INFO[k][0]}', f'{INFO[k][1]}' 
        ])

def get_git_info():

    infoTable = PrettyTable(['Variable', 'Value'])
    infoTable.title = 'Global git settings'
    
    for k in INFO.keys():
        infoTable.add_row([f'{k}', subprocess.run(['git', 'config', '--global', f'{INFO[k][0]}'], capture_output=True, text=True).stdout.strip('\n')])
    
    return infoTable

if __name__ == "__main__":
    
    print(get_git_info())