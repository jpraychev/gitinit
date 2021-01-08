import subprocess

# autocrlf: Input for linux, True for Windows/MacOS, False otherwise
# editor: VSCode = code
INFORMATION = {
    'user.name' : [],
    'user.email' : [],
    'core.autocrlf' : [],
    'core.editor' : [],
}

def gitinit():   

    print('Please enter your information below:')

    INFORMATION['user.name'].append(input(f'\tUsername: '))

    # email = input(f'\tEmail address: ')
    # autocrlf = input(f'\tDevelopment OS (Linux/MacOS/Windows): ')
    # editor = input(f'\tDevelopment editor: ')

    # subprocess.run([
    #     'git', 'config', '--global', 'user.name', f'{username}' 
    # ])

if __name__ == "__main__":
    gitinit()

    # INFORMATION['username'].append('jraychev')
    print(INFORMATION)

    