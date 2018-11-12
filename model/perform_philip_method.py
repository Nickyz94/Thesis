from bayesian_philip import Bayesian_Philip
from best_base_files import get_files
import csv
import numpy as np
from read_test_data import read_drone_data
import pandas as pd


TIME_WINDOWS = [1.5, 5, 15, 30, 60, 120]

def main():
    drones = {}

    drone_data = read_drone_data()

    for index, drone in drone_data.iterrows():
        if drone['drone_id'] is not np.nan:
            drones[drone['drone_id']] = (drone['x_m'], drone['y_m'])

    for window in TIME_WINDOWS:
        files = get_files(window)

        for file_name, method, output in files:
            data = []
            times = []
            sourcemac = None

            with open(file_name, 'r') as f:
                reader = csv.DictReader(f, delimiter=';')

                for row in reader:
                    data.append((float(row['x_m']), float(row['y_m'])))
                    times.append(float(row['timestamp']))
                    sourcemac = row['sourcemac']

            for sigma in range(1, 51):
                Bayesian_Philip()

if __name__ == '__main__':
    main()
