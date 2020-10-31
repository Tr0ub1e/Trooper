import os
import sys
import shutil
from sugar import decorator

class program(decorator):

    _drives = []
    _user = None
    _name_os = None

    def __init__(self):

        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if os.path.exists('{}:'.format(letter)):
                self._drives.append(letter)

        self._user = os.getlogin()
        self._name_os = os.getenv('OS')

    def __str__(self):
        print('Пользователь {1} \nДиски в системе {0}\nОС {2}\nТекущая директория {3}'.format(self._drives, self._user, self._name_os, os.getcwd()))


    @decorator.select
    def show_files(self):
        for file in os.listdir(os.getcwd()):
            yield file

    @decorator.drives
    def info_drives(self):
        #returns drive name and total, used, free memory
        for drive in self._drives:
            yield drive, shutil.disk_usage(drive+':/')

    @decorator.weightf
    def weightf(self):
        c = {}

        for file in os.listdir():

            if len(file.split('.')) > 1:
                c[file.split('.')[-1]] = os.path.getsize(file)

        return c


    def cmd_processor(self, command):

        _cmds = {'info': self.__str__, 'select_path': self.show_files, 'analyses':self.weightf,
                 'drives': self.info_drives,
                 'exit':exit}

        if command == 'init':
            return _cmds.keys()

        try:
            _cmds[command]()

        except KeyError:
            print('---\nWrong cmd\n\n'+'\n'.join(_cmds.keys())+'\n')
