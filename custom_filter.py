#Реализуйте функцию custom_filter(), которая на вход принимает список some_list, с любыми типами данных,
#'находит в этом списке целые числа, отбирает из них те, что делятся нацело на 7,
#суммирует их, а затем проверяет превышает эта сумма 83 или нет.
#Если НЕ превышает - функция должна вернуть True, если превышает - False.

# some_list = [7, 14, 28, 32, 32, 56]
some_list = [7, 14, 28, 32, 32, '56']

# def custom_filter(lst: list) -> bool:
#     new_list = [x for x in some_list if isinstance(x, int) and not x % 7]
#     if sum(new_list) <= 83:
#         return True
#     else:
#         return False

# print(custom_filter(some_list))

# def custom_filter(lst: list) -> bool:
#     return sum(filter(lambda x: isinstance(x, int) and not x % 7, some_list)) <= 83
#
# print(custom_filter(some_list))


#Напишите функцию anonymous_filter, используя синтаксис анонимных функций,
# которая принимает строковый аргумент и возвращает значение True,
# если количество русских букв я не меньше 23 (регистр буквы неважен) и False в противном случае.


def anonymous_filter(s: str) -> bool:
    return (lambda x: x.lower().count('я') >= 23)(s)

print(anonymous_filter('Я - последняя буква в алфавите!'))

print(anonymous_filter('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))
