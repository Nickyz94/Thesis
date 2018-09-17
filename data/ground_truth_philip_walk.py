import matplotlib.pyplot as plt
import pandas as pd

def read_router_data():
    data = pd.read_csv('/media/nickyz/Data/scriptie_data/Huawei_routers_locations_at_Arena/sensors_arena_sensation.csv')
    return data.dropna(axis=0)

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
    ground_truth.append(('11:35:00', *amsterdam72))
    ground_truth.append(('11:35:10', -35, 70))
    ground_truth.append(('11:37:00', 35, 70))
    ground_truth.append(('11:38:00', 70, 60))
    ground_truth.append(('11:38:50', *vak129))
    ground_truth.append(('11:39:00', *vak129tribune))
    ground_truth.append(('11:41:00', *vak129tribune))
    ground_truth.append(('11:41:10', *vak129))
    ground_truth.append(('11:42:00', *vak129tribune))
    ground_truth.append(('11:44:00', *vak129tribune))
    ground_truth.append(('11:44:10', *vak129))
    ground_truth.append(('11:44:35', 105, 25))
    ground_truth.append(('11:45:00', *vak127))
    ground_truth.append(('11:45:30', 105, -25))
    ground_truth.append(('11:46:00', *vak125))
    ground_truth.append(('11:47:00', *balkonfside))
    ground_truth.append(('11:50:00', *balkonfside))
    ground_truth.append(('11:50:10', *vak124))
    ground_truth.append(('11:51:05', 55, -70))
    ground_truth.append(('11:52:00', *vak120))
    ground_truth.append(('11:52:25', -60, -65))
    ground_truth.append(('11:52:50', *vak117))
    ground_truth.append(('11:53:00', *vak117tribune))
    ground_truth.append(('11:55:00', *vak117tribune))
    ground_truth.append(('11:55:10', *vak117))
    ground_truth.append(('11:56:05', -100, -30))
    ground_truth.append(('11:56:35', -105, 0))

    ground_truth.append(('11:57:00', *vak112))

    ground_truth.append(('11:58:50', *vak110))

    ground_truth.append(('11:59:00', *vak110tribune))
    ground_truth.append(('12:00:00', *vak110tribune))
    ground_truth.append(('12:00:10', -52, 63))
    ground_truth.append(('12:00:35', -20, 64))
    ground_truth.append(('12:01:00', *amsterdam72))

    return ground_truth

def main():
    ground_truth = create_ground_truth()

    date, x, y = zip(*ground_truth)

    router_data = read_router_data()
    plt.scatter(router_data['x_m'], router_data['y_m'])

    plt.plot(x, y, '-o', color='r')
    plt.show()


if __name__ == '__main__':
    main()
