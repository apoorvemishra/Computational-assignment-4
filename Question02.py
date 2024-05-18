import time
import numpy as np
import matplotlib.pyplot as plt

# Timing np.random.rand()
start_time = time.time()
random_numbers_np = np.random.rand(10000)
np_time = time.time() - start_time

# Plotting the density histogram
plt.figure(figsize=(10, 6))
plt.hist(random_numbers_np, bins=100, density=True, alpha=0.6, color='g', edgecolor='black')

# Plotting the uniform PDF for comparison
x = np.linspace(0, 1, 100)
uniform_pdf = np.ones_like(x)  # PDF of the uniform distribution is constant (1) between 0 and 1
plt.plot(x, uniform_pdf, 'r-', lw=2, label='Uniform PDF')

plt.title('Density Histogram of np.random.rand() Generated Numbers')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()

print(f"Time taken by np.random.rand() to generate 10,000 numbers: {np_time:.6f} seconds")
