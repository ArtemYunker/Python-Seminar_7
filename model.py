from spravochnik import array

def expot_txt():
    data = open ('file_export.txt','w',encoding='utf-8')
    for i in range(len(array)):
        for j in range(4):
            data.write('\n')
            if j == 0:
                data.write(f'Фамилия  {str(array[i][j])}' + '\n')
                data.write('\n')
            if j == 1:
                data.write(f'Имя  {str(array[i][j])}' + '\n')
                data.write('\n')
            if j == 2:
                data.write(f'Телефон  {str(array[i][j])}' + '\n')
                data.write('\n')
            if j == 3:
                data.write(f'Описание  {str(array[i][j])}' + '\n')
                data.write('\n')
    data.close()
    return




def expot_csv():
    import csv
    with open("file_export.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
        file_writer.writerow(["Фамилия", "Имя", "Телефон","Описание"])
        for i in range(len(array)):
            file_writer.writerow(array[i])
    return

def import_txt():
    new_array = []
    data = open('file_export.txt', 'r',encoding='utf-8')
    for line in data:
        s = data.read().split()
        new_array.append(s)
    data.close()
    print(*new_array)
    return

def import_cvs():
    import csv
    array_cvs = []

    with open("file_export.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        for i in file_reader:
            array_cvs.append(i)
    del array_cvs[0]
    print(array_cvs)
    return