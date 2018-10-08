class Median_filter():
    """docstring for Median_filter"""
    def __init__(self, window):
        self.window = window

    def get_series(self, xs):
        locs = []
        last_index = len(xs) - 1

        for i, x in enumerate(xs):
            data = []
            data.append(x)

            for j in range(1, self.window + 1):
                data.append(xs[max(0, i - j)])
                data.append(xs[min(last_index, i + j)])

            x_locs, y_locs = zip(*data)
            x_locs = sorted(x_locs)
            y_locs = sorted(y_locs)

            locs.append((x_locs[self.window], y_locs[self.window]))

        return locs

class Gaussian_median_filter():
    """docstring for Gaussian_median_filter"""
    def __init__(self, window, sigma):
        self.window = window
        self.sigma = sigma

    def weight(x):
        return 1 / (self.sigma * (2 * np.pi)**0.5) * np.exp(-x**2 / (2 * self.sigma**2))

    def get_series(self, xs):
        locs = []
        last_index = len(xs) - 1

        for i, x in enumerate(xs):
            data = []
            data.append(x[1], weight(x[0] - x[0]))

            for j in range(1, self.window + 1):
                low_index = max(0, i - j)
                low_weight = self.weight(x[0] - xs[low_index][0])
                data.append((xs[low_index][1], low_weight))

                high_index = min(last_index, i + j)
                high_weight = self.weight(xs[0] - xs[high_index][0])
                data.append((xs[high_index][1], high_weight))

            weight_threshold = 0.5 * sum([row[1] for row in data])

            x_sorted = sorted(data, key=lambda k: k[0][0])
            weight_sum_start = 0
            weight_sum_end = 0
            i = -1

            while(weight_sum_start < weight_threshold):
                i += 1
                weight_sum_start += x_sorted[i][1]

            j = len(x_sorted)

            while(weight_sum_end < weight_threshold):
                j -= 1
                weight_sum_end += x_sorted[j][1]

            x_val = (x_sorted[i][0][0] + x_sorted[j][0][0]) / 2

            y_sorted = sorted(data, key=lambda k: k[0][1])
            weight_sum_start = 0
            weight_sum_end = 0
            i = -1

            while(weight_sum_start < weight_threshold):
                i += 1
                weight_sum_start += y_sorted[i][1]

            j = len(y_sorted)

            while(weight_sum_end < weight_threshold):
                j -= 1
                weight_sum_end += y_sorted[j][1]

            y_val = (y_sorted[i][0][1] + y_sorted[j][0][1]) / 2

            locs.append((x_val, y_val))

        return locs

class Shifting_median_filter():
    """docstring for Shifting_median_filter"""
    def __init__(self, window):
        self.window = window

    def get_series(self, xs):
        locs = []
        last_index = len(xs) - 1

        for i, x in enumerate(xs):
            data = []
            D = sorted([abs(x[0] - xt[0]) for xt in xs])
            data.append(x[1], D[-1] + D[1])

            for j in range(1, self.window + 1):
                low_index = max(0, i - j)
                low_weight = D[-1] - abs(x[0] - xs[low_index][0]) + D[1]
                data.append((xs[low_index][1], low_weight))

                high_index = min(last_index, i + j)
                high_weight = D[-1] - abs(x[0] - xs[high_index][0]) + D[1]
                data.append((xs[high_index][1], high_weight))

            weight_threshold = 0.5 * sum([row[1] for row in data])

            x_sorted = sorted(data, key=lambda k: k[0][0])
            weight_sum_start = 0
            weight_sum_end = 0
            i = -1

            while(weight_sum_start < weight_threshold):
                i += 1
                weight_sum_start += x_sorted[i][1]

            j = len(x_sorted)

            while(weight_sum_end < weight_threshold):
                j -= 1
                weight_sum_end += x_sorted[j][1]

            x_val = (x_sorted[i][0][0] + x_sorted[j][0][0]) / 2

            y_sorted = sorted(data, key=lambda k: k[0][1])
            weight_sum_start = 0
            weight_sum_end = 0
            i = -1

            while(weight_sum_start < weight_threshold):
                i += 1
                weight_sum_start += y_sorted[i][1]

            j = len(y_sorted)

            while(weight_sum_end < weight_threshold):
                j -= 1
                weight_sum_end += y_sorted[j][1]

            y_val = (y_sorted[i][0][1] + y_sorted[j][0][1]) / 2

            locs.append((x_val, y_val))

        return locs
