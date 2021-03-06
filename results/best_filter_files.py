BEST_FILTER_FILES = [
    ['exp_filter/', '{}_{}.csv', 'Exponential'],
    ['irr_exp_filter/', '{}_{}.csv', 'Irregular Exponential'],
    ['dbl_exp_filter/', '{}_{}_{}.csv', 'Double Exponential'],
    ['med_filter/', '{}_{}.csv', 'Median'],
    ['gauss_med_filter/', '{}_{}.csv', 'Gauss Median'],
    ['shift_med_filter/', '{}_{}.csv', 'Shift Median'],
    ['/media/nickyz/Data/scriptie_data/results/kalman_filter/', '{}_{}_{}.csv', 'Kalman']
]

BASE_PATH = {
    'proxsig': 'top_loc/results_top_loc_signal_',
    'proxfreq': 'top_loc/results_top_loc_frequency_',
    'proxsum': 'top_loc/results_top_loc_signal_sum_',
    'gridsig': 'grid/top_loc/results_grid_signal_',
    'gridfreq': 'grid/top_loc/results_grid_freq_',
    'gridsum': 'grid/top_loc/results_grid_signal_sum_',
    'normsumsig': 'grid/sum/results_grid_normal_signal_',
    'normsumfreq': 'grid/sum/results_grid_normal_frequency_',
    'normsumsum': 'grid/sum/results_grid_normal_signal_sum_',
    'normhadsig': 'grid/hadamard/results_grid_hadamard_normal_signal_',
    'normhadfreq': 'grid/hadamard/results_grid_hadamard_normal_freq_',
    'normhadsum': 'grid/hadamard/results_grid_hadamard_normal_sum_',
    'trilat': 'trilateration/results_trilateration_'
}

BEST_PARAMS = {
    'Exponential': {
        'proxsig': {
            1.5: 0.43,
            5: 0.58,
            15: 0.77,
            30: 0.8,
            60: 0.78,
            120: 0.66,
        },
        'proxfreq': {
            1.5: 0.38,
            5: 0.51,
            15: 0.76,
            30: 0.78,
            60: 0.76,
            120: 0.74,
        },
        'proxsum': {
            1.5: 0.39,
            5: 0.52,
            15: 0.76,
            30: 0.76,
            60: 0.76,
            120: 0.74,
        },
        'gridsig': {
            1.5: 0.38,
            5: 0.52,
            15: 0.69,
            30: 0.75,
            60: 0.77,
            120: 0.69,
        },
        'gridfreq': {
            1.5: 0.35,
            5: 0.5,
            15: 0.74,
            30: 0.77,
            60: 0.75,
            120: 0.74,
        },
        'gridsum': {
            1.5: 0.35,
            5: 0.51,
            15: 0.74,
            30: 0.77,
            60: 0.75,
            120: 0.74,
        },
        'normsumsig': {
            1.5: 0.4,
            5: 0.54,
            15: 0.8,
            30: 0.75,
            60: 0.79,
            120: 0.72,
        },
        'normsumfreq': {
            1.5: 0.36,
            5: 0.54,
            15: 0.78,
            30: 0.81,
            60: 0.81,
            120: 0.81,
        },
        'normsumsum': {
            1.5: 0.4,
            5: 0.54,
            15: 0.73,
            30: 0.87,
            60: 0.81,
            120: 0.81,
        },
        'normhadsig': {
            1.5: 0.4,
            5: 0.7,
            15: 0.89,
            30: 0.92,
            60: 0.9,
            120: 1.0,
        },
        'normhadfreq': {
            1.5: 0.36,
            5: 0.54,
            15: 0.78,
            30: 0.89,
            60: 0.81,
            120: 1.0,
        },
        'normhadsum': {
            1.5: 0.4,
            5: 0.64,
            15: 0.79,
            30: 0.9,
            60: 0.74,
            120: 1.0,
        },
        'trilat': {
            1.5: 0.67,
            5: 0.68,
            15: 0.72,
            30: 0.72,
            60: 0.72,
            120: 0.0,
        },
    },
    'Irregular Exponential': {
        'proxsig': {
            1.5: 4.6,
            5: 5.8,
            15: 10.1,
            30: 18.9,
            60: 40.2,
            120: 111.0,
        },
        'proxfreq': {
            1.5: 5.3,
            5: 7.0,
            15: 10.5,
            30: 20.1,
            60: 41.4,
            120: 90.0,
        },
        'proxsum': {
            1.5: 5.2,
            5: 6.8,
            15: 10.4,
            30: 21.2,
            60: 41.9,
            120: 90.0,
        },
        'gridsig': {
            1.5: 5.6,
            5: 6.8,
            15: 12.8,
            30: 21.6,
            60: 41.4,
            120: 101.4,
        },
        'gridfreq': {
            1.5: 6.3,
            5: 7.2,
            15: 11.1,
            30: 20.6,
            60: 43.5,
            120: 88.1,
        },
        'gridsum': {
            1.5: 6.1,
            5: 7.1,
            15: 11.2,
            30: 20.6,
            60: 43.8,
            120: 88.1,
        },
        'normsumsig': {
            1.5: 4.9,
            5: 6.4,
            15: 9.3,
            30: 21.6,
            60: 38.3,
            120: 94.9,
        },
        'normsumfreq': {
            1.5: 5.2,
            5: 6.4,
            15: 9.8,
            30: 18.3,
            60: 35.9,
            120: 72.3,
        },
        'normsumsum': {
            1.5: 5.0,
            5: 6.5,
            15: 11.4,
            30: 14.5,
            60: 35.9,
            120: 72.3,
        },
        'normhadsig': {
            1.5: 5.0,
            5: 4.2,
            15: 6.7,
            30: 12.0,
            60: 26.0,
            120: 0.1,
        },
        'normhadfreq': {
            1.5: 5.2,
            5: 6.4,
            15: 9.9,
            30: 13.5,
            60: 35.9,
            120: 0.1,
        },
        'normhadsum': {
            1.5: 5.0,
            5: 4.9,
            15: 9.5,
            30: 13.2,
            60: 44.5,
            120: 0.1,
        },
        'trilat': {
            1.5: 5.5,
            5: 5.9,
            15: 12.9,
            30: 23.5,
            60: 46.6,
            120: 0.1,
        },
    },
    'Double Exponential': {
        'proxsig': {
            1.5: (0.15, 0.35),
            5: (0.3, 0.5),
            15: (0.95, 0.7),
            30: (0.0, 1.0),
            60: (0.05, 0.85),
            120: (0.35, 0.75),
        },
        'proxfreq': {
            1.5: (0.15, 0.35),
            5: (0.0, 0.5),
            15: (0.0, 0.75),
            30: (1.0, 0.95),
            60: (0.1, 0.85),
            120: (0.5, 0.8),
        },
        'proxsum': {
            1.5: (0.15, 0.35),
            5: (0.0, 0.5),
            15: (0.0, 0.75),
            30: (1.0, 0.95),
            60: (0.1, 0.85),
            120: (0.5, 0.8),
        },
        'gridsig': {
            1.5: (0.1, 0.35),
            5: (0.25, 0.45),
            15: (0.8, 0.65),
            30: (0.0, 0.9),
            60: (0.05, 0.8),
            120: (0.3, 0.8),
        },
        'gridfreq': {
            1.5: (0.1, 0.3),
            5: (0.25, 0.45),
            15: (0.0, 0.75),
            30: (0.85, 0.85),
            60: (0.9, 0.85),
            120: (0.35, 0.8),
        },
        'gridsum': {
            1.5: (0.1, 0.3),
            5: (0.3, 0.45),
            15: (0.0, 0.75),
            30: (0.85, 0.85),
            60: (0.15, 0.85),
            120: (0.35, 0.8),
        },
        'normsumsig': {
            1.5: (0.1, 0.35),
            5: (0.0, 0.55),
            15: (0.9, 0.75),
            30: (0.0, 0.9),
            60: (0.05, 0.85),
            120: (0.0, 0.95),
        },
        'normsumfreq': {
            1.5: (0.05, 0.35),
            5: (0.05, 0.5),
            15: (0.0, 0.8),
            30: (0.0, 1.0),
            60: (0.0, 0.8),
            120: (0.25, 0.85),
        },
        'normsumsum': {
            1.5: (0.0, 0.4),
            5: (0.2, 0.5),
            15: (0.3, 0.7),
            30: (0.0, 1.0),
            60: (0.0, 0.8),
            120: (0.25, 0.85),
        },
        'normhadsig': {
            1.5: (0.0, 0.4),
            5: (0.0, 0.7),
            15: (0.0, 0.95),
            30: (0.0, 0.9),
            60: (0.0, 0.9),
            120: (0.0, 1.0),
        },
        'normhadfreq': {
            1.5: (0.05, 0.35),
            5: (0.05, 0.5),
            15: (0.0, 0.8),
            30: (0.0, 0.95),
            60: (0.0, 0.8),
            120: (0.0, 1.0),
        },
        'normhadsum': {
            1.5: (0.1, 0.35),
            5: (0.25, 0.55),
            15: (0.0, 0.8),
            30: (0.0, 1.0),
            60: (0.0, 0.75),
            120: (0.0, 1.0),
        },
        'trilat': {
            1.5: (0.5, 0.85),
            5: (0.25, 0.6),
            15: (0.05, 0.7),
            30: (0.1, 0.75),
            60: (0.05, 0.75),
            120: (0.0, 0.0),
        },
    },
    # 'Double Irregular Exponential': {
    #     'proxsig': {
    #         1.5: (7.5, 18.5),
    #         5: (7.5, 13.0),
    #         15: (12.0, 6.0),
    #         30: (0.5, 0.5),
    #         60: (34.0, 1043.0),
    #         120: (0.5, 0.5),
    #     },
    #     'proxfreq': {
    #         1.5: (7.5, 21.5),
    #         5: (8.0, 17.0),
    #         15: (10.0, 14.0),
    #         30: (8.5, 0.5),
    #         60: (33.0, 443.0),
    #         120: (73.0, 188.0)
    #     },
    #     'proxsum': {
    #         1.5: (7.5, 21.0),
    #         5: (8.0, 16.5),
    #         15: (10.5, 11.5),
    #         30: (9.0, 0.5),
    #         60: (34.0, 451.0),
    #         120: (73.0, 188.0),
    #     },
    #     'gridsig': {
    #         1.5: (9.5, 20.5),
    #         5: (8.0, 18.0),
    #         15: (13.5, 9.5),
    #         30: (11.5, 20.0),
    #         60: (26.5, 2.0),
    #         120: (0.5, 0.5),
    #     },
    #     'gridfreq': {
    #         1.5: (12.0, 23.0),
    #         5: (9.0, 16.0),
    #         15: (11.0, 26.0),
    #         30: (14.5, 18.0),
    #         60: (32.5, 27.0),
    #         120: (79.0, 262.0),
    #     },
    #     'gridsum': {
    #         1.5: (12.0, 22.5),
    #         5: (9.0, 16.0),
    #         15: (11.5, 24.5),
    #         30: (14.5, 18.0),
    #         60: (29.0, 22.0),
    #         120: (79.0, 262.0),
    #     },
    #     'normsumsig': {
    #         1.5: (8.0, 23.0),
    #         5: (7.5, 20.5),
    #         15: (11.0, 6.5),
    #         30: (11.5, 34.0),
    #         60: (25.5, 0.5),
    #         120: (0.5, 0.5),
    #     },
    #     'normsumfreq': {
    #         1.5: (4.5, 213.0),
    #         5: (6.5, 179.0)
    #         15: (10.0, 22.0),
    #         30: (1.0, 0.5),
    #         60: (36.0, 100000.0), # 90000 -> 100000: 12.5082278509 -> 12.5080447913
    #         120: (64.0, 456.0),
    #     },
    #     'normsumsum': {
    #         1.5: (8.5, 24.0),
    #         5: (7.5, 24.0),
    #         15: (13.0, 38.0),
    #         30: (0.5, 0.5),
    #         60: (12.0, 30.0),
    #         120: (30.0, 30.0),
    #     },
    #     'normhadsig': {
    #         1.5: (6.5, 28.0),
    #         5: (6.0, 17.0),
    #         15: (6.0, 9.5),
    #         30: (0.5, 0.5),
    #         60: (0.5, 0.5),
    #         120: (0.5, 0.5),
    #     },
    #     'normhadfreq': {
    #         1.5: (5.0, 30.0),
    #         5: (6.0, 30.0),
    #         15: (10.0, 22.0),
    #         30: (0.5, 0.5),
    #         60: (12.0, 30.0),
    #         120: (0.5, 0.5),
    #     },
    #     'normhadsum': {
    #         1.5: (8.5, 23.5),
    #         5: (6.5, 17.5),
    #         15: (9.5, 21.0),
    #         30: (0.5, 0.5),
    #         60: (28.0, 30.0),
    #         120: (0.5, 0.5),
    #     },
    #     'trilat': {
    #         1.5: (5.0, 7.0),
    #         5: (5.0, 12.0),
    #         15: (13.0, 30.0),
    #         30: (24.5, 30.0),
    #         60: (30.0, 30.0),
    #         120: (0.5, 0.5),
    #     },
    # },
    'Median': {
        'proxsig': {
            1.5: 26,
            5: 21,
            15: 4,
            30: 3,
            60: 1,
            120: 2,
        },
        'proxfreq': {
            1.5: 25,
            5: 22,
            15: 6,
            30: 3,
            60: 1,
            120: 2,
        },
        'proxsum': {
            1.5: 25,
            5: 22,
            15: 6,
            30: 3,
            60: 4,
            120: 2,
        },
        'gridsig': {
            1.5: 26,
            5: 21,
            15: 5,
            30: 10,
            60: 5,
            120: 2,
        },
        'gridfreq': {
            1.5: 25,
            5: 22,
            15: 6,
            30: 3,
            60: 1,
            120: 2,
        },
        'gridsum': {
            1.5: 25,
            5: 22,
            15: 6,
            30: 3,
            60: 1,
            120: 2,
        },
        'normsumsig': {
            1.5: 25,
            5: 22,
            15: 5,
            30: 1,
            60: 5,
            120: 3,
        },
        'normsumfreq': {
            1.5: 27,
            5: 19,
            15: 7,
            30: 3,
            60: 0,
            120: 0,
        },
        'normsumsum': {
            1.5: 26,
            5: 23,
            15: 2,
            30: 3,
            60: 0,
            120: 0,
        },
        'normhadsig': {
            1.5: 27,
            5: 21,
            15: 5,
            30: 2,
            60: 2,
            120: 0,
        },
        'normhadfreq': {
            1.5: 26,
            5: 19,
            15: 7,
            30: 3,
            60: 0,
            120: 0,
        },
        'normhadsum': {
            1.5: 26,
            5: 22,
            15: 7,
            30: 3,
            60: 0,
            120: 0,
        },
        'trilat': {
            1.5: 14,
            5: 10,
            15: 5,
            30: 2,
            60: 3,
            120: 0,
        },
    },
    'Gauss Median': {
        'proxsig': {
            1.5: 26,
            5: 22,
            15: 4,
            30: 3,
            60: 3,
            120: 2,
        },
        'proxfreq': {
            1.5: 25,
            5: 22,
            15: 6,
            30: 3,
            60: 1,
            120: 2,
        },
        'proxsum': {
            1.5: 25,
            5: 22,
            15: 6,
            30: 3,
            60: 4,
            120: 2,
        },
        'gridsig': {
            1.5: 26,
            5: 21,
            15: 5,
            30: 9,
            60: 4,
            120: 2,
        },
        'gridfreq': {
            1.5: 25,
            5: 22,
            15: 6,
            30: 3,
            60: 1,
            120: 2,
        },
        'gridsum': {
            1.5: 25,
            5: 22,
            15: 6,
            30: 3,
            60: 1,
            120: 2,
        },
        'normsumsig': {
            1.5: 25,
            5: 23,
            15: 5,
            30: 30,
            60: 4,
            120: 2,
        },
        'normsumfreq': {
            1.5: 27,
            5: 19,
            15: 7,
            30: 3,
            60: 0,
            120: 0,
        },
        'normsumsum': {
            1.5: 26,
            5: 23,
            15: 3,
            30: 3,
            60: 0,
            120: 0,
        },
        'normhadsig': {
            1.5: 27,
            5: 23,
            15: 5,
            30: 2,
            60: 0,
            120: 0,
        },
        'normhadfreq': {
            1.5: 26,
            5: 19,
            15: 7,
            30: 3,
            60: 0,
            120: 0,
        },
        'normhadsum': {
            1.5: 26,
            5: 22,
            15: 10,
            30: 3,
            60: 0,
            120: 0,
        },
        'trilat': {
            1.5: 14,
            5: 16,
            15: 5,
            30: 2,
            60: 4,
            120: 0,
        },
    },
    'Shift Median': {
        'proxsig': {
            1.5: 26,
            5: 21,
            15: 4,
            30: 3,
            60: 1,
            120: 2,
        },
        'proxfreq': {
            1.5: 25,
            5: 22,
            15: 6,
            30: 3,
            60: 1,
            120: 2,
        },
        'proxsum': {
            1.5: 25,
            5: 22,
            15: 6,
            30: 3,
            60: 4,
            120: 2,
        },
        'gridsig': {
            1.5: 26,
            5: 21,
            15: 21,
            30: 10,
            60: 5,
            120: 2,
        },
        'gridfreq': {
            1.5: 25,
            5: 22,
            15: 6,
            30: 3,
            60: 1,
            120: 2,
        },
        'gridsum': {
            1.5: 25,
            5: 22,
            15: 6,
            30: 3,
            60: 1,
            120: 2,
        },
        'normsumsig': {
            1.5: 25,
            5: 22,
            15: 5,
            30: 1,
            60: 5,
            120: 3,
        },
        'normsumfreq': {
            1.5: 27,
            5: 19,
            15: 7,
            30: 3,
            60: 0,
            120: 0,
        },
        'normsumsum': {
            1.5: 26,
            5: 23,
            15: 2,
            30: 3,
            60: 0,
            120: 0,
        },
        'normhadsig': {
            1.5: 27,
            5: 23,
            15: 5,
            30: 2,
            60: 2,
            120: 0,
        },
        'normhadfreq': {
            1.5: 26,
            5: 19,
            15: 7,
            30: 3,
            60: 0,
            120: 0,
        },
        'normhadsum': {
            1.5: 26,
            5: 23,
            15: 7,
            30: 3,
            60: 0,
            120: 0,
        },
        'trilat': {
            1.5: 14,
            5: 10,
            15: 5,
            30: 2,
            60: 3,
            120: 0,
        },
    },
    'Kalman': {
        'proxsig': {
            1.5: (5, 1),
            5: (6, 1),
            15: (7, 2),
            30: (28, 8),
            60: (64, 20),
            120: (3, 1)
        },
        'proxfreq': {
            1.5: (5, 1),
            5: (6, 1),
            15: (7, 2),
            30: (57, 14),
            60: (150, 34),
            120: (4, 1)
        },
        'proxsum': {
            1.5: (5, 1),
            5: (6, 1),
            15: (4, 1),
            30: (54, 14),
            60: (150, 34),
            120: (4, 1)
        },
        'gridsig': {
            1.5: (11, 2),
            5: (7, 1),
            15: (6, 1),
            30: (11, 2),
            60: (74, 18),
            120: (4, 1)
        },
        'gridfreq': {
            1.5: (11, 2),
            5: (7, 1),
            15: (5, 1),
            30: (19, 3),
            60: (189, 29),
            120: (4, 1)
        },
        'gridsum': {
            1.5: (11, 2),
            5: (7, 1),
            15: (5, 1),
            30: (19, 3),
            60: (189, 29),
            120: (4, 1)
        },
        'normsumsig': {
            1.5: (6, 1),
            5: (7, 1),
            15: (7, 2),
            30: (11, 2),
            60: (82, 18),
            120: (5, 2)
        },
        'normsumfreq': {
            1.5: (7, 1),
            5: (7, 1),
            15: (6, 1),
            30: (18, 5),
            60: (41, 12),
            120: (7, 2)
        },
        'normsumsum': {
            1.5: (8, 1),
            5: (13, 2),
            15: (15, 1),
            30: (76, 23),
            60: (41, 12),
            120: (7, 2)
        },
        'normhadsig': {
            1.5: (8, 1),
            5: (7, 1),
            15: (6, 1),
            30: (5, 1),
            60: (108, 39),
            120: (1494, 111)
        },
        'normhadfreq': {
            1.5: (8, 1),
            5: (7, 1),
            15: (6, 1),
            30: (7, 2),
            60: (41, 12),
            120: (18, 5)
        },
        'normhadsum': {
            1.5: (8, 1),
            5: (7, 1),
            15: (5, 1),
            30: (11, 3),
            60: (38, 12),
            120: (18, 5)
        },
        'trilat': {
            1.5: (399, 22),
            5: (28, 1),
            15: (10, 3),
            30: (3, 1),
            60: (19, 6),
            120: (1, 1)
        }
    }
}

def get_files(time_window):
    files = []
    for filter_method in BEST_FILTER_FILES:
        for base_method, path in BASE_PATH.items():
            prefix = filter_method[0]
            middle = path
            best_params = BEST_PARAMS[filter_method[2]][base_method][time_window]

            if type(best_params) == tuple:
                postfix = filter_method[1].format(time_window, *best_params)
            else:
                postfix = filter_method[1].format(time_window, best_params)

            files.append((prefix + middle + postfix, filter_method[2], base_method))

    return files
