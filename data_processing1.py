data_dict = {'time': [], 'temp': [], 'speed': []}

with open('2023-09-13_15-49-20_455190.txt', 'r') as f:
    t = 1
    for l in f:
        _d = eval(l)
        data_dict['time'].append(t)
        for key in _d.keys():
            data_dict[key].append(_d[key])

        t += 1

# save at new csv file

# find and erase ourbounding data (filter, with same mechanism)

# slice parts

# data process at each parts