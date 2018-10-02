import numpy as np
import get_performance
import matplotlib.pyplot as plt

TIME_WINDOW = 15

def main():
    param_values = range(0, 101)
    param_values = [param_value / 100 for param_value in param_values]

    file_names = [
        ('grid/alpha_estimation_signal/results_grid_normal_signal_{}_{}.csv', 'Signal'),
        # ('grid/alpha_estimation_frequency/results_grid_normal_frequency_{}_{}.csv', 'Frequency'),
        # ('grid/alpha_estimation_signal_sum/results_grid_normal_signal_sum_{}_{}.csv', 'Signal Sum'),
    ]

    results = [[] for _ in file_names]

    for param_value in param_values:
        for i, file_name in enumerate(file_names):
            results[i].append(
                get_performance.main(file_name[0].format(TIME_WINDOW, param_value), 'euc')
            )

    print(np.argmin(results[0]))

    for i, file_name in enumerate(file_names):
        plt.plot(param_values, results[i])
        plt.xlabel('Alpha')
        plt.ylabel('Average Euclidean Distance')
        plt.title('Parameter plot to determine the alpha value using the {}\n normal grid method and a time window of {}'.format(file_name[1], TIME_WINDOW))
        plt.show()

if __name__ == '__main__':
    main()
