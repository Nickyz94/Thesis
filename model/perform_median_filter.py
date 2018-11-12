from median_filter import *
from best_base_files import get_files
import csv
import numpy as np

TIME_WINDOWS = [1.5, 5, 15, 30, 60, 120]

SIGMA_EST_WINDOWS = {
    'Frequency Proximity Sensing': {
        1.5: 25,
        5: 22,
        15: 6,
        30: 3,
        60: 1,
        120: 2
    },
    'Signal Proximity Sensing': {
        1.5: 26,
        5: 21,
        15: 4,
        30: 3,
        60: 1,
        120: 2
    },
    'Signal Sum Proximity Sensing': {
        1.5: 25,
        5: 22,
        15: 6,
        30: 3,
        60: 4,
        120: 2
    },
    'Frequency Top-Loc Grid': {
        1.5: 25,
        5: 22,
        15: 6,
        30: 3,
        60: 1,
        120: 2
    },
    'Signal Top-Loc Grid': {
        1.5: 26,
        5: 21,
        15: 5,
        30: 10,
        60: 5,
        120: 2
    },
    'Signal Sum Top-Loc Grid': {
        1.5: 25,
        5: 22,
        15: 6,
        30: 3,
        60: 1,
        120: 2
    },
    'Normal Hadamard Frequency': {
        1.5: 26,
        5: 19,
        15: 7,
        30: 3,
        60: 0,
        120: 0
    },
    'Normal Hadamard Signal': {
        1.5: 27,
        5: 21,
        15: 5,
        30: 2,
        60: 0,
        120: 0
    },
    'Normal Hadamard Signal Sum': {
        1.5: 26,
        5: 22,
        15: 7,
        30: 3,
        60: 0,
        120: 0
    },
    'Normal Sum Frequency': {
        1.5: 27,
        5: 19,
        15: 7,
        30: 3,
        60: 0,
        120: 0
    },
    'Normal Sum Signal': {
        1.5: 25,
        5: 22,
        15: 5,
        30: 1,
        60: 5,
        120: 3
    },
    'Normal Sum Signal Sum': {
        1.5: 26,
        5: 23,
        15: 2,
        30: 3,
        60: 0,
        120: 0
    },
    'Trilateration': {
        1.5: 14,
        5: 10,
        15: 5,
        30: 2,
        60: 3,
        120: 0
    }
}

WINDOW_EST_SIGMA = {
    'Frequency Proximity Sensing': {
        1.5: 210,
        5: 251,
        15: 116,
        30: 95,
        60: 51,
        120: 204
    },
    'Signal Proximity Sensing': {
        1.5: 219,
        5: 205,
        15: 51,
        30: 84,
        60: 51,
        120: 204
    },
    'Signal Sum Proximity Sensing': {
        1.5: 210,
        5: 251,
        15: 116,
        30: 84,
        60: 34,
        120: 204
    },
    'Frequency Top-Loc Grid': {
        1.5: 148,
        5: 213,
        15: 121,
        30: 84,
        60: 51,
        120: 204
    },
    'Signal Top-Loc Grid': {
        1.5: 176,
        5: 205,
        15: 83,
        30: 44,
        60: 86,
        120: 204
    },
    'Signal Sum Top-Loc Grid': {
        1.5: 148,
        5: 213,
        15: 121,
        30: 84,
        60: 51,
        120: 204
    },
    'Normal Hadamard Frequency': {
        1.5: 71,
        5: 212,
        15: 128,
        30: 95,
        60: 1,
        120: 1
    },
    'Normal Hadamard Signal': {
        1.5: 134,
        5: 200,
        15: 83,
        30: 51,
        60: 1,
        120: 1
    },
    'Normal Hadamard Signal Sum': {
        1.5: 222,
        5: 191,
        15: 128,
        30: 95,
        60: 1,
        120: 1
    },
    'Normal Sum Frequency': {
        1.5: 66,
        5: 212,
        15: 128,
        30: 95,
        60: 1,
        120: 1
    },
    'Normal Sum Signal': {
        1.5: 215,
        5: 213,
        15: 88,
        30: 26,
        60: 86,
        120: 204
    },
    'Normal Sum Signal Sum': {
        1.5: 222,
        5: 179,
        15: 26,
        30: 95,
        60: 1,
        120: 1
    },
    'Trilateration': {
        1.5: 134,
        5: 69,
        15: 91,
        30: 51,
        60: 189,
        120: 1
    }
}

def main():
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

            # for data_window in range(0, 41):
            #     med_filter = Median_filter(data_window)
            #     results = med_filter.get_series(data)
            #
            #     with open('../results/med_filter/' + output + '_{}.csv'.format(data_window), 'a') as f:
            #         writer = csv.writer(f, delimiter=";")
            #         writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])
            #
            #         for j, result in enumerate(results):
            #             writer.writerow([sourcemac, times[j]] + list(result))
            #
            # for data_window in range(0, 41):
            #     med_filter = Shifting_median_filter(data_window)
            #     results = med_filter.get_series(list(zip(times, data)))
            #
            #     with open('../results/shift_med_filter/' + output + '_{}.csv'.format(data_window), 'a') as f:
            #         writer = csv.writer(f, delimiter=";")
            #         writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])
            #
            #         for j, result in enumerate(results):
            #             writer.writerow([sourcemac, times[j]] + list(result))

            # data_window = SIGMA_EST_WINDOWS[method][window]
            # for sigma in range(251, 301):
            #     med_filter = Gaussian_median_filter(data_window, sigma)
            #     results = med_filter.get_series(list(zip(times, data)))
            #
            #     with open('../results/gauss_med_filter/sigma_est/' + output + '_{}.csv'.format(sigma), 'a') as f:
            #         writer = csv.writer(f, delimiter=";")
            #         writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])
            #
            #         for j, result in enumerate(results):
            #             writer.writerow([sourcemac, times[j]] + list(result))

            sigma = WINDOW_EST_SIGMA[method][window]
            for data_window in range(0, 41):
                    med_filter = Gaussian_median_filter(data_window, sigma)
                    results = med_filter.get_series(list(zip(times, data)))

                    with open('../results/gauss_med_filter/' + output + '_{}.csv'.format(data_window), 'a') as f:
                        writer = csv.writer(f, delimiter=";")
                        writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])

                        for j, result in enumerate(results):
                            writer.writerow([sourcemac, times[j]] + list(result))

if __name__ == '__main__':
    main()
