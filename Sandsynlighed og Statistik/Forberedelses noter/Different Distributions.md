

> [!NOTE] Distributions
> - **==DISCRETE==**
> 	- **[[Bernoulli rv]]**
> 	- **[[Binomial rv]]**
> 	- **[[Geometric rv]]**
> 	- **[[Poisson rv]]**
> - **==CONTINUOUS??==**
> 	- **[[Uniform rv]]**
> 	- **[[Exponential rv]]**
> 	- Normal?
> 	- Poisson process?



# Properties Discrete Distributions
[KILDE](https://github.com/agangster1/Sandsynlighed-og-statestik-formelsamling/blob/main/mm_4Special%20Probability%20Distributions%20for%20Bernoulli%2C%20Binomial%2C%20Geometric%20and%20Poisson.ipynb)
The mean value is sometimes called ==the first moment of $X$==. The n'th moment of $X$ is defined by: The expected value of $X$ to the power of $n$ using the probability mass function ([[Probability Mass Function (PMF)|PMF]]):
$$E[X^n] = \sum_i x_i^n \cdot p(x_i)$$
The expected value of $X$ to the power of $n$ using the probability density function ([[Probability Density Function (PDF)|PDF]]):
$$E[X^n] = \int_{-\infty}^{\infty} x^n \cdot f(x) \, dx$$
## [[Bernoulli rv]]
An experiment with 2 possible outcomes (*success* or *failure*) is called a **Bernoulli trial**. The indicator of event A is called the Bernoulli r.v. since it describes outcome of a Bernoulli trial.

> [!NOTE] ELI5: Bernoulli
> Every Bernoulli trial, regardless of the definition of A, is equivalent to the ***tossing of a biased coin***.

$$E[I]=p$$
$$Var(I)=p(1-p)$$
==Example==: a r.v. I is an indicator of the event A The expected value of the indicator of an event is equal to the probability event:
$$I = \begin{cases} 1 & \text{if A occurs} \\ 0 & \text{if A does not occur} \end{cases}$$
$$E[I]=1*P(A)+0*P(A^c)=P(A)$$
$$Var(I) = E[I^2]-E[I]^2 = E[I]-E[I]^2 = E[I]*(1-E[I])=P(A)P(A^c)$$
```python
def bernoulli_expected_value(p):
    # Calculate the expected value of a Bernoulli random variable
    return p

def bernoulli_variance(p):
    # Calculate the variance of a Bernoulli random variable
    return p * (1 - p)

# Example usage
p = 0.6  # Probability of success (event A)

expected_value = bernoulli_expected_value(p)
variance = bernoulli_variance(p)

print("Expected Value:", expected_value)
print("Variance:", variance)
# Expected Value: 0.6
# Variance: 0.24
```


## [[Binomial rv]]
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

#### Computing the binomial distribution function
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

## [[Geometric rv]]
Let a r.v. $M$ be a number of independent **Bernoulli trials** until the first occurence of a success. $M$ is called a **geometric r.v**. [[Probability Mass Function (PMF)]]:
$$P{M=k}=(1-p)^{k-1}p$$
Expectance and Variance:
- $E[M]=\frac{1}{p}$
- $Var(M)=\frac{{1-p}}{p^2}$

==Example==: applications where we are interested in the time that elapses between the occurence of events in a sequence of independent experiments
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

## Hypergeometric rv: see [[Geometric rv]]
Suppose we have objects of ==two types==: type 1 N objects (acceptable components) and type 2 M objects (defective components). A sample of $n$ objects is randomly chosen without replacement. A r.v. $X$ represents a number of type 1 objects in the selection  hypergeometric with parameters ($N$, $M$, $n$) [[Probability Mass Function (PMF)]]:
$$P(X = i) = \frac{{\binom{N}{i} \binom{M}{n-i}}}{{\binom{N+M}{n}}}$$
Expectance and Variance:
$$E[X]=\frac{nN}{N+M}$$
$$ Var(X)=np(1-p)[1-\frac{n-1}{N+M-1}]$$
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

## [[Poisson rv]]
A r.v. taking on one of values 0, 1, 2, … is said to be a **Poisson** r.v. with parameter $λ$: (λ>0), if [[Probability Mass Function (PMF)]] is given by: $$P(X=i)=e^λ *\frac{λ^i}{i!}$$
**Moment generating function:** $$E[e^{tX}] = e^{λ(e^t - 1)}$$
Expectation and Variance:
- $E[X]=\lambda$
- $Var(X)=\lambda$

### Events that can be moddelled by Poisson distribution
Number of typos (misprints) on a page of a book Number of phone calls at a call center per minute Number of times a web server is accessed per minute Number of pine trees per unit area in a mized forest Number of stars in a given volume of space

> [!NOTE] Poisson: What for?
> One of the applications of the **Poisson probabilities** is ==*to approximate*== the **binomial probabilities** – when $n$ is large and $p$ is small. $$\lambda=np$$

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