import fileinput
import time
import glob
import json
import datetime
import itertools
import pandas as pd
import matplotlib.pyplot as plt

def read_data():
    start = time.time()
    data = {}
    files = glob.glob('/media/nickyz/Data/scriptie_data/armin/20170512_[4-5].csv')
    print(files)
    files.reverse()

    for line in fileinput.input(files=files):
        if fileinput.isfirstline():
            print(time.time() - start)
            print(fileinput.filename())
            start = time.time()
            continue

        splitted = line.split('\t')
        values = json.loads(splitted[0])

        try:
            sourceMac = values['sourceMac']
        except KeyError:
            sourceMac = values['sourcemac']

        try:
            localMac = int(values['localMac'])
        except KeyError:
            localMac = int(values['localmac'])

        signal = int(values['signal'])

        if(localMac):
            continue

        try:
            droneId = values['droneId']
        except KeyError:
            droneId = values['droneid']

        timestamp = splitted[2]
        timestamp = datetime.datetime.fromtimestamp(int(timestamp[0:-3])).strftime('%Y-%m-%d %H:%M:%S')

        try:
            data[sourceMac].append([timestamp, droneId, signal])
        except KeyError:
            data[sourceMac] = [[timestamp, droneId, signal]]

    print(time.time() - start)

    return data

def read_drone_data():
    data = pd.read_csv('/media/nickyz/Data/scriptie_data/Huawei_routers_locations_at_Arena/sensors_arena_sensation.csv')

    return data

def find_location(drone_id, drone_data):
    drone = drone_data.loc[drone_data['drone_id'] == drone_id]

    try:
        return drone.iloc[0]
    except IndexError:
        return None

def group_data(data, sort_index):
    sorted_data = sorted(data, key=lambda x: x[sort_index])

    return itertools.groupby(sorted_data, lambda x: x[sort_index])

def main():
    data = read_data()
    drone_data = read_drone_data()
    hist_data = []
    for person in data.values():
        grouped = group_data(person, 0)
        distances = []
        drone_locs = []

        for group in grouped:
            g_data = [(item[0], item[1], item[2]) for item in group[1]]
            g_data = sorted(g_data, key=lambda x: -x[2])

            i = 0
            drone_loc = find_location(g_data[i][1], drone_data)
            while drone_loc is None and i < len(g_data) - 1:
                i += 1
                drone_loc = find_location(g_data[i][1], drone_data)

            if drone_loc is None:
                continue

            drone_locs.append([group[0], drone_loc])

        for i, row in enumerate(drone_locs[1:]):
            cur_row = row[1]
            prev_row = drone_locs[i][1]

            if cur_row is None or prev_row is None:
                print('Oeps')
                continue

            dist = ((prev_row['x_m'] - cur_row['x_m'])**2 + (prev_row['y_m'] - cur_row['y_m'])**2)**0.5
            time = (datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(drone_locs[i][0], "%Y-%m-%d %H:%M:%S")).seconds
            # print((prev_row['x_m'] - cur_row['x_m'])**2 + (prev_row['y_m'] - cur_row['y_m'])**2, prev_row['x_m'], cur_row['x_m'], prev_row['y_m'], cur_row['y_m'])
            distances.append(dist / time)

        try:
            hist_data.append(max(distances))
        except ValueError:
            continue

    print(len(data), len(hist_data))

    plt.hist(hist_data)
    plt.show()

if __name__ == '__main__':
    main()
