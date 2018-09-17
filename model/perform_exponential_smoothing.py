from exponential_smoothing import Exp_mv_avg, Double_exp_smoothing
import csv
import numpy as np

def main(input_file, output_file, double=False, alpha=0.5, beta=None):
    if double:
        smooth = Double_exp_smoothing(alpha, beta)
        name_postfix = '{}_{}_{}'.format('double_exp_smoothing', str(alpha), str(beta))
    else:
        smooth = Exp_mv_avg(alpha)
        name_postfix = '{}_{}'.format('double_exp_smoothing', alpha)

    with open(input_file, 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        full_data = list(reader)

    loc_data = [[float(row['x_m']), float(row['y_m']), float(row['z_m'])] for row in full_data]

    results = smooth.get_series(loc_data)

    with open('../results/{}_{}.csv'.format(output_file, name_postfix), 'a') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["sourcemac", "timestamp", "x_m", "y_m", "z_m"])

        for i, row in enumerate(results):
            writer.writerow([full_data[i]['sourcemac'], full_data[i]['timestamp']] +
                            list(results[i]))



if __name__ == '__main__':
    input_files = ['../results/results_top_loc_frequency.csv',
                   '../results/results_top_loc_signal_sum.csv',
                   '../results/results_top_loc_signal.csv']

    output_files = ['results_top_loc_frequency',
                    'results_top_loc_signal_sum',
                    'results_top_loc_signal']

    ab_values = list(np.arange(0, 1.01, 0.1))

    for i, file_name in enumerate(input_files):
        for a_value in ab_values:
            main(file_name, output_files[i], alpha=a_value)
            for b_value in ab_values:
                main(file_name, output_files[i], double=True, alpha=a_value, beta=b_value)
