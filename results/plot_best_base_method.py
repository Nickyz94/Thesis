from best_base_files import get_files
import get_performance
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as mcolors
import seaborn as sns
import pandas as pd

TIME_WINDOWS = [1.5, 5, 15, 30, 60, 120]

def main():
    N = len(TIME_WINDOWS)
    results = []
    labels = ['Euclidean Distance', 'Method', 'Time Window']
    methods = []
    ps = []
    prev_length = 0

    for window in TIME_WINDOWS:
        base_files = get_files(window)
        methods = []

        for i, base_file in enumerate(base_files):
            dists = get_performance.main(base_file[0], 'euc', False)
            methods.append(base_file[2])

            # len_dif =
            # prev_length = len()

            for val in dists:
                results.append([val, base_file[1], window])

        # tri_shortness = len(part_results[0]) - len(part_results[-1])
        #
        # while tri_shortness > 0:
        #     part_results[-1].append(None)
        #     tri_shortness -= 1
        #
        # part_results.append([window for _ in part_results[0]])
        #
        # results += np.array(part_results).T.tolist()

    df = pd.DataFrame.from_records(results, columns=labels)

    g = sns.boxplot(x='Method', y='Euclidean Distance', hue='Time Window', data=df)
    g.set_xticklabels(labels=methods, rotation=30)

    axes = g.axes
    axes.set_ylim(0, 40)
    plt.show()

def get_latex_table():
    results = {}
    for window in TIME_WINDOWS:
        base_files = get_files(window)

        for i, base_file in enumerate(base_files):
            dist, std = get_performance.main(base_file[0], 'euc')

            try:
                results[base_file[1]].append(dist)
            except KeyError:
                results[base_file[1]] = [dist]

    print('', end=" ")

    for window in TIME_WINDOWS:
        print('& ' + str(window), end=" ")

    print('\\\\')
    print('\\hline')

    for key in results:
        print(key, end=" ")

        for value in results[key]:
            print('& ' + str(round(value, 3)), end=" ")

        print('\\\\')
        print('\\hline')


    # ind = np.array([i for i in range(N)])
    # width = 0.05
    # fig, ax = plt.subplots()
    #
    # for i, result in enumerate(results):
    #     # print(ind + i * width, result, width)
    #     ps.append(ax.bar(ind + i * width, result, width))
    #
    # ax.set_title('Results')
    # ax.set_xticks(ind + len(results) * width / 2)
    # ax.set_xticklabels(TIME_WINDOWS)
    #
    # ax.legend(ps, tuple(labels), bbox_to_anchor=(0., 1.04, 1., .11), loc=3,
    #        ncol=5, mode="expand", borderaxespad=0.)
    # ax.autoscale_view()
    #
    # fig, axes = plt.subplots(ncols=len(TIME_WINDOWS), sharey=True)
    # fig.subplots_adjust(wspace=0)
    #
    # for i, ax in enumerate(axes):
    #     ax.boxplot([result[i] for result in results])
    #     ax.set(xticklabels=labels, xlabel=TIME_WINDOWS[i])
    #     ax.margins(0.05)
    #
    # plt.ylim((10, 30))
    # plt.show()





if __name__ == '__main__':
    main()
