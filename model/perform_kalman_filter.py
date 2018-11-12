from kalman_filter import *
from best_base_files import get_files
import csv
import numpy as np


TIME_WINDOWS = [1.5]
ACTUAL_FIRST_POS = (np.array((-35, 70)), 1518086110)
ACTUAL_SECOND_POS = (np.array((35, 70)), 1518086220)

def main():
    pos_diff = ACTUAL_SECOND_POS[0] - ACTUAL_FIRST_POS[0]
    time_diff = ACTUAL_SECOND_POS[1] - ACTUAL_FIRST_POS[1]
    grad = pos_diff / time_diff

    for window in TIME_WINDOWS:
        files = get_files(window)

        for file_name, method, output in files:
            data = []
            times = []
            sourcemac = None

            with open(file_name, 'r') as f:
                reader = csv.DictReader(f, delimiter=';')

                for row in reader:
                    data.append((float(row['x_m']), float(row['y_m'])))
                    times.append(float(row['timestamp']))
                    sourcemac = row['sourcemac']

            act_init_pos = ACTUAL_FIRST_POS[0] + grad * (times[0] - ACTUAL_FIRST_POS[1])
            init_est_error = (np.array(data[0]) - act_init_pos)
            P0 = np.array([[init_est_error[0]**2, 0], [0, init_est_error[1]**2]])

            for q_sigma in range(1, 501):
                for r_sigma in range(21, 31):
                    kalman_filter = KalmanFilter(data[0], P0, times[0], q_sigma, r_sigma)
                    results = kalman_filter.perform_kalman_steps(data[1:], times[1:])

                    with open('/media/nickyz/Data/scriptie_data/results/kalman_filter/' + output + '_{}_{}.csv'.format(q_sigma, r_sigma), 'a') as f:
                        writer = csv.writer(f, delimiter=";")
                        writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])

                        for i, result in enumerate(results):
                            writer.writerow([sourcemac, times[i]] + list(result))

if __name__ == '__main__':
    main()
