# декоратор который считает времня выполнения функции
# генератор бесконечной последовательности

import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return wrapper

@timer
def hello():
    time.sleep(2)
    print("/")

hello()

def inf():
    n = 1
    while True:
        yield n
        n += 1

for i in inf():
    print(i)
    if i == 10:
        break





