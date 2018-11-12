from gaussian_blur import Gaus_blur

class Bayesian_Philip():
    """docstring for Bayesian_Philip"""
    def __init__(self, sensors, sigma):
        """sensors = {sensor_name: location}"""
        self.prior = self._set_initial_prior(sensors)
        self.sensor_locations = sensors
        self.gaus_blur = Gaus_blur(sigma, sensors)

    def _set_initial_prior(self, sensors):
        uniform_prior = 1 / len(sensors)

        return {sensor: uniform_prior for sensor in sensors}

    def _create_prob_dist(self, signals):
        unnormalized = {signal: 100 - abs(strength) for signal, strength in signals.items()}

        norm_factor = sum(unnormalized.values())

        return {signal: unnorm / norm_factor for signal, unnorm in unnormalized.items()}

    def _calculate_posterior(self, likelyhood):
        posterior = {}

        for sensor in likelyhood:
            posterior[sensor] = likelyhood[sensor] * self.prior[sensor]

        norm_sum = sum(posterior.values())

        return {sensor: posterior[sensor] / norm_sum for sensor in posterior}

    def perform_step(self, signals):
        """signals = {sensor_name: rssi_value}"""
        prob_dist = self._create_prob_dist(signals)
        likelyhood = self.gaus_blur.perform_blur(prob_dist)
        posterior = self._calculate_posterior(likelyhood)

        self.prior = self.gaus_blur.perform_blur(posterior)

        return posterior
