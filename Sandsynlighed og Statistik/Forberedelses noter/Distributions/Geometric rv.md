Let a r.v. $M$ be a number of independent **Bernoulli trials** until the first occurence of a success. $M$ is called a **geometric r.v**. [[Probability Mass Function (PMF)]]:
$$P{M=k}=(1-p)^{k-1}p$$
## Expectance and Variance:
- $E[M]=\frac{1}{p}$
- $Var(M)=\frac{{1-p}}{p^2}$

## Example:
applications where we are interested in the time that elapses between the occurence of events in a sequence of independent experiments
```python
def geometric_pmf(p, k):
    probability = (1 - p)**(k - 1) * p
    return probability

def geometric_expected_value(p):
    expected_value = 1 / p
    return expected_value

def geometric_variance(p):
    variance = (1 - p) / (p**2)
    return variance

# Example usage
p = 0.3  # Probability of success
k = 5    # Number of trials until the first success

# Calculate the pmf
pmf = geometric_pmf(p, k)
print(f"P(M = {k}) = {pmf:.4f}")

# Calculate the expected value
expected_value = geometric_expected_value(p)
print(f"E[M] = {expected_value:.4f}")

# Calculate the variance
variance = geometric_variance(p)
print(f"Var(M) = {variance:.4f}")
# P(M = 5) = 0.0720
# E[M] = 3.3333
# Var(M) = 7.7778
```

# **Hypergeometric** RV
Suppose we have objects of ==two types==: type 1 N objects (acceptable components) and type 2 M objects (defective components). A sample of $n$ objects is randomly chosen without replacement. A r.v. $X$ represents a number of type 1 objects in the selection  hypergeometric with parameters ($N$, $M$, $n$) [[Probability Mass Function (PMF)]]:
$$P(X = i) = \frac{{\binom{N}{i} \binom{M}{n-i}}}{{\binom{N+M}{n}}}$$
## Expectance and Variance:
$$E[X]=\frac{nN}{N+M}$$
$$ Var(X)=np(1-p)[1-\frac{n-1}{N+M-1}]$$

## Example:
```python
import math

def hypergeometric_pmf(N, M, n, i):
    numerator = math.comb(N, i) * math.comb(M, n - i)
    denominator = math.comb(N + M, n)
    probability = numerator / denominator
    return probability

def hypergeometric_expected_value(N, M, n):
    expected_value = (n * N) / (N + M)
    return expected_value

def hypergeometric_variance(N, M, n):
    p = N / (N + M)
    variance = n * p * (1 - p) * ((N + M - n) / (N + M - 1))
    return variance

# Example usage
N = 10  # Number of type 1 objects
M = 20  # Number of type 2 objects
n = 5   # Number of objects chosen
i = 2   # Number of type 1 objects in the selection

# Calculate the pmf
pmf = hypergeometric_pmf(N, M, n, i)
print(f"P(X = {i}) = {pmf:.4f}")

# Calculate the expected value
expected_value = hypergeometric_expected_value(N, M, n)
print(f"E[X] = {expected_value:.4f}")

# Calculate the variance
variance = hypergeometric_variance(N, M, n)
print(f"Var(X) = {variance:.4f}")
# P(X = 2) = 0.3600
# E[X] = 1.6667
# Var(X) = 0.9579
```
