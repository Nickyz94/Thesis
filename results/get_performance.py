import numpy as np
import numpy.linalg as LA
import csv
import time
import datetime

def euclidean(est, real):
    return LA.norm(est - real)

def squared_euclidean(est, real):
    return LA.norm(est - real)**2

def manhatten(est, real):
    return LA.norm(est - real, ord=1)

def create_ground_truth():
    vak129tribune = (81.5, 36)
    vak129 = (91, 42)
    vak127 = (105, 0)
    vak125 = (97, -42)
    balkonfside = (80, -45)
    vak124 = (80, -60)
    vak120 = (-10, -70)
    vak117 = (-75, -55)
    vak117tribune = (-69, -46)
    vak112 = (-95, 42)
    vak110 = (-67, 64)
    vak110tribune = (-65, 55)
    amsterdam72 = (-20, 72)

    ground_truth = []
    ground_truth.append(('11:35:00', amsterdam72))
    ground_truth.append(('11:35:10', (-35, 70)))
    ground_truth.append(('11:37:00', (35, 70)))
    ground_truth.append(('11:38:00', (70, 60)))
    ground_truth.append(('11:38:50', vak129))
    ground_truth.append(('11:39:00', vak129tribune))
    ground_truth.append(('11:41:00', vak129tribune))
    ground_truth.append(('11:41:10', vak129))
    ground_truth.append(('11:42:00', vak129tribune))
    ground_truth.append(('11:44:00', vak129tribune))
    ground_truth.append(('11:44:10', vak129))
    ground_truth.append(('11:44:35', (105, 25)))
    ground_truth.append(('11:45:00', vak127))
    ground_truth.append(('11:45:30', (105, -25)))
    ground_truth.append(('11:46:00', vak125))
    ground_truth.append(('11:47:00', balkonfside))
    ground_truth.append(('11:50:00', balkonfside))
    ground_truth.append(('11:50:10', vak124))
    ground_truth.append(('11:51:05', (55, -70)))
    ground_truth.append(('11:52:00', vak120))
    ground_truth.append(('11:52:25', (-60, -65)))
    ground_truth.append(('11:52:50', vak117))
    ground_truth.append(('11:53:00', vak117tribune))
    ground_truth.append(('11:55:00', vak117tribune))
    ground_truth.append(('11:55:10', vak117))
    ground_truth.append(('11:56:05', (-100, -30)))
    ground_truth.append(('11:56:35', (-105, 0)))

    ground_truth.append(('11:57:00', vak112))

    ground_truth.append(('11:58:50', vak110))

    ground_truth.append(('11:59:00', vak110tribune))
    ground_truth.append(('12:00:00', vak110tribune))
    ground_truth.append(('12:00:10', (-52, 63)))
    ground_truth.append(('12:00:35', (-20, 64)))
    ground_truth.append(('12:01:00', amsterdam72))

    return ground_truth

def find_ground_truth(est, ground_truth_dict):
    try:
        return np.array(ground_truth_dict[est[0]])
    except KeyError:
        pass

    keys = ground_truth_dict.keys()

    try:
        prev_stamp = max(filter(lambda x: x < est[0], keys))
        next_stamp = min(filter(lambda x: x > est[0], keys))
    except ValueError:
        return

    prev_loc = ground_truth_dict[prev_stamp]
    next_loc = ground_truth_dict[next_stamp]

    x_grad = (next_loc[0] - prev_loc[0]) / (next_stamp - prev_stamp)
    y_grad = (next_loc[1] - prev_loc[1]) / (next_stamp - prev_stamp)

    truth_x = prev_loc[0] + x_grad * (est[0] - prev_stamp)
    truth_y = prev_loc[1] + y_grad * (est[0] - prev_stamp)

    return np.array([truth_x, truth_y])

def main(datafile, measure):
    if measure == 'euc':
        method = euclidean
    elif measure == 'sq_euc':
        method = squared_euclidean
    elif measure == 'man':
        method = manhatten
    else:
        print("Measure must be either 'euc', 'sq_euc' or 'man'")
        return

    ests = []

    with open(datafile, 'r') as f:
        reader = csv.DictReader(f, delimiter=';')

        for row in reader:
            stamp = float(row['timestamp'])
            ests.append((stamp, np.array([float(row['x_m']), float(row['y_m'])])))

    ground_truth = create_ground_truth()

    ground_truth_dict = {}
    for spot in ground_truth:
        stamp = time.mktime(datetime.datetime.strptime('2018-02-08 ' + spot[0],
                                                       "%Y-%m-%d %H:%M:%S").timetuple())
        ground_truth_dict[stamp] = spot[1]

    dists = []

    for est in ests:
        truth = find_ground_truth(est, ground_truth_dict)

        if truth is not None:
            dists.append(method(est[1], truth))

    return sum(dists) / len(dists)
