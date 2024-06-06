#StatsTODO 
# some functions
Certainly! Maximum Likelihood Estimation (MLE) is a method for estimating the parameters of a statistical model. The goal is to find the parameter values that maximize the likelihood function given the observed data.

Here are Python functions for computing MLE for a couple of common distributions: the normal distribution and the exponential distribution. We'll use the `scipy.optimize` library to maximize the likelihood function.

### MLE for Normal Distribution

For a normal distribution, we need to estimate the mean (\(\mu\)) and standard deviation (\(\sigma\)).

```python
import numpy as np
from scipy.optimize import minimize

def normal_log_likelihood(params, data):
    mu, sigma = params[0], params[1]
    n = len(data)
    likelihood = -n/2 * np.log(2 * np.pi * sigma**2) - np.sum((data - mu)**2) / (2 * sigma**2)
    return -likelihood  # Negative because we minimize in scipy

def normal_mle(data):
    # Initial guesses for mu and sigma
    initial_params = [np.mean(data), np.std(data)]
    result = minimize(normal_log_likelihood, initial_params, args=(data,), bounds=((None, None), (1e-6, None)))
    mu_mle, sigma_mle = result.x
    return mu_mle, sigma_mle

# Example usage
data = np.random.normal(loc=5, scale=2, size=100)  # Generate some sample data
mu_mle, sigma_mle = normal_mle(data)
print(f"MLE for Normal Distribution: mu = {mu_mle}, sigma = {sigma_mle}")
```

### MLE for Exponential Distribution

For an exponential distribution, we need to estimate the rate parameter (\(\lambda\)).

```python
def exponential_log_likelihood(params, data):
    lambd = params[0]
    n = len(data)
    likelihood = n * np.log(lambd) - lambd * np.sum(data)
    return -likelihood  # Negative because we minimize in scipy

def exponential_mle(data):
    # Initial guess for lambda
    initial_params = [1 / np.mean(data)]
    result = minimize(exponential_log_likelihood, initial_params, args=(data,), bounds=((1e-6, None),))
    lambd_mle = result.x[0]
    return lambd_mle

# Example usage
data = np.random.exponential(scale=2, size=100)  # Generate some sample data
lambda_mle = exponential_mle(data)
print(f"MLE for Exponential Distribution: lambda = {lambda_mle}")
```

### Explanation:

1. **Log-Likelihood Functions**:
   - `normal_log_likelihood`: Calculates the log-likelihood for a normal distribution.
   - `exponential_log_likelihood`: Calculates the log-likelihood for an exponential distribution.

2. **MLE Functions**:
   - `normal_mle`: Uses `scipy.optimize.minimize` to find the MLE for the mean (\(\mu\)) and standard deviation (\(\sigma\)) of a normal distribution.
   - `exponential_mle`: Uses `scipy.optimize.minimize` to find the MLE for the rate parameter (\(\lambda\)) of an exponential distribution.

3. **Initial Guesses**:
   - For the normal distribution, the initial guesses are the sample mean and standard deviation.
   - For the exponential distribution, the initial guess is the inverse of the sample mean.

4. **Bounds**:
   - For the normal distribution, the standard deviation (\(\sigma\)) is constrained to be positive.
   - For the exponential distribution, the rate parameter (\(\lambda\)) is constrained to be positive.

### Example Usage:

- Generate sample data for both normal and exponential distributions.
- Compute the MLEs using the respective functions.
- Print the results.

These functions provide a general framework for MLE, which can be adapted to other distributions and more complex models by defining the appropriate likelihood functions and parameter constraints.


### MLE for Poisson Distribution

For a Poisson distribution, we need to estimate the rate parameter (\(\lambda\)).

```python
import numpy as np
from scipy.optimize import minimize

def poisson_log_likelihood(params, data):
    lambd = params[0]
    likelihood = np.sum(data * np.log(lambd) - lambd - np.log(np.arange(1, data.max() + 1)).cumsum()[data-1])
    return -likelihood  # Negative because we minimize in scipy

def poisson_mle(data):
    # Initial guess for lambda
    initial_params = [np.mean(data)]
    result = minimize(poisson_log_likelihood, initial_params, args=(data,), bounds=((1e-6, None),))
    lambd_mle = result.x[0]
    return lambd_mle

# Example usage
data = np.random.poisson(lam=3, size=100)  # Generate some sample data
lambda_mle = poisson_mle(data)
print(f"MLE for Poisson Distribution: lambda = {lambda_mle}")
```

### MLE for Bernoulli Distribution

For a Bernoulli distribution, we need to estimate the success probability (\(p\)).

```python
def bernoulli_log_likelihood(params, data):
    p = params[0]
    n = len(data)
    likelihood = np.sum(data * np.log(p) + (1 - data) * np.log(1 - p))
    return -likelihood  # Negative because we minimize in scipy

def bernoulli_mle(data):
    # Initial guess for p
    initial_params = [np.mean(data)]
    result = minimize(bernoulli_log_likelihood, initial_params, args=(data,), bounds=((1e-6, 1 - 1e-6),))
    p_mle = result.x[0]
    return p_mle

# Example usage
data = np.random.binomial(n=1, p=0.6, size=100)  # Generate some sample data
p_mle = bernoulli_mle(data)
print(f"MLE for Bernoulli Distribution: p = {p_mle}")
```

### MLE for Gamma Distribution

For a Gamma distribution, we need to estimate the shape parameter (\(\alpha\)) and the scale parameter (\(\beta\)).

```python
def gamma_log_likelihood(params, data):
    alpha, beta = params
    n = len(data)
    likelihood = n * alpha * np.log(beta) - n * np.log(np.math.gamma(alpha)) + (alpha - 1) * np.sum(np.log(data)) - beta * np.sum(data)
    return -likelihood  # Negative because we minimize in scipy

def gamma_mle(data):
    # Initial guesses for alpha and beta
    mean = np.mean(data)
    var = np.var(data)
    initial_params = [mean**2 / var, mean / var]
    result = minimize(gamma_log_likelihood, initial_params, args=(data,), bounds=((1e-6, None), (1e-6, None)))
    alpha_mle, beta_mle = result.x
    return alpha_mle, beta_mle

# Example usage
data = np.random.gamma(shape=2, scale=2, size=100)  # Generate some sample data
alpha_mle, beta_mle = gamma_mle(data)
print(f"MLE for Gamma Distribution: alpha = {alpha_mle}, beta = {beta_mle}")
```

### Explanation:

1. **Log-Likelihood Functions**:
   - `poisson_log_likelihood`: Calculates the log-likelihood for a Poisson distribution.
   - `bernoulli_log_likelihood`: Calculates the log-likelihood for a Bernoulli distribution.
   - `gamma_log_likelihood`: Calculates the log-likelihood for a Gamma distribution.

2. **MLE Functions**:
   - `poisson_mle`: Uses `scipy.optimize.minimize` to find the MLE for the rate parameter (\(\lambda\)) of a Poisson distribution.
   - `bernoulli_mle`: Uses `scipy.optimize.minimize` to find the MLE for the success probability (\(p\)) of a Bernoulli distribution.
   - `gamma_mle`: Uses `scipy.optimize.minimize` to find the MLE for the shape (\(\alpha\)) and scale (\(\beta\)) parameters of a Gamma distribution.

3. **Initial Guesses**:
   - For the Poisson distribution, the initial guess is the sample mean.
   - For the Bernoulli distribution, the initial guess is the sample mean.
   - For the Gamma distribution, the initial guesses are derived from the sample mean and variance.

4. **Bounds**:
   - For all distributions, parameters are constrained to be positive to ensure valid parameter values.

5. **Example Usage**:
   - Generate sample data for each distribution.
   - Compute the MLEs using the respective functions.
   - Print the results.

These functions provide a template for MLE of various distributions and can be adapted to other distributions by defining the appropriate likelihood functions and parameter constraints.
# Example Exponential Distribution
## Code


## Problem
An alternative way of defining the exponential distribution is: $f(x;\beta)=\frac{1}{\beta}e^{-x/\beta}$
1) Obtain the expression for the maximum likelihood estimator (MLE) for $\beta$
2) Is the MLE that you calculated consistent? Provide the necessary equations to support your answer
