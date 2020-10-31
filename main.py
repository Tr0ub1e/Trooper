import os
import sys
from additions import *

def main():

    wpath = os.getcwd()
    client = program()

    print('Возможности\n'+'\t'.join(client.cmd_processor('init')))

    while True:
        client.cmd_processor(input('>>> '))

if __name__ == '__main__':
    main()
