from datetime import datetime
import numpy as np
from read_test_data import find_location, read_drone_data, group_data, SECONDS_GROUPING
from scipy.stats import multivariate_normal

X_OFFSET = -150
Y_OFFSET = -150
Z_OFFSET = 0
MAX_SECONDS_DIFF = max(SECONDS_GROUPING, 5)

def grid_index(loc, bottom, size=10):
    return (int((loc[0] - bottom[0]) / size),
            int((loc[1] - bottom[1]) / size))

def get_xyz(index, bottom, size=10):
    return (bottom[0] + (index[0] + 0.5) * size,
            bottom[1] + (index[1] + 0.5) * size)

def create_norm_matrix(mean, std, dimensions):
    x_space = np.linspace(0, dimensions[1], dimensions[1], endpoint=False)
    y_space = np.linspace(0, dimensions[0], dimensions[0], endpoint=False)
    X, Y = np.meshgrid(x_space, y_space)
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X; pos[:, :, 1] = Y

    rv = multivariate_normal(mean, std)
    return rv.pdf(pos)

def get_max_matrix_value(matrix):
    return np.unravel_index(np.argmax(matrix, axis=None), matrix.shape)

def get_dimensions(size):
    return (int(300 / size + 0.5), int(350 / size + 0.5))

def create_std_matrix(std):
    return [[std, 0], [0, std]]

def top_loc_grid_signal(data, mac, size):
    results = []
    drone_data = read_drone_data()
    time_grouped = group_data(data, 0)

    for time_group in time_grouped:
        max_score = max(time_group[1], key=lambda x: x[2])

        loc = find_location(max_score[1], drone_data)
        loc_tup = (loc['x_m'], loc['y_m'])

        index = grid_index(loc_tup, (X_OFFSET, Y_OFFSET), size)
        index_tup = (index[0], index[1])

        res = get_xyz(index_tup, (X_OFFSET, Y_OFFSET), size)
        results.append([mac, time_group[0], res[0], res[1]])

    return results

def top_loc_grid_signal_sum(data, mac, size):
    results = []
    drone_data = read_drone_data()
    time_grouped = group_data(data, 0)

    for time_group in time_grouped:
        index_count = {}

        for row in time_group[1]:
            loc = find_location(row[1], drone_data)
            loc_tup = (loc['x_m'], loc['y_m'])

            index = grid_index(loc_tup, (X_OFFSET, Y_OFFSET), size)
            index_tup = (index[0], index[1])

            try:
                index_count[index_tup] += 100 + int(row[2])
            except KeyError:
                index_count[index_tup] = 100 + int(row[2])

        top_loc = max(index_count, key=lambda x: index_count[x])

        res = get_xyz(top_loc, (X_OFFSET, Y_OFFSET), size)
        results.append([mac, time_group[0], res[0], res[1]])

    return results

def top_loc_grid_freq(data, mac, size):
    results = []
    drone_data = read_drone_data()
    time_grouped = group_data(data, 0)

    for time_group in time_grouped:
        index_count = {}

        for row in time_group[1]:
            loc = find_location(row[1], drone_data)
            loc_tup = (loc['x_m'], loc['y_m'])

            index = grid_index(loc_tup, (X_OFFSET, Y_OFFSET), size)
            index_tup = (index[0], index[1])

            try:
                index_count[index_tup][0] += 1
                index_count[index_tup][1] += 100 + int(row[2])
            except KeyError:
                index_count[index_tup] = [1, 100 + int(row[2])]

        top_loc = max(index_count, key=lambda x: (index_count[x][0],
                                                  index_count[x][1]))

        res = get_xyz(top_loc, (X_OFFSET, Y_OFFSET), size)
        results.append([mac, time_group[0], res[0], res[1]])

    return results

def normal_grid_method(data, mac, size, std, alpha=0.5, signal_sum=True):
    results = []
    drone_data = read_drone_data()
    prev_pos = None
    prev_time = None
    dimensions = get_dimensions(size)
    std_matrix = create_std_matrix(std)

    time_grouped = group_data(data, 0)
    for time_group in time_grouped:
        values = list(time_group[1])
        g_data = [(item[0], item[1], item[2]) for item in values]

        index_count = np.zeros(dimensions)

        for row in g_data:
            loc = find_location(row[1], drone_data)

            if loc is None:
                continue

            loc_tup = (loc['x_m'], loc['y_m'])

            index = grid_index(loc_tup, (X_OFFSET, Y_OFFSET), size)
            index_tup = (index[0], index[1])

            if signal_sum:
                index_count[index_tup] += 100 + int(row[2])
            else:
                index_count[index_tup] += 1

        # make the matrix sum up to 1
        index_count = index_count / np.sum(index_count)

        if prev_pos is None or (time_group[0] - prev_time) > MAX_SECONDS_DIFF:
            prev_pos = get_max_matrix_value(index_count)
        else:
            norm_matrix = create_norm_matrix((prev_pos[1], prev_pos[0]), std_matrix, dimensions)
            prev_pos = get_max_matrix_value(alpha * index_count + (1 - alpha) * norm_matrix)


        res = get_xyz(prev_pos, (X_OFFSET, Y_OFFSET), size)
        prev_time = time_group[0]
        results.append([mac, time_group[0], res[0], res[1]])

    return results
