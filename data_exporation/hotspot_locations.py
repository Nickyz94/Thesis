import pandas as pd
import matplotlib.pyplot as plt

def read_data():
    data = pd.read_csv('/media/nickyz/Data/scriptie_data/Huawei_routers_locations_at_Arena/sensors_arena_sensation.csv')
    types = pd.read_csv('/media/nickyz/Data/scriptie_data/Huawei_routers_locations_at_Arena/AP_Info-2.csv', delimiter=';')
    return data.dropna(axis=0), types

def get_type(adres, type_data):
    adres = adres[:5] + '-' + adres[6:11] + '-' + adres[12:]
    adres = adres.replace(':', '')
    # print(type_data.columns)
    return type_data.loc[type_data['MAC'] == adres]['Name'].iloc[0][:6]

def get_location(adres, location_data):
    adres = adres.replace('-', ':')
    adres = adres[:2] + ':' + adres[2:7] + ':' + adres[7:12] + ':' + adres[12:]

    return location_data.loc[location_data['drone_id'] == adres]

def missing_aps(locations, types):
    counter = 0

    for _, ap in types.iterrows():
        loc = get_location(ap['MAC'], locations)

        if len(loc.index) == 0:
            counter += 1
            print(ap)

    print(counter)

def main():
    data, types = read_data()
    # for value in data['drone_id']:
    #     print(get_type(value, types))

    plt.scatter(data['x_m'], data['y_m'], s=data['z_m'])
    plt.show()

if __name__ == '__main__':
    main()
    # data, types = read_data()
    # missing_aps(data, types)
