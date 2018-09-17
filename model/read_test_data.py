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

def read_data(datafile):
    data = {}
    with open(datafile) as f:
        reader = csv.DictReader(f)

        for row in reader:
            row_data = []

            timestamp = row['measurementtimestamp']
            rounded_stamp = timestamp = round(int(timestamp[0:-3]) / SECONDS_GROUPING) * SECONDS_GROUPING
            timestamp = datetime.datetime.fromtimestamp(rounded_stamp).strftime('%Y-%m-%d %H:%M:%S')

            row_data = [timestamp, row['sensorid'], row['signal']]

            try:
                data[row['sourcemac']].append(row_data)
            except:
                data[row['sourcemac']] = [row_data]

    return data
