[kilde](https://github.com/agangster1/Sandsynlighed-og-statestik-formelsamling/blob/main/mm_1-2Counting_and_basics.ipynb)

kig på bunden af den her [KILDE2](https://github.com/agangster1/Sandsynlighed-og-statestik-formelsamling/blob/main/Gammelformler.ipynb)

Variance: $$Var(X) = E[X^2]-E[X]^2$$

Standard deviation: $$Std(X) = sqrt(Var(X))$$

Covariance is: $$Cov(X,Y)= E[(X-E[X])(Y-E[Y])]$$

Correlation: $$Corr(X,Y)=\frac{Cov(X,Y)}{(sqrt(Var(X))*sqrt(Var(Y))})$$

# general knowledge
- when all events are equally likely to happen: $P(A)=\frac{|A|}{|S|}$
```python
A = [1,2] # success events
S = [1,2,3,4,5,6] # Sample space
propA = len(A)/len(S)
print(propA)
```

- or any event E, the probability P(E) is non-negative: $P(E) \geq 0$

- For any two disjoint events E and F, the probability of their union is the sum of their individual probabilities: $P(E \cup F) = P(E) + P(F)$

- Sampling with or without replacement: $Possibilities = n^k$
```python
# we want to draw k samples from n values
n = 6 
k = 6 
Possibilities = n ** k
print(Possibilities)
```


- Sampling without Replacement and with Ordering: $Possibilities = \frac{n!}{(n - k)!}$
```python
import math
# we want to draw k samples from n values
n = 6 
k = 6 
Possibilities = math.factorial(n) / math.factorial(n - k)
print(Possibilities)
```

- Sampling without Replacement and without Ordering: $Possibilities = {n\choose k} = \frac{n!}{(n-k)!*k!}$
```python
import math
# we want to draw k samples from n values
n = 6 
k = 6 
Possibilities = math.factorial(n) / math.factorial(k) * (math.factorial(n - k))
print(Possibilities)
```

- Sampling with replacement and without ordering: $Possibilities = \frac{(n + k - 1)!}{k! * (n - 1)!}$
```python
import math
# we want to draw k samples from n values
n = 6 
k = 6 
Possibilities = math.factorial(n + k - 1) / (math.factorial(k) * (math.factorial(n - 1)))
print(Possibilities)
```


- Bayes formula: $P(A | B) = \frac{P(B | A) \cdot P(A)}{P(B)}$
```python
def bayes_formula(prob_a_sent, prob_b_sent, prob_a_sent_fail, prob_b_sent_fail):
    # Calculate the probability of A given evidence
    prob_a_given_received = (prob_a_sent * (1 - prob_a_sent_fail)) / (
                (prob_a_sent * (1 - prob_a_sent_fail)) + (prob_b_sent * prob_b_sent_fail))
    return prob_a_given_received

# Inputs
prob_a_sent = 12/30
prob_b_sent = 20/35
prob_a_sent_fail = 1 / 2
prob_b_sent_fail = 1 / 2

# Calculate probability using Bayes' formula
result_a = bayes_formula(prob_a_sent, prob_b_sent, prob_a_sent_fail, prob_b_sent_fail)
# Calculate probability using Bayes' formula
result_b = bayes_formula(prob_b_sent, prob_a_sent, prob_b_sent_fail, prob_a_sent_fail)

# Calculate the probability that A is received
prob_a_received = (1-prob_a_sent_fail)*prob_a_sent+prob_b_sent_fail*prob_b_sent

# Calculate the probability that A is received
prob_b_received = (1-prob_b_sent_fail)*prob_b_sent+prob_a_sent_fail*prob_a_sent

# Print the result
print("Probability of A sent given A is received:", result_a)
print("Probability of B sent given A is received:", 1 - result_a)

print("\n")

print("Probability of B sent given B is received:", result_b)
print("Probability of A sent given B is received:", 1 - result_b)

# Print the probability that A is received
print("Probability that A is received:", prob_a_received)

# Print the probability that B is received
print("Probability that B is received:", prob_b_received)
```

- [[Cumulative distribution function (CDF)]]: $F(a) = \sum_{\text{all } x \leq a} P(x)$
```python
import matplotlib.pyplot as plt

def cdf(a, probabilities):
    # Calculate the cumulative distribution function (CDF)
    cdf = 0
    cdf_values = []  # List to store the CDF values
    for x in (probabilities.keys()):
        if x <= a:
            cdf += probabilities[x]
        cdf_values.append(cdf)
    return cdf_values

# Example usage
probabilities = {1: 0.2, 2: 0.3, 3: 0.5}  # Dictionary of probabilities for each value

a = 3  # Value of how much to calculate of the x axis

cdf_values = cdf(a, probabilities)
print("CDF:", cdf_values, sum(probabilities[x] for x in probabilities if x < a))

# Plotting the CDF
x_values = sorted(probabilities.keys())
plt.step(x_values, cdf_values, where='post')
plt.xlabel('Values')
plt.ylabel('CDF')
plt.title('Cumulative Distribution Function')
plt.ylim(0, 1)  # Set the y-axis limits to match the CDF range
plt.xlim(0, a)  # Set the x-axis limits to match the CDF range
plt.grid(True)
plt.show()
```

- [[Probability Mass Function (PMF)]] for discrete R.V: $p(x) = P(X = x)$
```python
import numpy as np
import matplotlib.pyplot as plt

def pmf(x, probabilities):
    # Calculate the probability mass function (PMF) for a discrete random variable
    if x in probabilities:
        return probabilities[x]
    else:
        return 0

def plot_pmf(probabilities):
    values = list(probabilities.keys())
    pmf_values = list(probabilities.values())

    plt.bar(values, pmf_values, width=0.2)
    plt.xlabel('Values')
    plt.ylabel('Probability')
    plt.title('Probability Mass Function (PMF)')
    plt.show()

def calculate_mean(probabilities):
    values = list(probabilities.keys())
    pmf_values = list(probabilities.values())
    mean = np.dot(values, pmf_values)
    return mean

def calculate_variance(probabilities):
    values = list(probabilities.keys())
    pmf_values = list(probabilities.values())
    mean = calculate_mean(probabilities)
    variance = np.dot((values - mean) ** 2, pmf_values)
    return variance

# Example usage
probabilities = {1: 0.2, 2: 0.3, 3: 0.5}  # Dictionary of probabilities for each value

plot_pmf(probabilities)
mean = calculate_mean(probabilities)
variance = calculate_variance(probabilities)

print("Mean:", mean)
print("Variance:", variance)
```


- [[Probability Density Function (PDF)]] continuous r.v: $P(a \leq X < b) = \int_{a}^{b} f(x) dx$
```python
import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt

def pdf(a, b, pdf_function):
    # Calculate the probability density function (PDF)
    result, _ = spi.quad(pdf_function, a, b)
    return result

# Example usage
def pdf_function(x):
    # Define the probability density function (PDF)
    # Replace with your own function or distribution
    return x**2

a = 1.0  # Lower bound
b = 2.0  # Upper bound

pdf_value = pdf(a, b, pdf_function)
print("PDF:", pdf_value)

# Plotting the PDF
x = np.linspace(a, b, 100)  # Create 100 equally spaced points between a and b
y = pdf_function(x)         # Evaluate the PDF function at each point

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('PDF')
plt.title('Probability Density Function')
plt.grid(True)
plt.show()
```

- Mixed type: $F(x) = p_1 * F_1(x) + p_2 * F_2(x) + ... + p_n * F_n(x)$
```python
def cdf(x, probabilities, cdfs):
    # Calculate the cumulative distribution function (CDF)
    cdf = 0
    for i in range(len(probabilities)):
        cdf += probabilities[i] * cdfs[i](x)
    return cdf

# Example usage
probabilities = [0.2, 0.3, 0.5]  # List of probabilities
cdfs = [cdf1, cdf2, cdf3]  # List of CDF functions for each distribution

x = 2.0  # Value at which to compute the CDF

cdf_value = cdf(x, probabilities, cdfs)
print("CDF:", cdf_value)
```

- Multiple r.v joint CDF: $F(x, y) = P(X \leq x, Y \leq y)$
```python
def joint_cdf(x, y, probabilities):
    # Calculate the joint cumulative distribution function (CDF) for two random variables
    cdf = 0
    for (x_val, y_val), prob in probabilities.items():
        if x_val <= x and y_val <= y:
            cdf += prob
    return cdf

# Example usage
probabilities = { (1, 2): 0.1, (2, 3): 0.2, (3, 4): 0.3, (4, 5): 0.4 }  # Dictionary of probabilities for each (x, y) pair

x = 3.5  # Value for the first random variable
y = 4.2  # Value for the second random variable

cdf_value = joint_cdf(x, y, probabilities)
print("Joint CDF:", cdf_value)
```

- Joint distributed discrete r.vs. [[joint PMF]]: $p(x_i, y_i) = P(X = x_i, Y = y_i)$
```python
def joint_pmf(x, y, probabilities):
    # Calculate the joint probability mass function (PMF) for two random variables
    if (x, y) in probabilities:
        pmf = probabilities[(x, y)]
    else:
        pmf = 0
    return pmf

# Example usage
probabilities = { (1, 2): 0.1, (2, 3): 0.2, (3, 4): 0.3, (4, 5): 0.4 }  # Dictionary of probabilities for each (x, y) pair

x = 2  # Value for the first random variable
y = 3  # Value for the second random variable

pmf_value = joint_pmf(x, y, probabilities)
print("Joint PMF:", pmf_value)
```

- Jointly distributed continous r.vs. $P\{(X, Y) \in C\} = \int\int_{(x, y) \in C} f(x, y) \, dx \, dy$
```python
import scipy.integrate as spi

def probability_in_region(region, joint_pdf_function):
    # Calculate the probability of the event (X, Y) belonging to the given region
    result, _ = spi.dblquad(joint_pdf_function, region[0], region[1], lambda x: region[2](x), lambda x: region[3](x))
    return result

# Example usage
def joint_pdf_function(x, y):
    # Define the joint probability density function (PDF) for (X, Y)
    # Replace with your own function or distribution
    return x * y

region = [1, 2, lambda x: x, lambda x: 2 * x]  # Region defined as [x_min, x_max, y_min_function, y_max_function]

probability = probability_in_region(region, joint_pdf_function)
print("Probability:", probability)
```

- If you are talking about independent r.v. You can split the formulas: [[Cumulative distribution function (CDF)]]: $F(A, B) = F_X(A) \cdot F_Y(B)$

- In terms of [[Probability Mass Function (PMF)]] for discrete random variables (rv) and [[Probability Density Function (PDF)]] for continuous random variables:
	- $p(x, y) = p_X(x) \cdot p_Y(y)$
	- $f(x, y) = f_X(x) \cdot f_Y(y)$
	- Basically, $X$ and $Y$ are independent if knowing the value of one does not change the distribution of another.

- The relationship between two random variables can often be clarified by consideration of the conditional distribution of one given the value of the other.
	- The [[conditional PMF]] ([[probability mass function (PMF)|PMF]]) of $X$ given that $Y=y$ is defined by: $$p_{X|Y}(x|y) = P(X=x|Y=y) = \frac{P(X, Y)}{P_Y(y)}$$
	- If $X$ and $Y$ have a [[joint PDF]] ([[probability density function (PDF)|PDF]]), then the [[conditional PDF]] ([[probability density function (PDF)|PDF]]) of $X$ given that Y=y is defined as: $$f_{X|Y}(x|y) = \frac{f(x, y)}{f_Y(y)}$$


# Types of variables:

## [[Bernoulli rv]]
Two possible outcomes (success or failure) $E[I]=p*var(I)=p(1-p)$

## [[Binomial rv]]:
A certain event A occurs in n trials (number of successes in n trials) [[Probability Mass Function (PMF)|PMF]] :
#StatsTODO 
$$P\{X=i\}=$$
## [[Geometric rv]]:
We do something until we have a success [[Probability Mass Function (PMF)|PMF]]: 
$$P\{M=k\}=(1-p)^{(k-1)}p *E[M]=\frac{1}{p*Var(M)}=\frac{{1-p}}{p^2}$$
## hypergeometric rv (see: [[Geometric rv]])
we have objects of two types: type 1 N objects (acceptable components) and type 2 M objects (defective components). A sample of n objects is randomly chosen without replacement. [[Probability Mass Function (PMF)|PMF]]:
$$P\{X=i\}=\frac{{\left( \frac{N}{i}*\frac{M}{n-i}  \right)}}{\frac{{N+M}}{n}}E[X]$$ $$=\frac{{n*N}}{N+M}Var(X)$$ $$=np(1-p)\left[1-\frac{{n-1}}{N+M-1}\right]$$
#StatsTODO tror ikke at den formel er korrekt. Den ser lidt for kringlet ud

## [[Poisson rv]]
Taking on one of values 0, 1, 2, … is said to be a **Poisson r.v**. with parameter $λ$ (λ>0), if [[Probability Mass Function (PMF)|PMF]] is given by:
$$P(X=i)=e^λ *\frac{λ^i}{i!}$$ 
$$E[X]= λ*Var(X)=λ$$

# types af continues distributes
## [[Uniform rv]]
#### [[Probability Density Function (PDF)]]
$$c = \frac{1}{\beta - \alpha}$$

#### [[Cumulative distribution function (CDF)]]
$$F(x) = \frac{x-a}{\beta - \alpha}$$
$$E[X] = \frac{\beta + \alpha}{2}$$
$$E[X^2] = \frac{\beta^3 + \alpha^3}{3(\beta + \alpha)}$$
$$Var(X) = \frac{(\beta - \alpha)^2}{12}$$
$$Var(X) = \frac{(\beta - \alpha)^2}{12}$$
## [[Exponential rv]]
#### [[Probability Density Function (PDF)]]
$$f(x)=f(x) = \lambda e^{-\lambda x},\text{ }x \geq 0$$
#### [[Cumulative distribution function (CDF)]]
$$F(x) = 1 - e^{-\lambda x}$$
#### Reliability function: (The probability that X is greater than some number)
$$R(x) = P(X<x) = e^{-\lambda x}$$$$E[X] = \frac{1}{\lambda}$$
$$Var(X) = \frac{1}{\lambda^2}$$
==**Example: on average a computer works for 10 years: therefore:**== $$\lambda = \frac{1}{\text{average lifetime}} = \frac{1}{10}$$
#### Memoryless property:
$$P(X>s+t|X>t)=P(X>s)$$
## Poisson process:
$$P(N=k) = \frac{e^{-\lambda}\lambda^k}{k!}$$

## Normal r.v. (Gaussian r.v.)
#### [[Probability Density Function (PDF)]]
$$f(x) = \frac{1}{\sqrt{2\pi\sigma}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$
$$E[X]=\mu$$
$$std(x)=\sigma$$
$$Var(x)=\sigma^2$$
Statistic is used to interpret some data. Sample space: Ω is all the possible outcomes.

### Sample mean:
$$\overline{X}_n=\frac{1}{n}\sum_{i=1}^n X_i$$
### Sample variance:
$$S_n^2=\frac{1}{n-1}\sum_{i=1}^n(X_i -\overline{X}_n)^2$$
### Gaussian distribution:
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$
where $𝑥$ is a random variable, $𝜇$ is the mean, $𝜎$ is the standard deviation, and $𝑒$ is the base of the natural logarithm. 
### Standard normal distribution:
$$\varphi(x) = \frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}$$
where $𝑥$ is a random variable and $𝑒$ is the base of the natural logarithm.

### The central limit theorem:
In words the sum of n i.i.d. random variables are approximately normally distributed with mean $$\mu_{n}=n\mu$$
and variance $$\sigma_{n}2=n\sigma^2$$

