from math import exp, sin
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

class GeoBrownian:
    def __init__(self, delta_t = 1, mu = 0, sigma = 1, n = 1000, S_0=1):
        self.delta_t = delta_t
        self.mu = mu
        self.sigma = sigma
        self.n = n
        self.S_0 = S_0
        B = Brownian(delta_t=self.delta_t, mu=self.mu - (self.sigma**2) / 2, sigma=self.sigma, n=self.n)
        self.range = [self.S_0 * exp(b) for b in B.range]
        # I don't know right now, it's weird

class SineBrownian:
    def __init__(self, delta_t = 1, mu = 0, sigma = 1, n = 1000, S_0 = 1):
        self.delta_t = delta_t
        self.mu = mu
        self.sigma = sigma
        self.n = n
        self.S_0 = S_0
        self.range = []
        B = Brownian(delta_t=self.delta_t, mu=self.mu, sigma=self.sigma, n=self.n)
        for i in range(len(B.range)):
            self.range.append(self.S_0 * exp(sigma**2 / 2 * delta_t * i) * sin(B.range[i]))

B = SineBrownian(delta_t=1, mu=1, sigma=1, n=1000)
plt.plot(B.range)
plt.show()


