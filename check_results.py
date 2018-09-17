from model.read_test_data import *
import matplotlib.pyplot as plt
from results.get_performance import create_ground_truth

PI_MAC = '38f3bac0f9e453211a65d468359ded4a56669add0be69079924e901f0b41d4f6'

def drone_loc(sensor_id, drone_data):
    loc = find_location(sensor_id, drone_data)
    return (loc['x_m'], loc['y_m'])

def with_aps():
    data = read_data('/media/nickyz/Data/scriptie_data/calibration/calibration_data_20180126.csv')
    drone_data = read_drone_data().dropna(axis=0)

    drone_locs = {sensor_id: drone_loc(sensor_id, drone_data) for sensor_id in drone_data['drone_id']}

    results = {}

    with open('results/results_trilateration.csv', 'r') as f:
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
        # plt.savefig('tri_plots/{}.png'.format(group[0]))
        # plt.close()
        plt.show()

def path():
    with open('results/results_top_loc_frequency_15.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        x_results = []
        y_results = []

        for row in reader:
            if row['sourcemac'] == PI_MAC:
                x_results.append(row['x_m'])
                y_results.append(row['y_m'])

        # for row in create_ground_truth():
        #     x_results.append(row[1][0])
        #     y_results.append(row[1][1])

        # plt.gca().invert_yaxis()
        plt.plot(x_results, y_results, '-')
        plt.show()

if __name__ == '__main__':
    path()
