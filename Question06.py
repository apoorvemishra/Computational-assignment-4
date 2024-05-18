import numpy as np
import matplotlib.pyplot as plt

b = np.sqrt(2/np.pi)

def target_distribution(x):
    return b * np.exp(-x**2 / 2)


# Number of samples
num_samples = 10000
samples = []
while len(samples)<num_samples:
    x = np.random.rand()*5
    y = np.random.rand()*b
    if y<target_distribution(x): samples.append(x)
    


# Plotting the density histogram
plt.figure(figsize=(10, 6))
plt.hist(samples, bins=100, density=True, alpha=0.6, edgecolor='black')

# Plotting the target distribution for comparison
x = np.linspace(0, 5, 1000)
plt.plot(x, target_distribution(x), 'r-', lw=2, label='Target Distribution $f(x)$')

plt.title('Density Histogram of Rejection Sampling Generated Numbers')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()
