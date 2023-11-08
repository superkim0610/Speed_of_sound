new_files = []
temp_err_range = 1.0
distance = 120


def progress_bar(a, size):
    print('\r' + '■'*a + '_'*(size-a), end='')


def temp_err_finder(temp_list):
    avg = sum(temp_list)/len(temp_list)
    for temp in temp_list:
        if abs(temp - avg) >= temp_err_range:
            temp_list.remove(temp)

    return sum(temp_list)/len(temp_list)


# progress_bar(int((i+1)/line_num * 20), 20)

line_num = len(open('result.txt').readlines())

with open('result.txt', 'r') as file:
    for i, l in enumerate(file):
        if l.startswith('>> logging starts at '):
            time = l.replace('>> logging starts at ', '')
            new_files.append({'time': time, 'data': []})
        elif l.startswith('{'):
            l = eval(l)
            temp = temp_err_finder(l['temp'])
            speed = distance / l['ultrasonic'] * 10**4
            new_files[-1]['data'].append({'temp': temp, 'speed': speed})

        progress_bar(int((i+1)/line_num*30), 30)

for new_file in new_files:
    time = new_file['time']
    data = new_file['data']
    with open(f'{time.replace(" ", "_").replace(".", "_").replace(":", "-").strip()}.txt', 'w') as file:
        file.write('\n'.join(map(str, data)))