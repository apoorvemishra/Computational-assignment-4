import numpy as np
import matplotlib.pyplot as plt

def uniform_density(x):
    if 3 < x < 7:
        return 1 / (7 - 3)
    else:
        return 0

def metropolis_sampling(n_samples, initial, step_size):
    samples = [initial]
    current = initial

    for _ in range(n_samples - 1):
        proposal = current + np.random.uniform(-step_size, step_size)
        acceptance_ratio = uniform_density(proposal) / uniform_density(current)
        
        if acceptance_ratio >= 1 or np.random.rand() < acceptance_ratio:
            current = proposal
        
        samples.append(current)
    
    return np.array(samples)

# Parameters
n_samples = 10000
initial = 5.0
step_size = 1.0

# Generate samples
samples = metropolis_sampling(n_samples, initial, step_size)

# Plotting the Markov Chain
plt.figure(figsize=(10, 6))
plt.plot(samples, lw=0.5, alpha=0.8)
plt.title('Markov Chain using Metropolis Algorithm')
plt.xlabel('Iteration')
plt.ylabel('Sample value')
plt.grid(True)
#plt.show()

# Plotting the density histogram
plt.figure(figsize=(8, 4))
plt.hist(samples, bins=40, density=True, alpha=0.6, color='g', edgecolor='black')

# Plotting the expected uniform density
x = np.linspace(2.5, 7.5, 1000)
y = [uniform_density(xi) for xi in x]
plt.plot(x, y, 'r-', lw=2, label='Expected Uniform Density')

plt.title('Density Histogram of Samples')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
