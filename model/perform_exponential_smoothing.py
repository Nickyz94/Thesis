from exponential_smoothing import *
from best_base_files import get_files
import csv
import numpy as np


TIME_WINDOWS = [120]

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

            # for i in range(0, 101):
            #     alpha = i / 100
            #
            #     exp_filter = Exp_mv_avg(alpha)
            #     results = exp_filter.get_series(data)
            #
            #     with open('../results/exp_filter/' + output + '_{}.csv'.format(alpha), 'a') as f:
            #         writer = csv.writer(f, delimiter=";")
            #         writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])
            #
            #         for j, result in enumerate(results):
            #             writer.writerow([sourcemac, times[j]] + list(result))

            # for i in range(1001, 1501):
            #     tau = i / 10
            #
            #     exp_filter = Irr_exp_mv_avg(tau)
            #     results = exp_filter.get_series(list(zip(times, data)))
            #
            #     with open('../results/irr_exp_filter/' + output + '_{}.csv'.format(tau), 'a') as f:
            #         writer = csv.writer(f, delimiter=";")
            #         writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])
            #
            #         for j, result in enumerate(results):
            #             writer.writerow([sourcemac, times[j]] + list(result))

            # for i in range(0, 101, 5):
            #     alpha = i / 100
            #     for j in range(0, 101, 5):
            #         beta = j / 100
            #
            #         exp_filter = Double_exp_smoothing(alpha, beta)
            #         results = exp_filter.get_series(data)
            #
            #         with open('../results/dbl_exp_filter/' + output + '_{}_{}.csv'.format(alpha, beta), 'a') as f:
            #             writer = csv.writer(f, delimiter=";")
            #             writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])
            #
            #             for k, result in enumerate(results):
            #                 writer.writerow([sourcemac, times[k]] + list(result))

            for i in range(31, 51):
                tau_a = float(i)

                for j in range(1, 31):
                    tau_b = float(j)

                    exp_filter = Irr_double_exp_smoothing(tau_a, tau_b)
                    results = exp_filter.get_series(list(zip(times, data)))

                    with open('/media/nickyz/Data/scriptie_data/results/dbl_irr_exp_filter/' + output + '_{}_{}.csv'.format(tau_a, tau_b), 'a') as f:
                        writer = csv.writer(f, delimiter=";")
                        writer.writerow(["sourcemac", "timestamp", "x_m", "y_m"])

                        for k, result in enumerate(results):
                            writer.writerow([sourcemac, times[k]] + list(result))

if __name__ == '__main__':
    main()
