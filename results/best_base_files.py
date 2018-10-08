BEST_BASE_FILES = [
    ['top_loc/results_top_loc_frequency_{}.csv', 'Frequency Proximity Sensing'],
    ['top_loc/results_top_loc_signal_{}.csv', 'Signal Proximity Sensing'],
    ['top_loc/results_top_loc_signal_sum_{}.csv', 'Signal Sum Proximity Sensing'],
    ['grid/top_loc/results_grid_freq_{}.csv', 'Frequency Top-Loc Grid'],
    ['grid/top_loc/results_grid_signal_{}.csv', 'Signal Top-Loc Grid'],
    ['grid/top_loc/results_grid_signal_sum_{}.csv', 'Signal Sum Top-Loc Grid'],
    ['grid/std_estimation_hadamard/results_grid_hadamard_normal_freq_{}_{}.csv', 'Normal Hadamard Frequency'],
    ['grid/std_estimation_hadamard/results_grid_hadamard_normal_signal_{}_{}.csv', 'Normal Hadamard Signal'],
    ['grid/std_estimation_hadamard/results_grid_hadamard_normal_sum_{}_{}.csv', 'Normal Hadamard Signal Sum'],
    ['grid/alpha_estimation_frequency/results_grid_normal_frequency_{}_{}.csv', 'Normal Sum Frequency'],
    ['grid/alpha_estimation_signal/results_grid_normal_signal_{}_{}.csv', 'Normal Sum Signal'],
    ['grid/alpha_estimation_signal_sum/results_grid_normal_signal_sum_{}_{}.csv', 'Normal Sum Signal Sum'],
    ['trilateration/results_trilateration_{}_{}.csv', 'Trilateration']
]

BEST_PARAMS = {
    'Normal Hadamard Frequency': {
        1.5: 6,
        5: 22,
        15: 16,
        30: 9,
        60: 29,
        120: 10,
    },
    'Normal Hadamard Signal': {
        1.5: 6,
        5: 8,
        15: 16,
        30: 14,
        60: 22,
        120: 24,
    },
    'Normal Hadamard Signal Sum': {
        1.5: 6,
        5: 8,
        15: 16,
        30: 9,
        60: 29,
        120: 10,
    },
    'Normal Sum Frequency': {
        1.5: 0.01,
        5: 0.02,
        15: 0.04,
        30: 0.07,
        60: 0.01,
        120: 0.01,
    },
    'Normal Sum Signal': {
        1.5: 0.04,
        5: 0.03,
        15: 0.42,
        30: 1.0,
        60: 0.13,
        120: 0.20,
    },
    'Normal Sum Signal Sum': {
        1.5: 0.02,
        5: 0.01,
        15: 0.02,
        30: 0.04,
        60: 0.01,
        120: 0.01,
    },
    'Trilateration': {
        1.5: 0.2,
        5: 0.05,
        15: 0.05,
        30: 0.1,
        60: 0.05,
        120: 0.0,
    }
}

def get_files(time_window):
    base_files = []
    for base_file in BEST_BASE_FILES:
        try:
            param_value = BEST_PARAMS[base_file[1]][time_window]
            base_files.append([base_file[0].format(time_window, param_value), base_file[1]])
        except KeyError:
            base_files.append([base_file[0].format(time_window), base_file[1]])

    return base_files
