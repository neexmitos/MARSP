## для корректной работы необходимо указать пути в файле conf
## файлы батники должны ОБЯЗАТЕЛЬНО называться *ГОДforbads.bat
## в батнике ОБЯЗАТЕЛЬНО для marceditor должна быть кодировка utf8 (она по умолчанию если что)
import glob, shutil, os
from py7zr import SevenZipFile
from datetime import date
year = str(date.today())[0:4] # переменная хранит текущий год (для доступа к bat файлу)

str = ''  # переменная в которой хранится
count = 0 # счетчик обработанных файлов
with open('conf') as path:
    badpath = path.readline().rstrip() #путь к входным (плохим файлам)
    goodpath = path.readline().rstrip() ##путь к выходным (хорошим файлам)
print('Пути к файлам хранятся в файле conf.')
print(f'Смотри файл. ENTER -- продолжить')
input()
for file in glob.glob(f'{badpath}/*bad.iso'): # блок исправления файла iso
    str = ''
    with open(file, encoding='utf8') as fMars:
        for line in fMars:
            str += line.replace('\n', ' ')   # удаление лишних символов перевода строки
    file = (file[file.find("\\"):])
    count += 1
    with open(f'{goodpath}{file.split(".")[0]}_good.iso', 'w', encoding='utf8') as result_file: # сохранение исправленного iso
        result_file.write(str)
print(f'Обработано {count} файлов.\nЗалить обработанные файлы в базу?? y - ДА anykey - НЕТ\nТолько при запуске с сервера OPAC из папки iso_to_import') # блок вызова батника обработчика
answer = input()
if answer == 'y' or answer == 'Y':
    for file in glob.glob(f'{goodpath}/*.iso'):
        shutil.move(file, os.getcwd())  # перемещение подготовленных файлов в папку iso_to_import
    print('Какой год скрипта??')  # выбор нужного батника
    scriptyear = input()
    for batfile in glob.glob(f'*{scriptyear}forbads.bat'):
        os.system(batfile)
        count += 1
