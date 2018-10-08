import csv
import datetime
import itertools
import pandas as pd

SECONDS_GROUPING = 60

def group_data(data, sort_index):
    sorted_data = sorted(data, key=lambda x: x[sort_index])

    return itertools.groupby(sorted_data, lambda x: x[sort_index])

def read_drone_data():
    data = pd.read_csv('/media/nickyz/Data/scriptie_data/Huawei_routers_locations_at_Arena/sensors_arena_sensation.csv')

    return data

def find_location(drone_id, drone_data):
    drone = drone_data.loc[drone_data['drone_id'] == drone_id]

    try:
        return drone.iloc[0]
    except IndexError:
        return None

def find_first_last(datafile):
    stamps = []
    with open(datafile) as f:
        reader = csv.DictReader(f)

        for row in reader:
            timestamp = int(row['measurementtimestamp']) // 1000
            stamps.append(timestamp)

    return min(stamps), max(stamps)

def read_data(datafile):
    data = {}
    drone_data = read_drone_data()
    first_stamp, last_stamp = find_first_last(datafile)

    with open(datafile) as f:
        reader = csv.DictReader(f)

        for row in reader:
            row_data = []

            if int(row['signal']) < -80:
                continue

            if find_location(row['sensorid'], drone_data) is None:
                continue

            timestamp = int(row['measurementtimestamp']) // 1000
            index = int((timestamp - first_stamp) / SECONDS_GROUPING)
            stamp = first_stamp + index * SECONDS_GROUPING

            row_data = [stamp, row['sensorid'], int(row['signal'])]

            try:
                data[row['sourcemac']].append(row_data)
            except:
                data[row['sourcemac']] = [row_data]

    return data
