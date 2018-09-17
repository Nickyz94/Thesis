from scipy.stats import multivariate_normal
import numpy as np

class Gaus_blur():
    """docstring for Gaus_blur"""
    def __init__(self, sigma, dimensions, ap_dict):
        cov_matrix = np.array([[sigma, 0], [0, sigma]])
        gaus_matrix = self._create_gaus_matrix(cov_matrix, dimensions)
        self._get_gaus_values(ap_dict, gaus_matrix)

    def _create_gaus_matrix(self, cov, dimensions):
        x_space = np.linspace(0, dimensions[0], dimensions[0], endpoint=False)
        y_space = np.linspace(0, dimensions[1], dimensions[1], endpoint=False)
        X, Y = np.meshgrid(x_space, y_space)
        pos = np.empty(X.shape + (2,))
        pos[:, :, 0] = X; pos[:, :, 1] = Y

        rv = multivariate_normal(cov=cov)
        return rv.pdf(pos)

    def _get_gaus_values(self, ap_dict, gaus_matrix):
        self.ap_gaus_dict = {}
        for ap_x in ap_dict:
            self.ap_gaus_dict[ap_x] = {}
            ap_pos = ap_dict[ap_x]

            for ap_y in ap_dict.values():
                x_dif = abs(ap_pos[0] - ap_y[0])
                y_dif = abs(ap_pos[1] - ap_y[1])
                self.ap_gaus_dict[ap_x][ap_y] = gaus_matrix[y_dif, x_dif]

    def perform_blur(self, ap_probs):
        blurred_probs = {}
        for ap_m in ap_probs:
            gaus_vals = self.ap_gaus_dict[ap_m]
            blurred_probs[ap_m] = sum([ap_probs[ap_n] * gaus_vals[ap_n] for ap_n in ap_probs])

        return blurred_probs
