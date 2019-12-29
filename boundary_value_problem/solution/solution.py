import numpy as np
from math import exp, sqrt

def u1(x: float):
    return 0.06055722 * exp(sqrt(2 / 7) * x) - 1.06055722 * exp(-1 * sqrt(2 / 7) * x) + 1

def u2(x: float):
    return -0.47202455 * exp(sqrt(0.4) * x) - 4.33108482 * exp(-1 * sqrt(0.4) * x) + exp(-1 * 0.4) / 0.16

def f1_test(x: float):
    return 0.4

def f2_test(x: float):
    return exp(-0.4)

def k1_test(x: float):
    return 1 / 1.4

def k2_test(x: float):
    return 1 / 0.4

def q1_test(x: float):
    return 0.4

def q2_test(x: float):
    return 0.16

def f1_main(x: float):
    return x

def f2_main(x: float):
    return exp(-x)

def k1_main(x: float):
    return 1 / (x + 1)

def k2_main(x: float):
    return 1 / x

def q1_main(x: float):
    return x

def q2_main(x: float):
    return x ** 2

class Task:
    def __init__(self, x0: float, xn: float, e: float, u0: float, un: float, n: int):
        self._m1 = u0
        self._m2 = un
        self._x0 = x0
        self._xn = xn
        self._e = e
        self._n = n
        self._h = xn / n

    def set_functions(self, u1: callable, u2: callable, k1: callable, k2: callable, q1: callable, q2: callable, f1: callable, f2: callable):
        self._u1 = u1
        self._u2 = u2
        self._k1 = k1
        self._k2 = k2
        self._q1 = q1
        self._q2 = q2
        self._f1 = f1
        self._f2 = f2

    def _calculate_integral(self, x_left: float, x_right: float, f: callable):
        if (x_left == x_right): return 0.0
        return f((x_left + x_right) / 2) * (x_right - x_left)

    def _calculate_ai(self, x_i: float):
        x_left = x_i - self._h
        x_right = x_i
        if (x_right <= self._e):
            a_coef = self._calculate_integral(x_left, x_right, self._k1)
        if (self._e <= x_left):
            a_coef = self._calculate_integral(x_left, x_right, self._k2)
        if (x_left < self._e < x_right):
            a_coef = 0.0
            a_coef += self._calculate_integral(x_left, self._e, self._k1)
            a_coef += self._calculate_integral(self._e, x_right, self._k2)
        a_coef /= self._h
        a_coef = 1.0 / a_coef
        return a_coef

    def _calculate_di(self, x_i: float):
        x_left = x_i - (self._h / 2)
        x_right = x_i + (self._h / 2)
        if x_right <= self._e:
            d_coef = self._calculate_integral(x_left, x_right, self._q1)
        if self._e <= x_left:
            d_coef = self._calculate_integral(x_left, x_right, self._q2)
        if x_left < self._e < x_right:
            d_coef = 0.0
            d_coef += self._calculate_integral(x_left, self._e, self._q1)
            d_coef += self._calculate_integral(self._e, x_right, self._q2)
        d_coef /= self._h
        return d_coef

    def _calculate_fi(self, x_i: float):
        x_left = x_i - (self._h / 2)
        x_right = x_i + (self._h / 2)
        if x_right <= self._e:
            f_coef = self._calculate_integral(x_left, x_right, self._f1)
        if self._e <= x_left:
            f_coef = self._calculate_integral(x_left, x_right, self._f2)
        if x_left < self._e < x_right:
            f_coef = 0.0
            f_coef += self._calculate_integral(x_left, self._e, self._f1)
            f_coef += self._calculate_integral(self._e, x_right, self._f2)
        f_coef /= self._h
        return f_coef
    
    def _create_vector(self):
        vector = np.zeros(shape=(self._n + 1,))
        vector[0] = self._m1
        vector[self._n] = self._m2
        for i in range(1, self._n):
            vector[i] = self._calculate_fi(self._h * i)
        return vector

    def _create_matrix(self):
        a_vec = np.zeros(shape=(self._n + 1,))
        c_vec = np.zeros(shape=(self._n + 1,))
        b_vec = np.zeros(shape=(self._n + 1,))
        c_vec[0] = c_vec[self._n] = 1

        for i in range(1, self._n):
            ai_l = self._calculate_ai(i * self._h) / (self._h ** 2)
            ai_r = self._calculate_ai((i + 1) * self._h) / (self._h ** 2)
            di = self._calculate_di(i * self._h)
            a_vec[i] = ai_l
            c_vec[i] = ai_l + ai_r + di
            b_vec[i] = ai_r
        return a_vec, c_vec, b_vec

    def _solve_matrix(self, a_vec: np.array, c_vec: np.array, b_vec: np.array, f: np.array):
        a = [0, 0]
        b = [0, self._m1]

        for i in range(1, self._n):
            ai = b_vec[i] / (c_vec[i] - a_vec[i] * a[i])
            bi = (f[i] + a_vec[i] * b[i]) / (c_vec[i] - a_vec[i] * a[i])
            a.append(ai)
            b.append(bi)

        x = np.zeros(shape=(self._n + 1,))

        x[self._n] = self._m2
        for i in range(self._n - 1, -1 , -1):
            x[i] = a[i + 1] * x[i + 1] + b[i + 1]
        return x

    def calculate(self):
        f = self._create_vector()
        a, c, b = self._create_matrix()
        x = self._solve_matrix(a, c, b, f)
        return x

    def calculate_e(self):
        result = np.zeros(shape=(self._n + 1))
        for i in range(self._n + 1):
            if (i * self._h <= self._e):
                result[i] = self._u1(i * self._h)
            if (self._e < i * self._h):
                result[i] = self._u2(i * self._h)
        return result

test_func = [u1, u2, k1_test, k2_test, q1_test, q2_test, f1_test, f2_test]
main_func = [None, None, k1_main, k2_main, q1_main, q2_main, f1_main, f2_main]

def test_task(n: int):
    x = np.array([i / n for i in range(n + 1)])
    task1 = Task(0, 1, 0.4, 0, 1, n)
    task1.set_functions(*test_func)
    v = task1.calculate()
    u = task1.calculate_e()
    return x, v, u

def main_task(n: int):
    x = np.array([i / n for i in range(n + 1)])
    task1 = Task(0, 1, 0.4, 0, 1, n)
    task1.set_functions(*main_func)
    v = task1.calculate()

    task2 = Task(0, 1, 0.4, 0, 1, 2 * n)
    task2.set_functions(*main_func)
    v2n = task2.calculate()

    v2 = np.zeros(shape=(n + 1,))
    v2[0] = 0
    for i in range(1, n):
        v2[i] = v2n[i * 2]
    v2[n] = 1
    return x, v, v2

def main():
    n = 100
    test_task(n)
    main_task(n)

if __name__ == "__main__":
    main()
