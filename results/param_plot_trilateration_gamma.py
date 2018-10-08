import numpy as np
import get_performance
import matplotlib.pyplot as plt

TIME_WINDOW = 60

def main():
    param_values = [i / 100 for i in range(0, 301, 5)]
    file_name = 'trilateration/results_trilateration_{}_{}.csv'
    results = []

    for param_value in param_values:
        results.append(
            get_performance.main(file_name.format(TIME_WINDOW, param_value), 'euc')
        )

    print(param_values[np.argmin(results)])


    plt.plot(param_values, results)
    plt.xlabel('Gamma')
    plt.ylabel('Average Euclidean Distance')
    plt.title('Parameter plot to determine the gamma for the trilateration method\n and a time window of {}'.format(TIME_WINDOW))
    plt.show()

if __name__ == '__main__':
    main()
