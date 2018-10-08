from model.read_test_data import *
import matplotlib.pyplot as plt
from results.get_performance import create_ground_truth

PI_MAC = '437aab3f88a56f32a428df1fc6b2c140bebd28cdf7601a767854c5b41e8d52c5'

def drone_loc(sensor_id, drone_data):
    loc = find_location(sensor_id, drone_data)
    return (loc['x_m'], loc['y_m'])

def with_aps():
    data = read_data('/media/nickyz/Data/scriptie_data/calibration/calibration_data_20180126.csv')
    drone_data = read_drone_data().dropna(axis=0)

    drone_locs = {sensor_id: drone_loc(sensor_id, drone_data) for sensor_id in drone_data['drone_id']}

    results = {}

    with open('results/grid/std_estimation_hadamard/results_grid_hadamard_normal_freq_30_9.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=';')

        for row in reader:
            if row['sourcemac'] == PI_MAC:
                results[row['timestamp']] = (row['x_m'], row['y_m'])

    grouped_data = group_data(data[PI_MAC], 0)

    for group in grouped_data:
        try:
            result = results[group[0]]
        except KeyError:
            continue

        for sensor in group[1]:
            try:
                loc = drone_locs[sensor[1]]
                plt.scatter(*loc, s=150, alpha=0.3)
            except KeyError:
                continue

        plt.scatter(drone_data['x_m'], drone_data['y_m'])
        plt.scatter(*result, color='r')
        plt.savefig('tri_plots/{}.png'.format(group[0]))
        plt.close()
        # plt.show()

def path():
    with open('results/grid/std_estimation_hadamard/results_grid_hadamard_normal_freq_30_9.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        x_results = []
        y_results = []

        drone_data = read_drone_data().dropna(axis=0)
        drone_locs = {sensor_id: drone_loc(sensor_id, drone_data) for sensor_id in drone_data['drone_id']}

        for row in reader:
            if row['sourcemac'] == PI_MAC:
                x_results.append(row['x_m'])
                y_results.append(row['y_m'])

        # for row in create_ground_truth():
        #     x_results.append(row[1][0])
        #     y_results.append(row[1][1])

        # plt.gca().invert_yaxis()
        plt.scatter(drone_data['x_m'], drone_data['y_m'])
        plt.plot(x_results, y_results, '-', color='r')
        plt.show()

if __name__ == '__main__':
    path()
