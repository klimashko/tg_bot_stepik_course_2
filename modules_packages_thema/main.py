print(dir()) #Пространство имен до импортов (способы импортов влияют на пространство имен)
from functions import get_double_number
from data import my_dict
from classes import *


print('Это исполняемый файл')

new_variable: int = 15

if __name__ == '__main__':
    print('Код ниже не выполнится, если этот файл будет импортируемым модулем в другой исполняемый файл')
    print(get_double_number(100))
    print(my_dict)
    MyClass()
    print(dir()) #Пространство имен после импортов (способы импортов влияют на пространство имен)
