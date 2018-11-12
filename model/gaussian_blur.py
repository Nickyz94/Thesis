from scipy.stats import multivariate_normal
import numpy as np

class Gaus_blur():
    """docstring for Gaus_blur"""
    def __init__(self, sigma, ap_locs):
        self.sigma = sigma
        self.ap_locs = ap_locs

    def _gauss(self, x):
        return 1 / (self.sigma * (2 * np.pi)**0.5) * np.exp(-x**2 / (2 * self.sigma**2))

    def _dist(self, ap_x, ap_y):
        return ((ap_x[0] - ap_y[0])**2 + (ap_x[1] - ap_y[1])**2)**0.5

    def perform_blur(self, ap_probs):
        blurred_probs = {}
        for ap_m in ap_probs:
            ap_m_loc = self.ap_locs[ap_m]
            blurred_probs[ap_m] = sum([ap_probs[ap_n] * self._gauss(self._dist(ap_m_loc, self.ap_locs[ap_n]))
                                       for ap_n in ap_probs])

        return blurred_probs
