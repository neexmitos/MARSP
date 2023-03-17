import glob
from py7zr import SevenZipFile
from datetime import date
year = str(date.today())[0:4]
print(year)
current_date = str(date.today())
formated_date = current_date[8:10] + '.' + current_date[5:7] + '.' + current_date[0:4]
str = ''
archpath = 'C:/Test'
goodpath = 'C:/Test/good'
print(formated_date)
for file in glob.glob(f'{archpath}/*{formated_date}_imported_isos.7z'):
    with SevenZipFile(file, 'r') as arch:
        arch.extractall()
    print(file)
    # with open(file, encoding='utf8') as fMars:
    #     for line in fMars:
    #          str += line.replace('\n', ' ')
    # file = (file[file.find("\\"): ])
    # with open(f'{goodpath}{file.split(".")[0]}_good.iso', 'w', encoding='utf8') as result_file:
    #     result_file.write(str)
    # print(str)
# with SevenZipFile('123.7z', 'r') as arch:
#     arch.extractall()

