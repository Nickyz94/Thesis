from best_filter_files import get_files
import seaborn as sns
import pandas as pd
import get_performance

TIME_WINDOWS = [1.5, 5, 15, 30, 60, 120]

def main():
    for time_window in TIME_WINDOWS:
        results = []
        filter_files = get_files(time_window)
        for i, filter_file in enumerate(filter_files):
            dist, std = get_performance.main(filter_file[0], 'euc')

            results.append([dist, filter_file[1], filter_file[2]])

        print(results)

        # g = sns.FacetGrid()

if __name__ == '__main__':
    main()
