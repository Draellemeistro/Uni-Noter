See also [[Poisson process]]
> [!NOTE] Poisson: What for?
> One of the applications of the **Poisson probabilities** is ==*to approximate*== the **binomial probabilities** – when $n$ is large and $p$ is small. $$\lambda=np$$

A r.v. taking on one of values 0, 1, 2, … is said to be a **Poisson** r.v. with parameter $λ$: (λ>0), if [[Probability Mass Function (PMF)]] is given by: $$P(X=i)=e^λ *\frac{λ^i}{i!}$$
**Moment generating function:** $$E[e^{tX}] = e^{λ(e^t - 1)}$$
## Expectance and Variance:
- $E[X]=\lambda$
- $Var(X)=\lambda$

## Events that can be moddelled by Poisson distribution:
Number of typos (misprints) on a page of a book Number of phone calls at a call center per minute Number of times a web server is accessed per minute Number of pine trees per unit area in a mized forest Number of stars in a given volume of space
## Example

```python
#General
import math

def poisson_pmf(lmbda, i):
    numerator = math.exp(-lmbda) * (lmbda ** i)
    denominator = math.factorial(i)
    pmf = numerator / denominator
    return pmf

def poisson_moment_generating_function(lmbda, t):
    mgf = math.exp(lmbda * (math.exp(t) - 1))
    return mgf

def poisson_expected_value(lmbda):
    expected_value = lmbda
    return expected_value

def poisson_variance(lmbda):
    variance = lmbda
    return variance

# Example usage
lmbda =  1000 * 10**-3  # Mean of the Poisson distribution (λ = np)
i = 5      # Value of X
t = 0.05    # Value of t

# Calculate the pmf
pmf = poisson_pmf(lmbda, i)
print(f"P(X = {i}) = {pmf:.4f}")

# Calculate the moment generating function
mgf = poisson_moment_generating_function(lmbda, t)
print(f"E[e^({t}X)] = {mgf:.4f}")

# Calculate the expected value
expected_value = poisson_expected_value(lmbda)
print(f"E[X] = {expected_value:.4f}")

# Calculate the variance
variance = poisson_variance(lmbda)
print(f"Var(X) = {variance:.4f}")
# P(X = 5) = 0.0031
# E[e^(0.05X)] = 1.0526
# E[X] = 1.0000
# Var(X) = 1.0000
```

```python
#The BER of a communication channel is 10^-3. What is a probability that a block of 1000 bits has five or more errors?  
# using the poisson r.v. in python
from scipy.stats import poisson

lambda_val = 1000 * 10**-3  # Mean of the Poisson distribution (λ = np)

# Calculate the probability using the survival function (1 - cumulative distribution function)
probability = 1 - poisson.cdf(4, lambda_val)  # P(X >= 5) = 1 - P(X <= 4)

print(f"The probability of having five or more errors in a block of 1000 bits is: {probability:.4f}")
# The probability of having five or more errors in a block of 1000 bits is: 0.0037
```

```python
import scipy.stats as stats

# Parameters
mean = 10
rate = 1 / mean

# Time already elapsed
time_elapsed = 10

# Calculate the probability using the survival function (1 - cumulative distribution function)
probability = 1 - stats.expon.cdf(time_elapsed, scale=1/rate)

# Print the result
print("Probability:", probability)
# Probability: 0.36787944117144233
```