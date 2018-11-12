import numpy as np
import get_performance
import matplotlib.pyplot as plt

TIME_WINDOWS = [1.5, 5, 15, 30, 60, 120]

def main():
    param_values = [i / 10 for i in range(1, 1501)]
    file_name = 'irr_exp_filter/trilateration/results_trilateration_{}_{}.csv'

    print('{')
    for window in TIME_WINDOWS:
        results = []
        params = param_values
        for param_value in param_values:
            try:
                results.append(
                    get_performance.main(file_name.format(window, param_value), 'euc')[0]
                )
            except:
                if window == 60:
                    params = [i / 10 for i in range(1, 501)]
                else:
                    params = [i / 10 for i in range(1, 301)]
                break

        print('            {}: {},'.format(window, param_values[np.argmin(results)]))
    print('        }')

        # plt.plot(params, results)
        # plt.xlabel('Gamma')
        # plt.ylabel('Average Euclidean Distance')
        # plt.title('Parameter plot to determine the gamma for the trilateration method\n and a time window of {}'.format(window))
        # plt.show()

if __name__ == '__main__':
    main()
