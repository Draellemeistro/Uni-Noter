Let $X$ be a r.v. representing the number of times a certain event A occurs in $n$ trials (number of success in n trials). Denote $p$ probability of success. - Then $X$ is said to be a binomial r.v. with parameters $n$ and $p$ $$X \sim \text{Binomial}(n, p)$$
the [[Probability Mass Function (PMF)]] is described as: $$P(X = i) = \binom{n}{i} p^i (1 - p)^{n-i}, \quad i = 0, 1, \ldots, n$$
With expectance and variance:
-  $E[X]=np$ 
- $Var(X)=np(1-p)$

```python
import math

def binomial_pmf(n, p, i):
    numerator = math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return numerator

def binomial_expected_value(n, p):
    expected_value = n * p
    return expected_value

def binomial_variance(n, p):
    variance = n * p * (1 - p)
    return variance

# Example usage
n = 10   # Number of trials
p = 0.3  # Probability of success
i = 3    # Number of successes

# Calculate the pmf
pmf = binomial_pmf(n, p, i)
print(f"P(X = {i}) = {pmf:.4f}")

# Calculate the expected value
expected_value = binomial_expected_value(n, p)
print(f"E[X] = {expected_value:.4f}")

# Calculate the variance
variance = binomial_variance(n, p)
print(f"Var(X) = {variance:.4f}")
# P(X = 3) = 0.2668
# E[X] = 3.0000
# Var(X) = 2.1000
```

# **Computing the binomial distribution function**
- To optimize the computational process, we can utilize the following relationship between $P\{X=k+1\}$ and $P\{X=k\}$: $$P(X = k+1) = \frac{p}{1-p} \cdot \frac{n-k}{k+1} \cdot P(X = k)$$
- Now starting from $P(X=0)$ we can recursively find all other $P(X=k)$
```python
#General
def binomial_pmf(n, p, k):
    pmf = [0] * (k + 1)  # Initialize an array to store the pmf values
    pmf[0] = (1 - p)**n  # P(X = 0)

    for i in range(k):
        pmf[i + 1] = (p / (1 - p)) * ((n - i) / (i + 1)) * pmf[i]

    return pmf

# Example usage
n = 10   # Number of trials
p = 0.3  # Probability of success
k = 5    # Number of successes

# Calculate the binomial distribution function
pmf = binomial_pmf(n, p, k)

# Print the pmf values
for i, probability in enumerate(pmf):
    print(f"P(X = {i}) = {probability:.4f}")

# P(X = 0) = 0.0282
# P(X = 1) = 0.1211
# P(X = 2) = 0.2335
# P(X = 3) = 0.2668
# P(X = 4) = 0.2001
# P(X = 5) = 0.1029
```

```python
#A system consists of n components. Each component functions independently with probability p. 
#Question: for which values of p is a 5-component system more likely to operate than a 3-component system? 
import math

def system_3_component(p):
    # Calculate the probability of a 3-component system operating
    q = 1 - p
    probability = math.comb(3, 2) * (p ** 2) * (q ** 1) + (p ** 3)
    return probability

def system_5_component(p):
    # Calculate the probability of a 5-component system operating
    q = 1 - p
    probability = math.comb(5, 3) * (p ** 3) * (q ** 2) + math.comb(5, 4) * (p ** 4) * (q ** 1) + (p ** 5)
    return probability

# Iterate over different values of p
for p in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
    probability_3_component = system_3_component(p)
    probability_5_component = system_5_component(p)
    
    # Compare the probabilities and print the result
    if probability_5_component > probability_3_component:
        print(f"For p = {p}, the 5-component system is more likely to operate.")
    else:
        print(f"For p = {p}, the 3-component system is more likely to operate.")

# For p = 0.1, the 3-component system is more likely to operate.
# For p = 0.2, the 3-component system is more likely to operate.
# For p = 0.3, the 3-component system is more likely to operate.
# For p = 0.4, the 3-component system is more likely to operate.
# For p = 0.5, the 3-component system is more likely to operate.
# For p = 0.6, the 5-component system is more likely to operate.
# For p = 0.7, the 5-component system is more likely to operate.
# For p = 0.8, the 5-component system is more likely to operate.
# For p = 0.9, the 5-component system is more likely to operate.
```
