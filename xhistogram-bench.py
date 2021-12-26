"""

n numpy xhistogram
1 0.0006265687919221819 0.0007165344804525376
10 0.005039609561208636 0.0031582056009210645
50 0.025540791330859066 0.01860524701885879
200 0.11167568020056934 0.09127700285054743
800 0.5745104460907169 0.3756942337495275
3000 2.0705310765490865 1.5305814586603084
"""



import xarray as xr
import xhistogram.xarray as xh
import numpy as np
from timeit import timeit


def main():
    test(1)
    test(10)
    test(50)
    test(200)
    test(800)
    test(3000)


def test(n):
    data = np.random.random((n, 10000))
    bins = np.linspace(0, 1, 20)
    np_hist_bench = bench(lambda: np_hist(data, bins))
    x_hist_bench = bench(lambda: x_hist(data, bins))
    print(n, np_hist_bench, x_hist_bench)


def bench(f):
    number = 100
    return timeit(f, number=number)/number


def np_hist(data, bins):
    res = np.zeros((data.shape[0], bins.shape[0]-1))
    for i, row in enumerate(data):
        res[i] = np.histogram(row, bins=bins)[0]
    return res


def x_hist(data, bins):
    data_arr = xr.DataArray(data, dims=["a", "b"], name="aaa")
    res = xh.histogram(data_arr, bins=bins, dim="b")
    return res.data


if __name__ == "__main__":
    main()
