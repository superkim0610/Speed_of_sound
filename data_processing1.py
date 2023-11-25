# data_dict = {'time': [], 'temp': [], 'speed': []}

# with open('2023-09-13_15-49-20_455190.txt', 'r') as f:
#     t = 1
#     for l in f:
#         _d = eval(l)
#         data_dict['time'].append(t)
#         for key in _d.keys():
#             data_dict[key].append(_d[key])

#         t += 1

# save at new csv file
# find and erase ourbounding data (filter, with same mechanism)
# slice parts
# data process at each parts




# import matplotlib.pyplot as plt

# temp = []
# speed = []


# with open('2023-09-13_15-49-20_455190.txt', 'r') as f:
#     i=0
#     for l in f:
#         if i % 2==0:
#             l = eval(l)
#             temp.append(l['temp'])
#             speed.append(l['speed'])
#         i+=1

# def temp_with_time(range_start=0, range_finish=-1):
#     plt.xlabel('time(sec)')
#     plt.ylabel('temp(degree)')
#     plt.scatter(list(range(1, len(temp)+1))[range_start:range_finish], temp[range_start:range_finish], color='g')
#     plt.show()

# temp_with_time()
# speed_with_temp()


import matplotlib.pyplot as plt

def read_data(file_path):
    temp = []
    speed = []

    with open(file_path, 'r') as f:
        i = 0
        for line in f:
            if i % 2 == 0:
                data = eval(line)
                temp.append(data['temp'])
                speed.append(data['speed'])
            i += 1

    return temp, speed

def plot_temperature_with_time(temp, range_start=0, range_finish=-1):
    plt.xlabel('Time (sec)')
    plt.ylabel('Temperature (degrees)')
    plt.scatter(list(range(1, len(temp) + 1))[range_start:range_finish], temp[range_start:range_finish], color='g')
    
    # x = 32854에 평행한 선 추가함
    plt.axvline(x=32854, color='b', linestyle='--', label='x = 32854')
    
    plt.title('Temperature over Time')
    plt.grid(True)
    plt.legend()
    plt.show()


# 파일 
file_path = '2023-09-13_15-49-20_455190.txt'

# 데이터 확인함
temperature, speed = read_data(file_path)

# 온도와 속도를 각각 그래프로 표시함
plot_temperature_with_time(temperature)
plot_speed_with_time(speed)
