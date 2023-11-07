from multiprocessing import Pool


def f(x):
    return x*x


if __name__ == '__main__':
    with Pool(10) as p:
        result = p.map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(result)