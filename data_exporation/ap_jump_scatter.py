import fileinput
import time
import glob
import json
import datetime
import itertools
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_data():
    start = time.time()
    data = {}
    files = glob.glob('/media/nickyz/Data/scriptie_data/armin/20170512_[5].csv')
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

        if localMac:
            continue

        try:
            droneId = values['droneId']
        except KeyError:
            droneId = values['droneid']

        timestamp = splitted[2]
        orig_time = datetime.datetime.fromtimestamp(int(timestamp[0:-3])).strftime('%Y-%m-%d %H:%M:%S')
        timestamp = datetime.datetime.fromtimestamp(int(timestamp[0:-3])).strftime('%Y-%m-%d %H:%M')

        try:
            data[sourceMac].append([timestamp, droneId, signal, orig_time])
        except KeyError:
            data[sourceMac] = [[timestamp, droneId, signal, orig_time]]

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
    measurements = []

    for key in data:
        time_grouped = group_data(data[key], 0)
        max_value = 0
        drone_locs = []
        distances = []

        for time_group in time_grouped:
            values = list(time_group[1])
            counter = 0

            drone_grouped = group_data(values, 1)

            for row in drone_grouped:
                counter += 1

            if counter > max_value:
                max_value = counter

            g_data = [(item[0], item[1], item[2], item[3]) for item in values]
            # print(g_data)
            g_data = sorted(g_data, key=lambda x: -x[2])
            # print(g_data)

            i = 0
            drone_loc = find_location(g_data[i][1], drone_data)
            time_orig = g_data[i][3]
            while drone_loc is None and i < len(g_data) - 1:
                i += 1
                drone_loc = find_location(g_data[i][1], drone_data)
                time_orig = g_data[i][3]

            if drone_loc is None:
                continue

            drone_locs.append([time_orig, drone_loc])

        for i, row in enumerate(drone_locs[1:]):
            cur_row = row[1]
            prev_row = drone_locs[i][1]

            if cur_row is None or prev_row is None:
                print('Oeps')
                continue

            dist = ((prev_row['x_m'] - cur_row['x_m'])**2 + (prev_row['y_m'] - cur_row['y_m'])**2)**0.5
            time = (datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(drone_locs[i][0], "%Y-%m-%d %H:%M:%S")).seconds
            distances.append(dist / time)

        try:
            measurements.append([max_value, max(distances)])
        except ValueError:
            continue

    plt.scatter([row[0] for row in measurements], [row[1] for row in measurements])
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    plt.xlabel("Maximum number of AP's connected to in a minute")
    plt.ylabel("Biggest jump within a minute (m/s)")
    plt.show()

if __name__ == '__main__':
    main()
