"""
program
"""
import time
import threading
check1 = time.time()
def file_creator(i):
    """
    program
    """
    with open(f'file{i+1}.txt', 'w',encoding='UTF-8') as file:
        file.write('This is a file created by a Python script.')
        time.sleep(1)
for i in range(10):
    file_creator(i)
print("Files Created.")
print(f'Time taken to create 10 files: {time.time() - check1} seconds')
check2 = time.time()
for i in range(10):
    my_thread = threading.Thread(target=file_creator, args=(i,))
    my_thread.start()
print("Files Created.")
print(f'Time taken to create 10 files: {time.time() - check2} seconds')
