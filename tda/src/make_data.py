import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')


def make_random_2d_data(n=100):
    '''
    --- arg(s) ---
    n: int
        number of data
    '''
    x = np.random.rand(n)
    y = np.random.rand(n)
    data = np.array([x, y])
    np.savetxt(fname='../data/random_2d.txt', X=data)
    plt.scatter(x, y)
    plt.savefig('../fig/random_2d.png')


def main():
    make_random_2d_data()


if __name__ == '__main__':
    main()
