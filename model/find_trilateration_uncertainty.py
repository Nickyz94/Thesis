from trilateration import Trilateration
from perform_trilateration import count_unique_aps
from read_test_data import group_data, read_data, read_drone_data
import matplotlib.pyplot as plt
import scipy.optimize as opt
import copy

# Outcome 1.58794195

DEF_FILE_NAME = '/media/nickyz/Data/scriptie_data/calibration/calibration_data_20180126.csv'
PI_MAC = '38f3bac0f9e453211a65d468359ded4a56669add0be69079924e901f0b41d4f6'

def _loss(sigma, time_grouped, drone_locs):
    time_groups = copy.deepcopy(time_grouped)
    trilateration = Trilateration(sigma)
    all_groups = []

    for time_group in time_groups:
        sensors = []
        for sensor in time_group[1]:
            try:
                loc = drone_locs[sensor[1]]
            except KeyError:
                continue

            sensors.append({'x': loc[0],
                            'y': loc[1],
                            'z': loc[2],
                            'signal': int(sensor[2])})

        all_groups.append(sensors)

    largest_ndof = max(all_groups, key=lambda x: count_unique_aps(x))

    est = trilateration.get_location(largest_ndof)

    return (est.fun / (len(largest_ndof) - 4))

def main(datafile=DEF_FILE_NAME):
    data = read_data(datafile)
    drone_data = read_drone_data()
    drone_locs = {}

    for index, row in drone_data.iterrows():
        drone_locs[row["drone_id"]] = [float(row["x_m"]), float(row["y_m"]), float(row["z_m"])]

    time_grouped = group_data(data[PI_MAC], 0)

    results = []
    for i in range(1, 101):
        results.append(_loss(i, time_grouped, drone_locs))

    plt.plot(list(range(1, 101)), results)

    for i in zip(list(range(1, 101)), results):
        print(i)

    plt.show()

if __name__ == '__main__':
    main()
