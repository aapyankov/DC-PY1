import string
import random

def get_random_password(n=8) -> str:
    all_char =string.digits + string.ascii_letters
    password = ''.join(random.sample((all_char, n)))
    return password


print(get_random_password())

#Traceback (most recent call last):
#File "C:\Users\redac\PycharmProjects\Course Python английский\Тема 5\Лабораторная работа\task5\main.py", line 9, in <module>
#   print(get_random_password())
#File "C:\Users\redac\PycharmProjects\Course Python английский\Тема 5\Лабораторная работа\task5\main.py", line 6, in get_random_password
#   return ''.join(random.sample((all_char, n)))
#TypeError: Random.sample() missing 1 required positional argument: 'k'

#Process finished with exit code 1
