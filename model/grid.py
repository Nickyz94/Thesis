X_OFFSET = -150
Y_OFFSET = -150
Z_OFFSET = 0
CELL_SIZE = 10
GRID_MATRIX_SIZE = (30, 35)
NORM_STD = [[10, 0], [0, 10]]

def grid_index(loc, bottom, size=10):
    return int((loc[0] - bottom[0]) / size),
           int((loc[1] - bottom[1]) / size),
           int((loc[2] - bottom[2]) / size)

def get_xyz(index, bottom, size=10):
    return (bottom[0] + (index[0] + 0.5) * size,
            bottom[1] + (index[1] + 0.5) * size,
            bottom[2] + (index[2] + 0.5) * size)

def create_norm_matrix(mean):
    x_space = np.linspace(0, GRID_MATRIX_SIZE[1], GRID_MATRIX_SIZE[1], endpoint=False)
    y_space = np.linspace(0, GRID_MATRIX_SIZE[0], GRID_MATRIX_SIZE[0], endpoint=False)
    X, Y = np.meshgrid(x_space, y_space)
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X; pos[:, :, 1] = Y

    rv = multivariate_normal(mean, NORM_STD)
    return rv.pdf(pos)

def get_max_matrix_value(matrix):
    max_index = matrix.argmax()

    return (max_index % GRID_MATRIX_SIZE[1], max_index // GRID_MATRIX_SIZE[1])

def top_loc_grid_signal(data, mac):
    results = []

    time_grouped = group_data(data[mac], 0)
    for time_group in time_grouped:
        values = list(time_group[1])
        g_data = [(item[0], item[1], item[2]) for item in values]
        g_data = sorted(g_data, key=lambda x: -x[2])

        index_count = {}
        ids = []
        all_locs = []

        for row in g_data:
            loc = find_location(row[1], drone_data)

            if loc is None:
                continue

            loc_tup = (loc['x_m'], loc['y_m'], loc['z_m'])

            index = grid_index(loc_tup, (X_OFFSET, Y_OFFSET, Z_OFFSET), CELL_SIZE)
            index_tup = (index[0], index[1])

        res = get_xy(top_loc(index_count), (X_OFFSET, Y_OFFSET, Z_OFFSET), CELL_SIZE)
        results.append([res[0], res[1]])

    return results

def top_loc_grid_signal_sum(data, mac):
    results = []

    time_grouped = group_data(data[mac], 0)
    for time_group in time_grouped:
        values = list(time_group[1])
        g_data = [(item[0], item[1], item[2]) for item in values]

        index_count = {}
        ids = []
        all_locs = []

        for row in g_data:
            loc = find_location(row[1], drone_data)

            if loc is None:
                continue

            loc_tup = (loc['x_m'], loc['y_m'], loc['z_m'])

            index = grid_index(loc_tup, (X_OFFSET, Y_OFFSET, Z_OFFSET), CELL_SIZE)
            index_tup = (index[0], index[1])

            try:
                index_count[index_tup] += 100 + int(row[2])
            except KeyError:
                index_count[index_tup] = 100 + int(row[2])

        top_loc = max(index_count, key=lambda x: index_count[x])

        res = get_xyz(top_loc, (X_OFFSET, Y_OFFSET, Z_OFFSET), CELL_SIZE)
        results.append([res[0], res[1]])

    return results

def top_loc_grid_freq(data, mac):
    results = []

    time_grouped = group_data(data[mac], 0)
    for time_group in time_grouped:
        values = list(time_group[1])
        g_data = [(item[0], item[1], item[2]) for item in values]

        index_count = {}
        ids = []
        all_locs = []

        for row in g_data:
            loc = find_location(row[1], drone_data)

            if loc is None:
                continue

            loc_tup = (loc['x_m'], loc['y_m'], loc['z_m'])

            index = grid_index(loc_tup, (X_OFFSET, Y_OFFSET, Z_OFFSET), CELL_SIZE)
            index_tup = (index[0], index[1])

            try:
                index_count[index_tup][0] += 1
                index_count[index_tup][1] += 100 + int(row[2])
            except KeyError:
                index_count[index_tup] = [1, 100 + int(row[2])]

        top_loc = max(index_count, key=lambda x: (index_count[x][0],
                                                  index_count[x][1]))

        res = get_xyz(top_loc, (X_OFFSET, Y_OFFSET, Z_OFFSET), CELL_SIZE)
        results.append([res[0], res[1]])

    return results
