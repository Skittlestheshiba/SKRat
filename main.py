import colors
import sys
import os


def menu():
    print(colors.blue('|--SKRat--|') + '\n \n \n \n \n \n \n' + colors.blue('1) Option 1  2) Option 2 E) Exit'))

selection = input(colors.blue('>'))

menu()
if selection == '1':
    print(colors.red('1'))

elif selection == '2':
    print(colors.red('2'))

elif selection == 'E':
    sys.exit()

else:
    if os.name == 'nt':
        os.system('cls')

    else:
        os.system('clear')

    menu()
