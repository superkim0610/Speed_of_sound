import matplotlib.pyplot as plt

temp = []
speed = []

# with open('2023-09-13_10-10-12_500925.txt', 'r') as f:
# with open('2023-09-13_15-49-20_455190.txt', 'r') as f: # test : 0~7000, 65600~69000
#     for l in f:
#         l = eval(l)
#         temp.append(l['temp'])
#         speed.append(l['speed'])


# with open('2023-09-13_10-10-12_500925.txt', 'r') as f:
with open('2023-09-13_15-49-20_455190.txt', 'r') as f: # test : 0~7000, 65600~69000
    i=0
    for l in f:
        if i % 2==0:
            l = eval(l)
            temp.append(l['temp'])
            speed.append(l['speed'])
        i+=1


def speed_with_temp(range_start=0, range_finish=-1):
    plt.xlabel('temp(degree)')
    plt.ylabel('speed(m/s)')
    plt.scatter(temp[range_start:range_finish], speed[range_start:range_finish], color='r')
    plt.plot([24, 29], [345.4, 348.4], color='b')
    plt.show()


def temp_with_time(range_start=0, range_finish=-1):
    plt.xlabel('time(sec)')
    plt.ylabel('temp(degree)')
    plt.scatter(list(range(1, len(temp)+1))[range_start:range_finish], temp[range_start:range_finish], color='g')
    plt.show()

temp_with_time()
speed_with_temp()