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


def make_normal_dist_2d_data(n=100):
    '''
    --- arg(s) ---
    n: int
        number of data
    '''
    x = np.random.randn(n)
    y = np.random.randn(n)
    data = np.array([x, y])
    np.savetxt(fname='../data/normal_dist_2d.txt', X=data)
    plt.scatter(x, y)
    plt.savefig('../fig/normal_dist_2d.png')


def make_2d_data():
    make_random_2d_data()
    make_normal_dist_2d_data()


def main():
    make_2d_data()


if __name__ == '__main__':
    main()
