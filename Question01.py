import time
import numpy as np
import matplotlib.pyplot as plt

class LinearCongruentialGenerator:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.current = seed

    def next(self):
        self.current = (self.a * self.current + self.c) % self.m
        return self.current

    def random(self):
        return self.next() / self.m

# Timing the LCG
lcg = LinearCongruentialGenerator(seed=42)
start_time = time.time()
random_numbers_lcg = [lcg.random() for _ in range(10000)]
lcg_time = time.time() - start_time

# Plotting the density histogram
plt.figure(figsize=(10, 6))
plt.hist(random_numbers_lcg, bins=100, density=True, alpha=0.6, color='g', edgecolor='black')

# Plotting the uniform PDF for comparison
x = np.linspace(0, 1, 100)
uniform_pdf = np.ones_like(x)  # PDF of the uniform distribution is constant (1) between 0 and 1
plt.plot(x, uniform_pdf, 'r-', lw=2, label='Uniform PDF')

plt.title('Density Histogram of LCG Generated Numbers')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()

print(f"Time taken by LCG to generate 10,000 numbers: {lcg_time:.6f} seconds")
