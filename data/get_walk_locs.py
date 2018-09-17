import pandas as pd
import matplotlib.pyplot as plt
import csv

def read_data():
    data = pd.read_csv('/media/nickyz/Data/scriptie_data/Huawei_routers_locations_at_Arena/sensors_arena_sensation.csv')
    walk = pd.read_csv('./toppers_walk.csv', delimiter=';')
    return data.dropna(axis=0), walk

def find_location(adres, drone_data):
    adres = adres.replace('-', ':')
    adres = adres[:2] + ':' + adres[2:7] + ':' + adres[7:12] + ':' + adres[12:]
    drone = drone_data.loc[drone_data['drone_id'] == adres]

    try:
        return drone.iloc[0]
    except IndexError:
        return None

def main():
    data, walk = read_data()

    fieldnames = ["time", "x_m", "y_m", "z_m"]

    with open('toppers_walk_locs.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for index, row in walk.iterrows():
            loc = find_location(row['ap_adres'], data)
            writer.writerow({"time": row["time"],
                             "x_m": loc["x_m"],
                             "y_m": loc["y_m"],
                             "z_m": loc["z_m"]})

    # plt.scatter(data['x_m'], data['y_m'], s=data['z_m'])
    # plt.show()

if __name__ == '__main__':
    main()
