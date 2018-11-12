import numpy as np
import get_performance
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

TIME_WINDOWS = [60]

def main():
    param_values1 = [float(i) for i in range(31, 51)]
    param_values2 = [float(i) for i in range(40001, 50001)]
    file_name = '/media/nickyz/Data/scriptie_data/results/dbl_irr_exp_filter/grid/sum/results_grid_normal_signal_sum_{}_{}_{}.csv'

    print('{')
    for window in TIME_WINDOWS:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, projection='3d')
        results = []
        min_val = 10000000
        min_tup = None
        for i, param_value1 in enumerate(param_values1):
            for param_value2 in param_values2:
                new_val = get_performance.main(file_name.format(window, param_value1, param_value2), 'euc')[0]
                if new_val < min_val:
                    min_val = new_val
                    min_tup = (param_value1, param_value2)
                # try:
                #     results[i].append(
                #         get_performance.main(file_name.format(window, param_value1, param_value2), 'euc')[0]
                #     )
                # except IndexError:
                #     results.append([get_performance.main(file_name.format(window, param_value1, param_value2), 'euc')[0]])

        # min_tup = np.unravel_index(np.argmin(results), np.array(results).shape)
        # print('            {}: ({}, {}),'.format(window, param_values1[min_tup[0]], param_values2[min_tup[1]]))
        print('            {}: ({}, {}),'.format(window, min_tup[0], min_tup[1]))
        print(min_val)
    print('        }')

        # ax.set_xlabel('alpha')
        # ax.set_ylabel('beta')
        # X, Y = np.meshgrid(param_values, param_values)
        # ax.plot_wireframe(X, Y, results, rstride=1, cstride=1)
        # plt.show()

        # plt.plot(param_values, results)
        # plt.xlabel('Gamma')
        # plt.ylabel('Average Euclidean Distance')
        # plt.title('Parameter plot to determine the gamma for the trilateration method\n and a time window of {}'.format(window))
        # plt.show()

if __name__ == '__main__':
    main()
