
from spravochnik import  array

def find_person():
    find_person = str(input('Кого ищите?Введите Фамилию '))
    k=0
    for i in range(len(array)):
        for j in range(4):
            if array[i][j].upper() == find_person.upper():
                print(f'Фамилия  {array[i][j]} Имя {array[i][1]} Телефон {array[i][2]} Описание {array[i][3]}')
                k=k+1
                res = True
            else:
                if k==0:
                    res = 'нет таких'
    print(res)
    return