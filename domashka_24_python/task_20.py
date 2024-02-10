"""
program
"""
import time
from random import randint
import multiprocessing
check1 = time.time()
def file_creator(i):
    """
    program
    """
    with open(f'text{i}.txt','w',encoding='UTF-8') as file:
        file.write(f'{randint(1,10)}')
        time.sleep(1)
for i in range(1,11):
    file_creator(i)
print("Files Created.")
print(f'Time taken to create 10 files: {time.time() - check1} seconds')
check2 = time.time()
for i in range(10,21):
    my_multi = multiprocessing.Process(target=file_creator,args=(i,))
    my_multi.start()
print("Files Created.")
print(f'Time taken to create 10 files: {time.time() - check2} seconds')
#Я не могу понять что за ошибка выходит если оставить только мультипроцессорный запуск 
#так что просто так оставлю
