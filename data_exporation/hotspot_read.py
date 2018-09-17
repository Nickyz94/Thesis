import csv
import glob
import matplotlib.pyplot as plt
import datetime
import itertools
import fileinput
import json
import time
import numpy as np

column_mapping = {
    'wifimeasurement_v2.value': 'wifimeasurement.value',
    'wifimeasurement_v2.version': 'wifimeasurement.version',
    'wifimeasurement_v2.measurementtimestamp': 'wifimeasurement.measurementtimestamp',
    'wifimeasurement_v2.processingtimestamp': 'wifimeasurement.processingtimestamp',
    'wifimeasurement_v2.application': 'wifimeasurement.application',
    'wifimeasurement_v2.date': 'wifimeasurement.date'
}

def read_data():
    start = time.time()
    data = {}
    files = glob.glob('/media/nickyz/Data/scriptie_data/armin/20170512_[1-5].csv')
    files.reverse()
    for line in fileinput.input(files=files):
        if fileinput.isfirstline():
            print(time.time() - start)
            print(fileinput.filename())
            continue

        """
        #     wifimeasurement.value (+)
        #     wifimeasurement.version
        #     wifimeasurement.measurementtimestamp (+)
        #     wifimeasurement.processingtimestamp
        #     wifimeasurement.application
        #     wifimeasurement.date
        #     """
        splitted = line.split('\t')

        timestamp = splitted[2]
        timestamp = datetime.datetime.fromtimestamp(int(timestamp[0:-3])).strftime('%Y-%m-%d %H:%M')

        """
        #         0 -> sourcemac (+)
        #         1 -> droneid (+)
        #         2 -> typenr
        #         3 -> signal (+)
        #         4 -> localmac (0 -> valuable, 1 -> not important)
        #         5 -> seqnr
        #         6 -> retryflag
        #         7 -> subtypenr
        #         """
        values = json.loads(splitted[0])

        try:
            localMac = int(values['localMac'])
        except KeyError:
            localMac = int(values['localmac'])

        if(localMac):
            continue

        try:
            sourceMac = values['sourceMac']
        except KeyError:
            sourceMac = values['sourcemac']

        # try:
        #     droneId = values['droneId']
        # except KeyError:
        #     droneId = values['droneid']

        try:
            data[timestamp] |= {sourceMac}
        except KeyError:
            data[timestamp] = {sourceMac}

        # data.append([timestamp, sourceMac, droneId, values['signal']])

    return data

def group_data(data, sort_index):
    sorted_data = sorted(data, key=lambda x: x[sort_index])

    return itertools.groupby(sorted_data, lambda x: x[sort_index])

def main():
    data = read_data()
    # grouped_data = group_data(data, 0)

    labels = []
    counts = []

    for key, value in data.items():
        # connections = 0
        # for subrow in group_data(row[1], 2):
            # connections += 1
        # outcomes.append(connections)
        labels.append(key)
        counts.append(len(value))

    y_pos = np.arange(len(labels))
    sorted_counts = [x for _, x in sorted(zip(labels, counts))]

    # plt.bar(y_pos, counts, alpha=0.5)
    plt.plot(counts)
    # plt.xticks(y_pos, labels)
    plt.ylabel("Number of AP's with a connection")
    # plt.plot(outcomes)
    plt.show()

if __name__ == '__main__':
    main()
