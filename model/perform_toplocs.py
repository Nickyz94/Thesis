from top_loc import top_loc_signal, top_loc_frequency, top_loc_signal_sum
import csv
from read_test_data import read_data, SECONDS_GROUPING

DEF_FILE_NAME = '/media/nickyz/Data/scriptie_data/calibration/calibration_data_20180126.csv'
PI_MAC = '38f3bac0f9e453211a65d468359ded4a56669add0be69079924e901f0b41d4f6'

methods = [
    (top_loc_signal, "signal"),
    (top_loc_frequency, "frequency"),
    (top_loc_signal_sum, "signal_sum")
]

def main(datafile=DEF_FILE_NAME):
    data = read_data(datafile)

    for method in methods:
        with open("../results/results_top_loc_{}_{}.csv".format(method[1], SECONDS_GROUPING),
                  "a") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["sourcemac", "timestamp", "x_m", "y_m", "z_m"])

            results = method[0](data[PI_MAC], PI_MAC)

            for row in results:
                writer.writerow(row)

if __name__ == '__main__':
    main()
