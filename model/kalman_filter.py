import numpy as np

class KalmanFilter():
    """docstring for KalmanFilter"""
    H = np.identity(2)

    def __init__(self, m0, P0, t0, q_sigma, r_sigma):
        self.m = np.array([m0]).T
        self.P = P0
        self.t0 = t0
        self.Q = q_sigma**2 * np.identity(2)
        self.R = r_sigma**2 * np.identity(2)

    def _prediction(self, A):
        self.m_est = A * self.m
        self.P_est = A * self.P * A.T + self.Q

    def _update(self, y, A):
        v = y - self.H * self.m_est
        S = self.H * self.P_est * self.H.T + self.R
        K = self.P_est * self.H.T * S.I
        self.m = self.m_est + K * v
        self.P = self.P_est - K * S * K.T

    def _kalman_step(self, y, dt):
        A = np.matrix([[1, dt], [0, 1]])
        self._prediction(A)
        self._update(np.matrix(y).T, A)

        return self.m

    def perform_kalman_steps(self, ys, dts):
        results = [self.m.T[0]]
        prev_time = self.t0

        for i, y in enumerate(ys):
            results.append(self._kalman_step(y, dts[i] - prev_time).T.tolist()[0])
            prev_time = dts[i]

        return results
