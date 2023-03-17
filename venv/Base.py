import glob
str = ''
badpath = 'C:/Test'
goodpath = 'C:/Test/good'
for file in glob.glob(f'{badpath}/*bad.iso'):
    with open(file, encoding='utf8') as fMars:
        for line in fMars:
             str += line.replace('\n', ' ')
    file = (file[file.find("\\"): ])
    print(file)
    with open(f'{goodpath}{file.split(".")[0]}_good.iso', 'w', encoding='utf8') as result_file:
        result_file.write(str)
    print(str)
