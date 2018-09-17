import numpy as np

class Exp_mv_avg():
    """docstring for Exp_mv_avg"""
    def __init__(self, alpha):
        self.alpha = alpha

    def get_series(self, xs):
        S = np.array(xs[1])
        Ss = [xs[0], S]

        for x in xs[2:]:
            S = self.alpha * np.array(x) + (1 - self.alpha) * S
            Ss.append(S)

        return Ss

class Double_exp_smoothing():
    """docstring for Exp_mv_avg"""
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta

    def get_series(self, xs):
        S = np.array(xs[0])
        b = np.array(xs[1]) - np.array(xs[0])
        Ss = [S]

        for x in xs[1:]:
            prev_S = S
            S = self.alpha * np.array(x) + (1 - self.alpha) * (S + b)
            b = self.beta * (S - prev_S) + (1 - self.beta) * b
            Ss.append(S)

        return Ss
