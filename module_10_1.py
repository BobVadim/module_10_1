from threading import Thread
import time
from _datetime import datetime
from pprint import pprint

time_start = datetime.now()


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(word_count):
            f.write(f'Какое-то слово № {i + 1} \n')
            time.sleep(0.1)
        return print(f'Завершилась запись в файл {file_name}')


wite_words(10, 'file8.txt')
wite_words(30, 'file1.txt')
wite_words(200, 'file2.txt')
wite_words(100, 'file3.txt')

time_stop = datetime.now()
time_result = time_stop - time_start
print(time_result)

time_start_1 = datetime.now()

thr = Thread(target=wite_words, args=(10, 'file4.txt',))
thr_1 = Thread(target=wite_words, args=(30, 'file5.txt',))
thr_2 = Thread(target=wite_words, args=(200, 'file6.txt',))
thr_3 = Thread(target=wite_words, args=(100, 'file7.txt',))

thr_1.start()
thr_2.start()
thr_3.start()
thr.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr.join()

time_stop_1 = datetime.now()
time_result_1 = time_stop_1 - time_start_1
print(time_result_1)
