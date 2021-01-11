import subprocess

# autocrlf: input for linux, true for Windows/MacOS, false otherwise
# editor: VSCode = code
INFORMATION = {
    'Username' : ['user.name'],
    'Email' : ['user.email'],
    'Dev OS' : ['core.autocrlf'],
    'Dev editor' : ['core.editor'],
}

def gitinit():   

    print('Please enter your information below:')
    
    for k in INFORMATION.keys():
        INFORMATION[k].append(input(f'\t{k}: '))
        subprocess.run([
            'git', 'config', '--global', f'{INFORMATION[k][0]}', f'{INFORMATION[k][1]}' 
        ])

if __name__ == "__main__":
    gitinit()


    