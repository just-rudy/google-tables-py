import gspread
import pandas as pd
# import string

# путь к JSON
gc = gspread.service_account(filename='/home/rudy/STUD/google-tables-py/api-experiments-395416-ff82bc7deac8.json')

# та самая таблица, в которую я лезу
sh = gc.open("try-py")

# если в столбце G стоит статус "в процессе"
# записываем имя из столбца A в текстовый файл

data = open("guys_in_prog.txt", "w")

for i in range(2, 31):
    num = 'G' + str(i)
    # print("type: ", type('G2'))
    # print("num: ", num)
    # print('just - ', sh.sheet1.get(num))
    status = str(sh.sheet1.acell(num).value)
    # print(status)
    if status.lower() in " в процессе ":
        num = 'A' + str(i)
        data.write(sh.sheet1.acell(num).value + "\n")
# print("end")

data.close()