import numpy as np

from utils.functions import bipstep
from utils.visualization import plot, line


def hebb_train(s, t, draw=False):
    w = np.zeros(len(s[0]) + 1)
    b = np.ones((len(s), 1))
    s = np.hstack((b, s))

    for r, row in enumerate(s):
        w = [w[i] + row[i] * t[r] for i in range(len(row))]

        print('Weight: {}'.format(w))

        if draw:
            plot(line(w, 0), s, t)

    return w


def hebb_test(x, w):
    y_in = w[0] + np.dot(x, w[1:])

    return bipstep(y_in)


if __name__ == '__main__':
    # AND
    train = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
    target = [1, -1, -1, -1]
    w = hebb_train(train, target, True)

    print(hebb_test([-1, -1], w))

    # OR
    train = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
    target = [1, 1, 1, -1]
    w = hebb_train(train, target, True)

    print(hebb_test([-1, -1], w))
