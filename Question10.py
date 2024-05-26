import numpy as np
import emcee
import requests
import matplotlib.pyplot as plt
import corner

# Load data
url = "https://theory.tifr.res.in/~kulkarni/data.txt"
response = requests.get(url)
data = response.text.split('\n')

# Extract columns
x = []
y = []
sigma = []
for line in data:
    if line.strip() != '' and line[0] != 'C':
        k, xi, yi, si = map(float, line.split())
        x.append(xi)
        y.append(yi)
        sigma.append(si)
x = np.array(x)
y = np.array(y)
sigma = np.array(sigma)

# Define the model
def model(theta, x):
    a, b, c = theta
    return a * x**2 + b * x + c

# Define the log likelihood
def log_likelihood(theta, x, y, sigma):
    model_y = model(theta, x)
    return -0.5 * np.sum(((y - model_y) / sigma) ** 2)

# Define the log prior
def log_prior(theta):
    a, b, c = theta
    if -10 < a < 10 and -10 < b < 10 and -10 < c < 10:
        return 0.0
    return -np.inf

# Define the log posterior
def log_posterior(theta, x, y, sigma):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, x, y, sigma)

# Initial guess for the parameters
initial = np.array([1.0, 1.0, 1.0])
nwalkers = 50
ndim = len(initial)
pos = initial + 1e-4 * np.random.randn(nwalkers, ndim)

# Set up the MCMC sampler
sampler = emcee.EnsembleSampler(nwalkers, ndim, log_posterior, args=(x, y, sigma))

# Run the MCMC sampler
nsteps = 4000
sampler.run_mcmc(pos, nsteps)

# Get the samples
samples = sampler.get_chain(discard=1000, thin=15, flat=True)

# Print out the results
fig = corner.corner(samples, labels=["a", "b", "c"], truths=[np.mean(samples[:, i]) for i in range(ndim)])
plt.show()

# Extract the best-fit parameters
a_mcmc, b_mcmc, c_mcmc = np.mean(samples, axis=0)
print(f"Best-fit parameters:\n a = {a_mcmc}\n b = {b_mcmc}\n c = {c_mcmc}")


# Randomly choose 200 sets of parameters from the posterior
random_indices = np.random.choice(samples.shape[0], size=200, replace=False)
random_samples = samples[random_indices]

# Plot the data
plt.errorbar(x, y, yerr=sigma, fmt='o', color='b', label='Data')

# Plot the best-fit model
x_model = np.linspace(min(x), max(x), 100)
y_model = model([a_mcmc, b_mcmc, c_mcmc], x_model)
plt.plot(x_model, y_model, color='r', label='Best-fit Model')

# Plot 200 models randomly chosen from the posterior
for params in random_samples:
    y_model_random = model(params, x_model)
    plt.plot(x_model, y_model_random, color='k', alpha=0.1)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Data with Best-fit Model and 200 Random Models from Posterior')
plt.legend()
plt.grid(True)
plt.show()
