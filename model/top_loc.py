from read_test_data import find_location, read_drone_data, group_data

def top_loc_signal(data, mac):
    locs = []
    drone_data = read_drone_data()
    time_grouped = group_data(data, 0)

    for time_group in time_grouped:
        score_sorted = sorted(list(time_group[1]), key=lambda x: -int(x[2]))

        i = 0
        loc = None

        try:
            while(loc is None):
                loc = find_location(score_sorted[i][1], drone_data)
                i += 1
        except IndexError:
            print('Couldnt find a location in the AP set')
            continue

        locs.append([mac, time_group[0], loc["x_m"], loc["y_m"], loc["z_m"]])

    return locs

def top_loc_frequency(data, mac):
    locs = []
    drone_data = read_drone_data()
    time_grouped = group_data(data, 0)

    for time_group in time_grouped:
        frequencies = {}

        for row in time_group[1]:
            try:
                frequencies[row[1]][0] += 1
                frequencies[row[1]][1] += 100 + int(row[2])
            except KeyError:
                frequencies[row[1]] = [1, 100 + int(row[2])]

        score_sorted = sorted(frequencies, key=lambda x: (-frequencies[x][0],
                                                          -frequencies[x][1]))

        i = 0
        loc = None

        try:
            while(loc is None):
                loc = find_location(score_sorted[i], drone_data)
                i += 1
        except IndexError:
            print('Couldnt find a location in the AP set')
            continue

        locs.append([mac, time_group[0], loc["x_m"], loc["y_m"], loc["z_m"]])

    return locs

def top_loc_signal_sum(data, mac):
    locs = []
    drone_data = read_drone_data()
    time_grouped = group_data(data, 0)

    for time_group in time_grouped:
        sums = {}

        for row in time_group[1]:
            try:
                sums[row[1]] += 100 + int(row[2])
            except KeyError:
                sums[row[1]] = 100 + int(row[2])

        score_sorted = sorted(sums, key=lambda x: -sums[x])

        i = 0
        loc = None

        try:
            while(loc is None):
                loc = find_location(score_sorted[i], drone_data)
                i += 1
        except IndexError:
            print('Couldnt find a location in the AP set')
            continue

        locs.append([mac, time_group[0], loc["x_m"], loc["y_m"], loc["z_m"]])

    return locs
