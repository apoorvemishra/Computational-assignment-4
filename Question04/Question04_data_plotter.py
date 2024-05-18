import numpy as np
import matplotlib.pyplot as plt

# Load the data from the file
data = np.loadtxt('exponential_data.txt')


# Create the density histogram
plt.hist(data, bins=50, density=True, alpha=0.6, color='g', label='Generated Data')

# Plot the exponential PDF
mean = 0.5
lambda_param = 1 / mean
x = np.linspace(0, max(data), 1000)
pdf = lambda_param * np.exp(-lambda_param * x)
plt.plot(x, pdf, 'r', label='Exponential PDF (mean=0.5)')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Histogram and Exponential PDF')
plt.legend()

# Show the plot
plt.show()
