from grid import top_loc_grid_signal, top_loc_grid_signal_sum, top_loc_grid_freq, normal_grid_method, normal_hadamard_grid_method
import csv
from read_test_data import read_data, SECONDS_GROUPING

DEF_FILE_NAME = '/media/nickyz/Data/scriptie_data/calibration/calibration_data_20180208.csv'
PI_MAC = '437aab3f88a56f32a428df1fc6b2c140bebd28cdf7601a767854c5b41e8d52c5'

methods = [
    (top_loc_grid_signal, "signal"),
    (top_loc_grid_signal_sum, "signal_sum"),
    (top_loc_grid_freq, "freq")
]

stds = {
    1.5: (6, 9, 2),
    5: (16, 22, 16),
    15: (25, 16, 2),
    30: (9, 8, 16)
}

def main(datafile=DEF_FILE_NAME):
    data = read_data(datafile)
    size = 16

    # for method in methods:
    #     with open("../results/grid/top_loc/results_grid_{}_{}.csv".format(method[1], SECONDS_GROUPING),
    #               "a") as f:
    #         writer = csv.writer(f, delimiter=";")
    #         writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])
    #
    #         results = method[0](data[PI_MAC], PI_MAC, size)
    #
    #         for row in results:
    #             writer.writerow(row)

    for i in range(0, 101):
        alpha = i / 100
    # for std in range(1, 36, 1):
    #     with open("../results/grid/alpha_estimation_signal_sum/results_grid_normal_signal_sum_{}_{}.csv".format(SECONDS_GROUPING, alpha),
    #               "a") as f:
    #         writer = csv.writer(f, delimiter=";")
    #         writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])
    #
    #         results = normal_grid_method(data[PI_MAC], PI_MAC, stds[SECONDS_GROUPING][0], size, 'signal_sum', alpha=alpha)
    #
    #         for row in results:
    #             writer.writerow(row)
    #
        # with open("../results/grid/alpha_estimation_frequency/results_grid_normal_frequency_{}_{}.csv".format(SECONDS_GROUPING, alpha),
        #           "a") as f:
        #     writer = csv.writer(f, delimiter=";")
        #     writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])
        #
        #     results = normal_grid_method(data[PI_MAC], PI_MAC, stds[SECONDS_GROUPING][1], size, 'freq', alpha=alpha)
        #
        #     for row in results:
        #         writer.writerow(row)
        with open("../results/grid/alpha_estimation_signal/results_grid_normal_signal_{}_{}.csv".format(SECONDS_GROUPING, alpha),
                  "a") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])

            results = normal_grid_method(data[PI_MAC], PI_MAC, stds[SECONDS_GROUPING][2], size, 'signal', alpha=alpha)

            for row in results:
                writer.writerow(row)

    # for std in range(1, 36, 1):
        # with open("../results/grid/std_estimation_hadamard/results_grid_hadamard_normal_sum_{}_{}.csv".format(SECONDS_GROUPING, std),
        #           "a") as f:
        #     writer = csv.writer(f, delimiter=";")
        #     writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])
        #
        #     results = normal_hadamard_grid_method(data[PI_MAC], PI_MAC, std, size, 'signal_sum')
        #
        #     for row in results:
        #         writer.writerow(row)
        #
        # with open("../results/grid/std_estimation_hadamard/results_grid_hadamard_normal_freq_{}_{}.csv".format(SECONDS_GROUPING, std),
        #           "a") as f:
        #     writer = csv.writer(f, delimiter=";")
        #     writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])
        #
        #     results = normal_hadamard_grid_method(data[PI_MAC], PI_MAC, std, size, 'freq')
        #
        #     for row in results:
        #         writer.writerow(row)

        # with open("../results/grid/std_estimation_hadamard/results_grid_hadamard_normal_signal_{}_{}.csv".format(SECONDS_GROUPING, std),
        #           "a") as f:
        #     writer = csv.writer(f, delimiter=";")
        #     writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])
        #
        #     results = normal_hadamard_grid_method(data[PI_MAC], PI_MAC, std, size, 'signal')
        #
        #     for row in results:
        #         writer.writerow(row)

if __name__ == '__main__':
    main()
