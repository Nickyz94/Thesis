from best_filter_files import get_files
import seaborn as sns
import pandas as pd
import get_performance
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

TIME_WINDOWS = [1.5, 5, 15, 30, 60, 120]

X_VALS = {
    'proxsig': 0.5,
    'proxfreq': 1,
    'proxsum': 1.5,
    'gridsig': 2,
    'gridfreq': 2.5,
    'gridsum': 3,
    'normsumsig': 3.5,
    'normsumfreq': 4,
    'normsumsum': 4.5,
    'normhadsig': 5,
    'normhadfreq': 5.5,
    'normhadsum': 6,
    'trilat': 6.5
}

COLORS = {
    1.5: 'r',
    5: 'b',
    15: 'g',
    30: 'c',
    60: 'm',
    120: 'y'
}

LEGEND_ELEMENTS = [Line2D([0], [0], color=COLORS[TIME_WINDOWS[i]], marker='o', label='time window = {}'.format(TIME_WINDOWS[i])) for i in range(6)]

filter_methods = ['Exponential', 'Irregular Exponential', 'Double Exponential',
                  'Median', 'Gauss Median', 'Shift Median', 'Kalman']

def main():
    results = {}

    for time_window in TIME_WINDOWS:
        results[time_window] = {}
        filter_files = get_files(time_window)
        for i, filter_file in enumerate(filter_files):
            dist, std = get_performance.main(filter_file[0], 'euc')

            try:
                results[time_window][filter_file[1]][filter_file[2]] = dist
            except:
                results[time_window][filter_file[1]] = {filter_file[2]: dist}

    f, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, sharey='row')
    f.delaxes(ax8)

    filter_plot_map = {
        'Exponential': ax1,
        'Irregular Exponential': ax2,
        'Double Exponential': ax3,
        'Median': ax4,
        'Gauss Median': ax5,
        'Shift Median': ax6,
        'Kalman': ax7,
    }

    x_ticks = ['proxsig', 'proxfreq', 'proxsum', 'gridsig', 'gridfreq',
               'gridsum', 'normsumsig', 'normsumfreq', 'normsumsum',
               'normhadsig', 'normhadfreq', 'normhadsum', 'trilat']

    for time_window in results:
        for filter_method in filter_methods:
            subplot = filter_plot_map[filter_method]
            xs = []
            ys = []
            filter_results = results[time_window][filter_method]

            for base_method in x_ticks:
                xs.append(X_VALS[base_method])
                ys.append(filter_results[base_method])

            subplot.scatter(xs, ys, c=COLORS[time_window])
            subplot.set_xticks(xs)
            subplot.set_xticklabels(x_ticks)
            subplot.set_title(filter_method)
            plt.setp(subplot.xaxis.get_majorticklabels(), rotation=90)

    ax1.set_xticklabels([])
    ax2.set_xticklabels([])
    ax3.set_xticklabels([])
    ax1.set_ylim((0, 30))
    ax5.set_ylim((0, 30))
    ax1.set_ylabel('Average Euclidean Distance')
    ax5.set_ylabel('Average Euclidean Distance')
    ax7.legend(handles=LEGEND_ELEMENTS, bbox_to_anchor=(2.0, 0.4))

    plt.show()

if __name__ == '__main__':
    main()
