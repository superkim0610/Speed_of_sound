import matplotlib.pyplot as plt


def progress_bar(a, size):
    print('\r' + '■'*a + '_'*(size-a), end='')


def temp_err_finder(temp_list):
    avg = sum(temp_list)/len(temp_list)
    for temp in temp_list:
        if abs(temp - avg) >= temp_err_range:
            temp_list.remove(temp)

    return sum(temp_list)/len(temp_list)


temp_err_range = 1.0
data = []
distance = 120


with open('result.txt', 'r') as file:
    file = file.readlines()
    line_num = len(file)
    for i, f in enumerate(file):
        if f.startswith('{'):
            _data = eval(f)
            _data['temp'] = temp_err_finder(_data['temp'])
            _data['ultrasonic'] = distance/_data['ultrasonic'] * 10**4
            i+=1
            data.append(_data)
        progress_bar(int((i+1)/line_num * 20), 20)


# temp_list = list(map(lambda x: x['temp'], data))
# ultrasonic_list = list(map(lambda x: x['ultrasonic'], data))
# plt.xlabel('temp')
# plt.ylabel('velocity')
# plt.scatter(temp_list, ultrasonic_list)
# plt.show()


plt.xlabel('time(sec)')
plt.ylabel('temp(degree)')
plt.scatter(list(range(1, len(data)+1)), list(map(lambda x: x['temp'], data)))
plt.show()