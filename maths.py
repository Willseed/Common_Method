# -*- coding: utf-8 -*-
import math
import fire


class Maths(object):
    def pi(self, n):
        s = 0
        for i in range(n):
            s += 1 / (i + 1) / (i + 1)
        return math.sqrt(6 * s)

    def fact(self, n):
        s = 1
        for i in range(n):
            s *= i + 1
        return s


if __name__ == '__main__':
    fire.Fire(Maths)
