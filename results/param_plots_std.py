import numpy as np
import get_performance
import matplotlib.pyplot as plt

TIME_WINDOW = 30

def main():
    param_values = range(1, 36)

    file_names = [
        ('grid/std_estimation/results_grid_normal_signal_{}_{}.csv', 'Signal'),
        # ('grid/std_estimation/results_grid_normal_frequency_{}_{}.csv', 'Frequency'),
        # ('grid/std_estimation/results_grid_normal_signal_sum_{}_{}.csv', 'Signal Sum'),
    ]

    results = [[] for _ in file_names]

    for param_value in param_values:
        for i, file_name in enumerate(file_names):
            results[i].append(
                get_performance.main(file_name[0].format(TIME_WINDOW, param_value), 'euc')
            )

    for i, file_name in enumerate(file_names):
        plt.plot(param_values, results[i])
        plt.xlabel('Variance')
        plt.ylabel('Average Euclidean Distance')
        plt.title('Parameter plot to determine the standard deviation using the {}\n normal grid method and a time window of {}'.format(file_name[1], TIME_WINDOW))
        plt.show()

if __name__ == '__main__':
    main()
