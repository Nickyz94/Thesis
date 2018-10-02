from numpy import log, log10, pi
from numpy.linalg import norm
from scipy.constants import c
import scipy.optimize as opt
import numpy as np

f = 2.4e9

class Trilateration():
    """docstring for Trilateration"""
    def __init__(self, gamma):
        self.gamma = gamma

    def _create_args(self, sensors):
        return ([sensor['x'] for sensor in sensors],
                [sensor['y'] for sensor in sensors],
                [sensor['z'] for sensor in sensors],
                [sensor['signal'] for sensor in sensors])

    def _get_args(self, args):
        """
            Returns elements from args created by create_args
            RETURN (sensors, sigma)
        """
        return args[0]

    def _d(self, x_sen, y_sen, z_sen, x, y, z):
        return ((x - x_sen)**2 + (y - y_sen)**2 + (z - z_sen)**2)**0.5

    def _loc_gradient(self, x_sen, y_sen, z_sen, x, y, z):
        sen_vec = np.array([[x_sen], [y_sen], [z_sen]])
        loc_vec = np.array([[x], [y], [z]])
        return (10 * self.gamma / (log(10) * self._d(x_sen, y_sen, z_sen, x, y, z)**2) * (loc_vec - sen_vec).T)

    def _friis(self, x_sen, y_sen, z_sen, x, y, z, eta):
        return (eta - 10 * self.gamma * log10(self._d(x_sen, y_sen, z_sen, x, y, z)))

    def _loss(self, pars, xs, ys, zs, signals):
        """
            pars[0] -> x
            pars[1] -> y
            pars[2] -> z
            pars[2] -> eta
        """
        return [(signals[i] - self._friis(xs[i], ys[i], zs[i], pars[0],
                                          pars[1], pars[2], pars[3]))**2
                 for i, _ in enumerate(xs)]

    def _jac(self, pars, xs, ys, zs, signals):
        """
            pars[0] -> x
            pars[1] -> y
            pars[2] -> z
            pars[2] -> eta
        """
        return [np.append([-1], self._loc_gradient(xs[i], ys[i], zs[i], pars[0], pars[1], pars[2]))
                for i, _ in enumerate(xs)]

    def get_location(self, sensors):
        args = self._create_args(sensors)
        return opt.least_squares(self._loss,
                                 [0.0, 0.0, 0.0, 0.0],
                                #  jac=self._jac,
                                 args=args,
                                 method='lm')
