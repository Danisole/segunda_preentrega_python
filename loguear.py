import sys
import getpass

registro_User = sys.argv[1]
registro_pass = sys.argv[2]


def login(usuario,passw):

    if usuario in registro_User:
        if passw in registro_pass:
            return 1
        else:
            print("\n\tLo siento la contraseña no coincide\n")
    else:
        return 2

usuario=input('Usuario: ')
passw = getpass.getpass('Contraseña: ')

if login(usuario,passw)==1:
    print(f'Bienvenid@ {usuario.capitalize()}')
else:
    print('ERROR! El usuario no esta registrado')