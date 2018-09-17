import fileinput
import time
import glob
import json
import datetime
import itertools
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_data():
    start = time.time()
    data = {}
    files = glob.glob('/media/nickyz/Data/scriptie_data/armin/20170512_[4-5].csv')
    print(files)
    files.reverse()

    for line in fileinput.input(files=files):
        if fileinput.isfirstline():
            print(time.time() - start)
            print(fileinput.filename())
            start = time.time()
            continue

        splitted = line.split('\t')
        values = json.loads(splitted[0])

        try:
            sourceMac = values['sourceMac']
        except KeyError:
            sourceMac = values['sourcemac']

        try:
            localMac = int(values['localMac'])
        except KeyError:
            localMac = int(values['localmac'])

        signal = int(values['signal'])

        if(localMac):
            continue

        try:
            droneId = values['droneId']
        except KeyError:
            droneId = values['droneid']

        timestamp = splitted[2]
        timestamp = datetime.datetime.fromtimestamp(int(timestamp[0:-3])).strftime('%Y-%m-%d %H:%M')

        try:
            data[sourceMac] |= {(timestamp, droneId)}
        except KeyError:
            data[sourceMac] = {(timestamp, droneId)}

    print(time.time() - start)

    return data

def group_data(data, sort_index):
    sorted_data = sorted(data, key=lambda x: x[sort_index])

    return itertools.groupby(sorted_data, lambda x: x[sort_index])

def main():
    data = read_data()
    frequencies = []

    for key in data:
        grouped = group_data(data[key], 0)
        max_value = 0

        for group in grouped:
            counter = 0

            for row in group[1]:
                counter += 1

            if counter > max_value:
                max_value = counter

        frequencies.append(max_value)

    plt.hist(frequencies, bins=100)
    plt.show()

if __name__ == '__main__':
    main()
