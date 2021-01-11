import subprocess

# autocrlf: input for linux, true for Windows/MacOS, false otherwise
# editor: VSCode = code

INFO = {
    'Username' : ['user.name'],
    'Email' : ['user.email'],
    'Dev OS' : ['core.autocrlf'],
    'Dev editor' : ['core.editor'],
}

def gitinit():   

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

        

if __name__ == "__main__":
    gitinit()


    