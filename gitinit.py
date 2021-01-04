# autocrlf: Input for linux, True for Windows/MacOS, False otherwise
# editor: VSCode = code

def gitinit():
    print('A python module to initialize git for your current project')
    username = input(f'Enter your name: ')
    email = input(f'Enter your email address: ')
    autocrlf = input(f'Enter your development OS (Linux/MacOS/Windows): ')
	editor = input(f'Enter your development editor. See gitinit --help for supported editors: ')
    
if __name__ == "__main__":
    gitinit()