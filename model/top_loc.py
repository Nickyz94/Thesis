from read_test_data import find_location, read_drone_data, group_data

def top_loc_signal(data, mac):
    locs = []
    drone_data = read_drone_data()
    time_grouped = group_data(data, 0)

    for time_group in time_grouped:
        max_score = max(time_group[1], key=lambda x: x[2])
        loc = find_location(max_score[1], drone_data)

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

        max_score = max(frequencies, key=lambda x: (frequencies[x][0],
                                                    frequencies[x][1]))
        loc = find_location(max_score, drone_data)

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

        max_score = max(sums, key=lambda x: sums[x])

        loc = find_location(max_score, drone_data)

        locs.append([mac, time_group[0], loc["x_m"], loc["y_m"], loc["z_m"]])

    return locs
