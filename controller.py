
import model
import view

def main_function():
    view.find_person()
    model.expot_txt()
    model.expot_csv()
    print()
    print('Получение списка из файла TXT')
    model.import_txt()
    print()  
    print('Получение списка из файла СVS')
    print()  
    model.import_cvs()

