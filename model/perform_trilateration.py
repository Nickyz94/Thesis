from trilateration import Trilateration
from read_test_data import group_data, read_data, read_drone_data, SECONDS_GROUPING
import csv
import numpy as np

DEF_FILE_NAME = '/media/nickyz/Data/scriptie_data/calibration/calibration_data_20180208.csv'
PI_MAC = '437aab3f88a56f32a428df1fc6b2c140bebd28cdf7601a767854c5b41e8d52c5'

def count_unique_aps(ap_ids):
    return len(ap_ids)

def main(datafile=DEF_FILE_NAME):
    data = read_data(datafile)
    drone_data = read_drone_data()
    drone_locs = {}

    for index, row in drone_data.iterrows():
        drone_locs[row["drone_id"]] = [float(row["x_m"]), float(row["y_m"]), float(row["z_m"])]

    time_grouped = group_data(data[PI_MAC], 0)
    sensors_per_time = []

    for time_group in time_grouped:
        ap_ids = []
        sensors = []
        used_sensors = set()
        sorted_data = sorted(time_group[1], key=lambda x: x[2])

        for sensor in sorted_data:
            if(sensor[1] in used_sensors):
                continue
            used_sensors.add(sensor[1])

            try:
                loc = drone_locs[sensor[1]]
            except KeyError:
                continue

            ap_ids.append(sensor[1])

            sensors.append({'x': loc[0],
                            'y': loc[1],
                            'z': loc[2],
                            'signal': int(sensor[2])})

        if count_unique_aps(ap_ids) > 3:
            sensors_per_time.append([time_group[0], sensors])
        else:
            print('JAMMER')

    for param in range(0, 301, 5):
        gamma = param / 100

        with open("../results/trilateration/results_trilateration_{}_{}.csv".format(SECONDS_GROUPING, gamma), "a") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["sourcemac", "timestamp", "x_m", "y_m", "z_m", "eta"])

            trilateration = Trilateration(gamma)

            for row in sensors_per_time:
                est = trilateration.get_location(row[1])
                writer.writerow([PI_MAC, row[0]] + list(est.x))



if __name__ == '__main__':
    main()
