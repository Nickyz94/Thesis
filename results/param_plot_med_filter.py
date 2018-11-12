import numpy as np
import get_performance
import matplotlib.pyplot as plt

TIME_WINDOWS = [1.5, 5, 15, 30, 60, 120]
NAME = 'shift_med_filter/top_loc/results_top_loc_signal_sum_{}_{}.csv'

def main():
    param_values = [i for i in range(0, 41)]
    # results = []
    #
    # for param_value in param_values:
    #     results.append(
    #         get_performance.main(NAME.format(TIME_WINDOW, param_value), 'euc')[0]
    #     )
    #
    # # print(param_values[np.argmin(results)])
    #
    #
    # plt.plot(param_values, results)
    # plt.xlabel('Gamma')
    # plt.ylabel('Average Euclidean Distance')
    # plt.title('Parameter plot to determine the gamma for the trilateration method\n and a time window of {}'.format(TIME_WINDOW))
    # plt.show()
    #
    # results = []
    #
    # for param_value in param_values:
    #     results.append(
    #         get_performance.main('shift_' + NAME.format(TIME_WINDOW, param_value), 'euc')[0]
    #     )
    #
    # # print(param_values[np.argmin(results)])
    #
    #
    # plt.plot(param_values, results)
    # plt.xlabel('Gamma')
    # plt.ylabel('Average Euclidean Distance')
    # plt.title('Parameter plot to determine the gamma for the trilateration method\n and a time window of {}'.format(TIME_WINDOW))
    # plt.show()

    print('{')
    for window in TIME_WINDOWS:
        results = []

        for param_value in param_values:
            results.append(
                get_performance.main(NAME.format(window, param_value), 'euc')[0]
            )

        print('            {}: {},'.format(window, param_values[np.argmin(results)]))
    print('        }')

        # plt.plot(param_values, results)
        # plt.xlabel('Gamma')
        # plt.ylabel('Average Euclidean Distance')
        # plt.title('Parameter plot to determine the gamma for the trilateration method\n and a time window of {}'.format(TIME_WINDOW))
        # plt.show()

if __name__ == '__main__':
    main()
