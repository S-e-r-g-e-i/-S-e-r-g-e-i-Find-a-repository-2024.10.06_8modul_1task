# Домашнее задание по уроку "Try и Except".

def add_everything_up(a, b):
    try:
        return round(a + b, 3)
    except TypeError as t:
        if isinstance(a, str) and (isinstance(b, float) or isinstance(b, int)):
            b = f'{b}' # переводим число в строку
            print(f'значение b переведено в str')
            return a + b
        elif isinstance(b, str) and (isinstance(a, float) or isinstance(a, int)):
            a = f'{a}' # переводим число в строку
            print(f'значение a переведено в str')
            return a + b
    finally:
        print('Задача выполнена :)')


# Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))