import numpy as np
import get_performance
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

TIME_WINDOW = 1.5

def main():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    param_values1 = list(range(1, 401))
    param_values2 = list(range(1, 31))
    file_name = '/media/nickyz/Data/scriptie_data/results/kalman_filter/trilateration/results_trilateration_{}_{}_{}.csv'
    results = []

    for i, param_value1 in enumerate(param_values1):
        for param_value2 in param_values2:
            try:
                results[i].append(
                    get_performance.main(file_name.format(TIME_WINDOW, param_value1, param_value2), 'euc')[0]
                )
            except IndexError:
                results.append([get_performance.main(file_name.format(TIME_WINDOW, param_value1, param_value2), 'euc')[0]])

    min_tup = np.unravel_index(np.argmin(results), np.array(results).shape)
    print(np.min(results), np.max(results), param_values1[min_tup[0]], param_values2[min_tup[1]])

    # ax.set_xlabel('R')
    # ax.set_ylabel('Q')
    # ax.set_zlabel('Average Euclidean Error')
    # ax.set_title('The parameter plot for estimating the optimal Q and R value for\nthe Kalman filter.\n' +
    #              'Applied to the Proximity Sensing Frequency results with a time window of {}'.format(TIME_WINDOW))
    # X, Y = np.meshgrid(param_values2, param_values1)
    # ax.plot_wireframe(X, Y, results, rstride=1, cstride=1)
    # plt.show()

    # plt.plot(param_values, results)
    # plt.xlabel('Gamma')
    # plt.ylabel('Average Euclidean Distance')
    # plt.title('Parameter plot to determine the gamma for the trilateration method\n and a time window of {}'.format(TIME_WINDOW))
    # plt.show()

if __name__ == '__main__':
    main()
