# Задача 1.
# Необходимо написать программу на Python версии 3.4 или выше.

# Программа должна со стандартного входного потока (с консоли) считывать текст и подсчитывать символы 
# a, b, c - латинские, в нижнем регистре.
# Необходимо через каждые прочитанные 1000 символов, 
# выводить статистику по количеству встретившихся в тексте символов a, b, c. 

# Статистику каждый раз выводить для всего прочитанного текста
#  (а не только с последних прочитанных 1000 символов). 
#  По завершении входных данных, необходимо также выводить статистику по тем же символам со всего текста.
# Статистику выводить в стандартный выходной поток (на консоль).

# Вывод статистики должен быть в следующем формате:
# a: x, b: y, c: z
# где
# x - количество встретившихся символов a
# y - количество встретившихся символов b
# z - количество встретившихся символов c
# - символ переноса строки, т.е. каждый вывод статистики на отдельной строке
# Пример:
# При запуске программы вводим с консоли текст:
# > abcdefghijklmnop
# > a: 1, b: 1, c: 1
# > aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac
# a: 995, b: 4, c: 1
from collections import OrderedDict

# ===================================================== набор функций для получения исходной строки

def get_str_setted_for_dev1()->str:
    "Строка на время разработки == чтобы не вводить"
    return 'abcdefghijklmnop'

def get_str_setted_for_dev2()->str:
    "Строка на время разработки == чтобы не вводить"
    return 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac'

def get_str_from_input()->str:
    "Получаем строку из через встроенную функцию input"
    return str(input())

import sys
def get_str_from_argv()->str:
    "Получаем строку через параметр командной строки при вызове скрипта"
    _res=str(sys.argv[1]) if len(sys.argv)>1 else ""
    return _res

# ===================================================== набор функций для получения исходной строки


def calc_char_precense(s:str, calcchars:tuple)->OrderedDict:
    "Подсчитываем количество символов(calcchars) в строке(s)"
    #формируем словарь упоминаний букв: ключ:str==буква, значение:int==количество упоминаний, по умолч==0
    _res=OrderedDict(map(lambda a: tuple([a,0]), calcchars))
    if not s: return _res #если строка пустая вовзращаем словарь с нулевыми вхождениями

    for c in s:
        if c in _res.keys():
            _res[c] += 1
    return _res

def get_calcs_dict(calcchars:object, f:object=get_str_setted_for_dev1, show_source=True, show_res=True)->OrderedDict:
    "подсчёт символов(calcchars) в строке(s) через функцию(f)"

    def print_res_as_str(d:OrderedDict):
        "Вспомогательная функция для вывода результата в человекочитаемом виде с сортировкой по calcchars"
        _s=""
        for k,v in d.items():
            _s += f"{k}: {v}, "
        else: # удаляем последнюю запятую и пробел.. для красоты и полного соответствия требованиям ТЗ
            _s = _s[:-2]

        print(_s)


    if isinstance(calcchars, str):
        # https://stackoverflow.com/questions/9841303/removing-duplicate-characters-from-a-string
        # calcchars = "".join(set(calcchars)) 
        calcchars = ''.join(sorted(set(calcchars), key=calcchars.index))
        #удаляем дубли символов(если есть) == последователность имеет значение

        calcchars = tuple(calcchars)


    if not isinstance(calcchars, tuple):
        raise ValueError(f"Параметр 'calcchars' задан неверно! \
            Ожидается 'tuple' или 'str' а пришло {type(calcchars)} со значением {repr(calcchars)}")

    if not isinstance(f, str) and not callable(f):
        raise ValueError(f"Параметр 'f' задан неверно! \
            Ожидается 'function' или 'str' а пришло {type(f)} со значением {repr(f)}")


    if callable(f): # если f указывает на функцию
        s=f() # получаем строку из функции указанной в параметрах вызова функции
    elif isinstance(f, str): # если вместо функции пришла строка - выполняем с ней
        s=f


    _res=calc_char_precense(s, calcchars)

    if show_source: print(s)
    if show_res: print_res_as_str(_res)

    return _res


if __name__ == '__main__':
    # набор символов(в виде строки) которые нужно подсчитать, 
    counting_chars_str:str = 'abc'
    # counting_chars_str:str = 'abca'
    # counting_chars_str:str = 'bca'
    # можно вводить повторяющиеся == они автоматически схлопнутся


    get_calcs_dict(counting_chars_str)

    get_calcs_dict(counting_chars_str, get_str_setted_for_dev2)

    print(f"Введите строку для подсчета количества символов из набора: '{counting_chars_str}'")
    get_calcs_dict(counting_chars_str, get_str_from_input, show_source=False)
