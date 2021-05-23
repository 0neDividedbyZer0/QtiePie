from math import exp
import random as r
import matplotlib.pyplot as plt

class Brownian:
    def __init__(self, delta_t=1, mu = 0, sigma = 1, n=1000):
        self.delta_t = delta_t
        self.mu = mu
        self.sigma = sigma
        self.n = n

        self.range = [0]
        for i in range(n):
            delta_B = r.gauss(mu * delta_t, (sigma ** 2) * self.delta_t)
            self.range.append(self.range[i] + delta_B )


B = Brownian(mu=0, sigma=1)
plt.plot(B.range)
plt.show()


