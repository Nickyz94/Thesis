from best_base_files import get_files
import get_performance
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as mcolors

TIME_WINDOWS = [1.5, 5, 15, 30, 60, 120]
# COLORS = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
BAR_COLORS = [
    (1,101,252,1),
    'xkcd:scarlet',
    'xkcd:orange red',
    'xkcd:bright blue',
    'xkcd:cerulean',
    'xkcd:steel blue',
]

def main():
    N = len(TIME_WINDOWS)
    results = []
    labels = []
    ps = []

    for window in TIME_WINDOWS:
        base_files = get_files(window)

        for i, base_file in enumerate(base_files):
            labels.append(base_file[1])
            try:
                results[i].append(get_performance.main(base_file[0], 'man'))
            except IndexError:
                results.append([get_performance.main(base_file[0], 'man')])

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

    fig, axes = plt.subplots(ncols=len(TIME_WINDOWS), sharey=True)
    fig.subplots_adjust(wspace=0)

    for i, ax in enumerate(axes):
        ax.boxplot([result[i] for result in results])
        ax.set(xticklabels=labels, xlabel=TIME_WINDOWS[i])
        ax.margins(0.05)

    plt.ylim((10, 30))
    plt.show()



if __name__ == '__main__':
    main()
