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
        self._h = 1 / n

    def set_functions(self, u1: callable, u2: callable, f1: callable, f2: callable, k1: callable, k2: callable, q1: callable, q2: callable):
        self._u1 = u1
        self._u2 = u2
        self._f1 = f1
        self._f2 = f2
        self._k1 = k1
        self._k2 = k2
        self._q1 = q1
        self._q2 = q2

    def _calculate_integral(self, x_left: float, x_right: float, f: callable):
        result = 0.0
        h = self._h
        i = 0
        while(x_left + i * h < x_right):
            result += f(x_left + i * h) + f(x_left + (i + 1) * h)
            i += 1
        result *= h / 2
        return result

    def _calculate_ai(self, x_left: float, x_right: float):
        a_coef = 0.0
        if (x_left <= self._e <= x_right):
            a_coef += self._calculate_integral(x_left, self._e, self._k1)
            a_coef += self._calculate_integral(self._e, x_right, self._k2)
        if (x_right < self._e):
            a_coef = self._calculate_integral(x_left, x_right, self._k1)
        if (self._e < x_left):
            a_coef = self._calculate_integral(x_left, x_right, self._k2)
        a_coef /= self._h
        a_coef = 1.0 / a_coef
        return a_coef

    def _calculate_di(self, x_left: float, x_right: float):
        d_coef = 0.0
        if (x_left - self._h / 2 < self._e <= x_right + self._h / 2):
            d_coef += self._calculate_integral(x_left - self._h / 2, self._e, self._q1)
            d_coef += self._calculate_integral(self._e, x_right + self._h / 2, self._q2)
        if (x_right + self._h / 2 < self._e):
            d_coef = self._calculate_integral(x_left, x_right, self._q1)
        if (self._e < x_left - self._h / 2):
            d_coef = self._calculate_integral(x_left, x_right, self._q2)
        d_coef /= self._h
        return d_coef

    def _calculate_fi(self, x_left: float, x_right: float):
        f_coef = 0.0
        if (x_left - self._h / 2 < self._e <= x_right + self._h / 2):
            f_coef += self._calculate_integral(x_left - self._h / 2, self._e, self._f1)
            f_coef += self._calculate_integral(self._e, x_right + self._h / 2, self._f2)
        if (x_right + self._h / 2 < self._e):
            f_coef = self._calculate_integral(x_left, x_right, self._f1)
        if (self._e < x_left - self._h / 2):
            f_coef = self._calculate_integral(x_left, x_right, self._f2)
        f_coef /= self._h
        return f_coef
    
    def _create_vector(self):
        vector = np.zeros(shape=(self._n,))
        vector[0] = self._m1
        vector[self._n - 1] = self._m2
        for i in range(1, self._n - 1):
            vector[i] = -self._calculate_fi(self._h * i, self._h * (i + 1))
        return vector

    def _create_matrix(self):
        a_vec = np.zeros(shape=(self._n,))
        c_vec = np.zeros(shape=(self._n,))
        b_vec = np.zeros(shape=(self._n,))
        c_vec[0] = c_vec[self._n - 1] = 1

        for i in range(1, self._n - 1):
            ai_l = self._calculate_ai((i - 1) * self._h, i * self._h) / (self._h ** 2)
            ai_r = self._calculate_ai(i * self._h, (i + 1) * self._h) / (self._h ** 2)
            di = self._calculate_di(i * self._h, (i + 1) * self._h)
            a_vec[i - 1] = ai_l
            c_vec[i] = -(ai_l + ai_r + di)
            b_vec[i + 1] = ai_r
        return a_vec, c_vec, b_vec

    def _solve_matrix(self, a_vec: np.array, c_vec: np.array, b_vec: np.array, f: np.array):
        a = [0]
        b = [self._m1]

        for i in range(1, self._n - 1):
            ai = b_vec[i + 1] / (-c_vec[i] - a[i - 1] * a_vec[i - 1])
            bi = (-f[i] + b_vec[i + 1] * b[i - 1]) / (-c_vec[i] - a[i - 1] * a_vec[i - 1])

            a.append(ai)
            b.append(bi)

        x = np.zeros(shape=(self._n,))
        x[self._n - 1] = 1

        for i in range(self._n - 2, -1 , -1):
            x[i] = a[i] * x[i + 1] + b[i]
        return x

    def calculate(self):
        f = self._create_vector()
        a, c, b = self._create_matrix()
        x = self._solve_matrix(a, c, b, f)
        return x

    def calculate_e(self):
        result = np.zeros(shape=(self._n))
        for i in range(self._n):
            if (i * self._h < self._e):
                result[i] = self._u1(i * self._h)
            else:
                result[i] = self._u2(i * self._h)
        return result

test_func = [u1, u2, f1_test, f2_test, k1_test, k2_test, q1_test, q2_test]
main_func = [None, None, f1_main, f2_main, k1_main, k2_main, q1_main, q2_main]

def test_task(n: int):
    task1 = Task(0, 1, 0.4, 0, 1, n)
    task1.set_functions(*test_func)
    x1 = task1.calculate()
    x2 = task1.calculate_e()
    return x1, x2

def main_task(n: int):
    task1 = Task(0, 1, 0.4, 0, 1, n)
    task1.set_functions(*main_func)
    x1 = task1.calculate()

    task2 = Task(0, 1, 0.4, 0, 1, 2 * n)
    task2.set_functions(*main_func)
    x2 = task2.calculate()

    x3 = np.array([x2[i * 2] for i in range(n)])
    return x1, x3

def main():
    n = 100

    test_task(n)
    main_task(n)
    # e = task1.calculate_e(x1)
    # print(x1, e)
    # norm2 = np.linalg.norm(e - x1, ord=np.inf)
    # print(norm2)

if __name__ == "__main__":
    main()
