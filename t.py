# with open('result.txt', 'r') as f:
#     print(len(f.readlines()))
import time

def progress_bar(a, size):
    print('\r' + '■'*a + '_'*(size-a), end='')

for i in range(11):
    progress_bar(i*2, 20)
    time.sleep(0.5)