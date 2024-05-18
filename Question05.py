import numpy as np
import matplotlib.pyplot as plt


def box_muller_transform(u1, u2):
    """ Apply the Box-Muller transform to generate two standard normal random variables """
    z0 = np.sqrt(-2.0 * np.log(u1)) * np.cos(2.0 * np.pi * u2)
    z1 = np.sqrt(-2.0 * np.log(u1)) * np.sin(2.0 * np.pi * u2)
    return z0, z1

# Generate 10,000 uniform random numbers
num_samples = 10000
u1 = np.random.rand(num_samples // 2)
u2 = np.random.rand(num_samples // 2)

# Apply Box-Muller transform
z0, z1 = box_muller_transform(u1, u2)

# Combine the two sets of numbers
gaussian_numbers = np.concatenate((z0, z1))

# Plotting the density histogram
plt.figure(figsize=(10, 6))
plt.hist(gaussian_numbers, bins=100, density=True, alpha=0.6, color='g', edgecolor='black')

# Plotting the Gaussian PDF for comparison
x = np.linspace(-4, 4, 100)
gaussian_pdf = (1/np.sqrt(2*np.pi)) * np.exp(-0.5 * x**2)  # Manual calculation of Gaussian PDF
plt.plot(x, gaussian_pdf, 'r-', lw=2, label='Gaussian PDF')

plt.title('Density Histogram of Box-Muller Generated Numbers')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()
