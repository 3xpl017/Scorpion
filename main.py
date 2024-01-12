# importamos las librerías
import os, time, sys, socket
from colorama import Fore, Back

# configuramos las variables principales
name = socket.gethostname()
ipv4 = socket.gethostbyname(name)

# ponemos a punto los colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# HACER EL INSTALADOR EN EL MISMO PROGRAMA DE PYTHON QUE INCLUYA INSTALAR MSFVENOM

# hacemos el menú
def menu():
    os.system('clear')
    time.sleep(1)

    title = f'''
                 ......                                         
               .+*+:.             [ 🅢 🅒 🅞 🅡 🅟 🅘 🅞 🅝 ] -----------------------------                         
              .-##.                                           
             .*#*.                [!] By 3xpl017: https://www.github.com/3xpl017                   
            .+%*..                [>] Scorpion v1: Payload generator with MsfVenom
            :#*-.                                            
            -##=                  [!] Utiliza este software con propósitos éticos                       
            :%#=.                 [>] Ip: {ipv4}
            .*@%.                 [>] Nombre de la máquina: {name}                           
                .#%%:     =+=..                                 
            .:=*#**#=--:. ..+.-:+**=.                           
        -=:-:.-#***++===:.--.=+=*+-.                         
        .=. .:+##%*##**++++==-.**-.-++:.                      
    .:==. :*+=..+%#######*=====+-*=--+=.:---:...             
    ....  .+=. :*###%#**#@@%#*#@#+#:.++***+@#+===-.           
        ..*: :*...-**%%%%@%%@%%%@%##%#+:...-+#*++=..         
        .=-...=+. .=++*++***#%%@%===:..    ....=+*#-.         
            .-=.  :++====+*+==:......         :***-.          
            .... .*%#**###*+-...            .......           
                .#*####%%%%%####*+:.                         
                    .:+###%%@%##%#*=:.                          
                    .........                                
    '''
    print(Fore.RED + Back.RESET + title)

    options = '''
    [00] Salir
    [01] Empezar a generar payloads con MsfVenom
    '''
    print(Fore.BLUE + Back.RESET + options)

    choice = input(Fore.WHITE + Back.RED + f'{name}@Scorpion:~$ ')

    if choice == '00':
        os.system('clear')
        print(Fore.RESET + Back.RESET)
        sys.exit()

    elif choice == '01':
        os.system('clear')
        time.sleep(1)
        options = '''
    [00] Salir
    [01] Volver al menú
    [02] Ver la lista de payloads disponibles
    [03] En proceso...
    '''
        print(Fore.BLUE + Back.RESET + options)
        choice = input(Fore.WHITE + Back.RED + f'{name}@Scorpion:~$ ')

        if choice == '00':
            os.system('clear')
            print(Fore.RESET + Back.RESET)
            sys.exit()

        elif choice == '01':
            os.system('clear')
            choice = input(Fore.WHITE + Back.RED + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
            print(Fore.RESET + Back.RESET)
            menu()

        elif choice == '02':
            os.system('clear')
            os.system('msfvenom -l payloads')
            choice = input(Fore.WHITE + Back.RED + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
            print(Fore.RESET + Back.RESET)
            menu()

        else:
            os.system('clear')
            print(Fore.BLUE + Back.RESET + '\n[>] Error: Command not found')
            choice = input(Fore.WHITE + Back.RED + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
            print(Fore.RESET + Back.RESET)
            menu()

    else:
        os.system('clear')
        print(Fore.BLUE + Back.RESET + '\n[>] Error: Command not found')
        choice = input(Fore.WHITE + Back.RED + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
        print(Fore.RESET + Back.RESET)
        menu()

menu()