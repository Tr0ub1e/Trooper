import os
from collections import Counter

class decorator:

    def drives(func):
        # sugar for function info_drives()
        def inner(*args, **kwargs):
            print('>>> Обзор памяти ')

            data = tuple(func(*args, **kwargs))

            for item in data:
                print('Disk %s:/' % item[0])

                print("Total %d GB" % (item[1][0] // 2**30), end='\t')
                print("Used %d GB" % (item[1][1] // 2**30), end='\t')
                print("Free %d GB" % (item[1][2] // 2**30), end='\n\n')

        return inner

    def weightf(func):

        def inner(*args, **kwargs):
            c = func(*args, **kwargs)
            for i in c:
                print('Type {} {} Kbytes'.format(i, c[i] // 10**3))

        return inner


    def select(func):
        #sugar for function show_files()

        def inner(*args, **kwargs):

            drive_name = input('Путь: ')
            os.chdir(drive_name)
            print('Текущая директория >>> ', os.getcwd())

            c = Counter()

            for file in func(*args, **kwargs):
                #print(file)
                if len(file.split('.')) > 1:
                    c[file.split('.')[-1]] += 1
                else:
                    c['other'] += 1

            print('Типы файлов >>>\n')
            for key in c.keys():
                print(key, c[key])


        return inner
