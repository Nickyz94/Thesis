import numpy as np

class Exp_mv_avg():
    """docstring for Exp_mv_avg"""
    def __init__(self, alpha):
        self.alpha = alpha

    def get_series(self, xs):
        S = np.array(xs[0])
        Ss = [S]

        for x in xs[1:]:
            S = self.alpha * np.array(x) + (1 - self.alpha) * S
            Ss.append(S)

        return Ss

class Irr_exp_mv_avg():
    """docstring for Exp_mv_avg"""
    def __init__(self, alpha):
        self.tau = tau

    def calc_irr_alpha(self, t, prev_t):
        return 1 - np.exp(-(t - prev_t) / self.tau)

    def get_series(self, xs):
        S = np.array(xs[0][1])
        prev_time = xs[0][0]
        Ss = [S]

        for x in xs[1:]:
            alpha = self.calc_irr_alpha(x[0], prev_time)
            S = self.alpha * np.array(x[1]) + (1 - self.alpha) * S
            Ss.append(S)
            prev_time = x[0]

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

class Irr_double_exp_smoothing():
    """docstring for Exp_mv_avg"""
    def __init__(self, alpha, beta):
        self.tau = tau

    def calc_irr_alpha(self, t, prev_t):
        return 1 - np.exp(-(t - prev_t) / self.tau)

    def get_series(self, xs):
        S = np.array(xs[0][1])
        b = np.array(xs[1][1]) - np.array(xs[0][1])
        prev_time = xs[0][0]
        Ss = [S]

        for x in xs[1:]:
            alpha = self.calc_irr_alpha(x[0], prev_time)
            prev_time = x[0]
            prev_S = S
            S = alpha * np.array(x[1]) + (1 - alpha) * (S + b)
            b = alpha * (S - prev_S) + (1 - alpha) * b
            Ss.append(S)

        return Ss
