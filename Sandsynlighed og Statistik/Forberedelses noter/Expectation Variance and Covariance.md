[KILDE](https://github.com/agangster1/Sandsynlighed-og-statestik-formelsamling/blob/main/mm_3Expect_variance_covariance.ipynb)

# Expectation E\[X]
- **==E(X)==**; the expectation represents the average value or mean of a discrete random variable X  It provides a measure of the central tendency of the variable's distribution
  $$E[X] = \sum \limits _{i} x_i P(X = x_i) = \sum \limits _{i} x_i p(x_i)$$
- **==E\[X]==**: Expected value is a measure of the central tendency or average value of a random variable. In the context of probability and statistics, it represents the long-term average outcome or value we would expect to observe if we repeated an experiment many times.
- $x_i$: This represents the possible values that the random variable X can take. In other words, x_i represents a specific outcome or value that X can assume.
- $P(X = x_i)$ or$p(x_i)$: This represents the probability that the random variable $X$ takes on the value $x_i$. In other words, it represents the likelihood of each possible outcome occurring.
- The expected value is a useful concept in probability and statistics as it provides a single value that summarizes the central tendency of a random variable. It can be used to make predictions, compare different random variables, or evaluate the average outcome of an experiment or process.
```python
import math

x = [1, 2, 3, 4, 5, 6] #possible events
p = [1/6, -1/6, 1/6, -1/6, 1/6, -1/6] #corresponding weighted probabilities set by the rules of the game (see slide 4 & 7 (mm3_updated.pdf))

# To calculate the expected value E(x), you sum up the products of each possible value x_i and its corresponding probability P(X = x_i):
expectation = sum(xi * pi for xi, pi in zip(x, p))
#In this equation, you iterate over all the possible values of X, multiply each value by its corresponding probability, and sum up these products. The result is the expected value of X.

# Print the result
print("E(X) =", expectation)
# E(X) = -0.5
```

## X is a continuous RV
- If X is a continuous random variable
  $$E[X] = \int_{-∞}^∞ \, x f(x)dx$$
- $E[X]$: As mentioned above, the expected value represents the average or central tendency of a random variable.
- $x$: This variable represents the possible values that the continuous random variable X can take.
- $f(x)$: This represents the probability density function **([[Probability Density Function (PDF)|PDF]])** of $X$. The **PDF** provides the relative likelihood of observing different values of $X$. It describes the distribution of $X$ and its shape.
- The expected value of a continuous random variable provides a measure of the central tendency or average value of the variable. It is useful for characterizing the distribution and making predictions or comparisons based on the average outcome.
```python
import math
from scipy.integrate import quad #pip install scipy

#To calculate the expected value, you multiply each possible value x by its corresponding probability density f(x), and then integrate over the entire range of X:

def f(x): #whatever function is given in problem put here
    if 0 <= x <= 1:
        return x
    elif -1 <= x < 0:
        return -x
    else:
        return 0

def integrand(x):
    return x * f(x)

# Define the integration limits
lower_limit = float(-1) #whatever lowerlimit is given in problem put here
upper_limit = float(1) #whatever upperlimit is given in problem put here

# Perform the numerical integration
expectation, error = quad(integrand, lower_limit, upper_limit)
#In this equation, you integrate the product of x and f(x) over the entire range of possible values for X. The integral sums up the contributions from all the possible values of X, weighted by their respective probabilities.

# Print the result
print("E[X] =", expectation)
# E[X] = 0.0
```
Now we found the expected value of a function $g(X)$, think of it as a new random variable $Y=g(X)$
$$E[Y] = E[g(X)] = \sum \limits _{i} g(x_i) p(x_i)$$
- $E[Y]$: This represents the expected value of the random variable $Y$. In this case, $Y$ is defined as the function $g(X)$.
- $g(X)$: This is a function that operates on the random variable $X$. It takes the values of $X$ as inputs and produces corresponding values of $Y$.
- $x_i$: These are the possible values that the random variable $X$ can take.
- $p(x_i)$: This represents the probability mass function ([[Probability Mass Function (PMF)|PMF]]) of $X$, which gives the probability of each possible value $x_i$.
- This equation allows you to **calculate the expected value of a transformed random variable by applying a function to the original random variable**. 
	- It is commonly used to assess the average outcome or behavior of a function of interest.
```python
#To calculate the expected value E[Y], you sum up the products of the function values g(x_i) and their corresponding probabilities p(x_i):

x = [-2, -1, 1, 2] #possible events
p = [1/len(x), 1/len(x), 1/len(x), 1/len(x)] #corresponding weighted probabilities

def g(x): #function of the possible events
    return x**2

# Calculate E(X)
expectation = sum(g(xi) * pi for xi, pi in zip(x, p))
#In this equation, you iterate over all the possible values of X, apply the function g(X) to each value, multiply the result by the corresponding probability p(x_i), and sum up these products. The result is the expected value of Y

# Print the result
print("E(X) =", expectation)
# E(X) = 2.5
```


> [!NOTE] Rules
> - **ALWAYS applies:**
> 	- $E[X+Y]=E[X]+E[Y]$
> - **only if INDEPENDENT:**
> 	- $E[X*Y]=E[X]*E[Y]$

# Variance
- Variance is a statistical measure that quantifies the spread or variability of a set of data points around their mean.  It provides a measure of how much the individual data points deviate from the average.
  $$Var(X)=E[(X-E(x))^2]=E[X^2]-E[X]^2$$
- $Var(X)$: This represents the variance of the random variable $X$. Variance is a measure of the spread or dispersion of a random variable's distribution.
- $E(X)$: This denotes the expected value or mean of the random variable $X$.
- $(X - E(X))^2$: This term represents the squared difference between each individual value of $X$ and its expected value. This step is necessary to measure the spread of the random variable
```python
 To calculate the variance, you take the expected value of the squared differences between X and its expected value:

def calculate_variance(data):
    # Calculate the number of data points
    n = len(data)
    
    # Calculate the mean of the data points
    mean = sum(data) / n
    
    # Calculate the variance using the formula (x - mean)^2
    # Sum up the squared differences between each data point and the mean
    variance = sum((x - mean) ** 2 for x in data) / n
    
    # Return the calculated variance
    return variance

# Example usage
values = [1, 2, 3, 4, 5]
result = calculate_variance(values)

# The variance provides information about the spread or dispersion of the values of X around its mean

print("Var(X) =", result)
# Var(X) = 2.0
```

## Covariance
-  It measures how changes in one variable correspond to changes in another variable
  $$Cov(X,Y)=E[(X-E[X])(Y-E[Y])]$$
- $Cov(X, Y)$: This represents the covariance between the random variables $X$ and $Y$. Covariance measures the extent to which $X$ and $Y$ vary together or co-vary.
- $E(X)$: This denotes the expected value or mean of the random variable $X$.
- $E(Y)$: This denotes the expected value or mean of the random variable $Y$.
- $(X - E(X))(Y - E(Y))$: This term represents the product of the differences between each individual value of $X$ and its expected value, and each individual value of $Y$ and its expected value. This step captures how the two variables deviate from their respective means simultaneously.
- **==The covariance is a measure of the linear relationship between two random variables.==**

#### Properties of Covariance
- $Cov(X,Y)=Cov(Y,X)$
- $Cov(X,X)=Var(X)$
- $Cov(aX,Y)=aCov(X,Y)$
- if $X$ and $Y$ are independent, $Cov(X,Y)=0$
- $Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y)$
	- thus, $Var(X+Y)=Var(X)+Var(Y)$ only in case of independence
### Code Covariance
```python
# To calculate the covariance, you take the expected value of the product of the deviations between X and its mean and Y and its mean:

def calculate_covariance(data_x, data_y):
    # Calculate the number of data points
    n = len(data_x)
    
    # Calculate the means of X and Y
    mean_x = sum(data_x) / n
    mean_y = sum(data_y) / n
    
    # Calculate the covariance using the formula (X - E(X))(Y - E(Y))
    covariance = sum((data_x[i] - mean_x) * (data_y[i] - mean_y) for i in range(n)) / n
    
    # Return the calculated covariance
    return covariance

# Example usage
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]
result = calculate_covariance(x_values, y_values)

# This formula measures the average or expected joint variability between X and Y. 
# If the covariance is positive, it indicates that the variables tend to move together in the same direction. 
# If it is negative, it suggests that the variables tend to move in opposite directions. 
# A covariance of zero suggests no linear relationship between the variables.

print("Cov(X, Y) =", result)
# Cov(X,Y) = 4.0
```

## Some useful identities concerning variances:
#### Variance of Linear Transformations
- Calculate the variance of the linear transformation:
  $$Var(aX+b)=a^2Var(X)$$
- $Var(aX + b)$: This represents the variance of the random variable ($aX + b$).
- $a$: This is a constant multiplier.
- $X$: This represents the random variable.
- $b$: This is a constant term added to the product of $aX$.
- **This property is often used in probability and statistics to analyze how linear transformations affect the variance of a random variable.** 
- ==It provides a simple way to calculate the new variance when the original random variable is scaled and shifted by constants.==
```python
# The property states that the variance of the transformed random variable (aX + b) is equal to the square of the constant "a" multiplied by the variance of the original random variable X:

def variance_linear_transform(a, b, variance_X):
    # Calculate the variance of the linear transformation
    transformed_variance = (a ** 2) * variance_X
    
    # Return the transformed variance
    return transformed_variance

# Example usage
a = 2
b = 3
variance_X = 5

# Calculate the variance of the linear transformation
result = variance_linear_transform(a, b, variance_X)

# In other words, multiplying a random variable X by a constant "a" and adding a constant "b" does not change the variance of the random variable. 
# However, the variance is scaled by the square of the constant "a".

print("Var(aX + b) =", result)
# Var(aX+b) = 20
```
#### Variance of constants
- Calculate the variance of the constant
  $$Var(b)=0$$
```python
def variance_constant(b):
    # Variance of a constant is always zero
    constant_variance = 0
    
    # Return the variance of the constant
    return constant_variance

# Example usage
b = 5

# Calculate the variance of the constant
result = variance_constant(b)
print("Var(b) =", result)
```

#### Variance of shifted RV
- Calculate the variance of the shifted random variable $$Var(X+b)=Var(X)$$
- $Var(X + b)$: This represents the variance of the random variable ($X + b$).
- $X$: This represents the random variable.
- $b$: This is a constant term added to the random variable $X$.
- **This property is a fundamental result in probability and statistics**. 
	- ==It implies that shifting a random variable by a constant does not alter its variance==. 
	- However, it is ***important to note that the mean of the random variable will change when a constant is added.***
```python
# The property states that adding a constant "b" to a random variable X does not change the variance of the random variable:

def variance_shift(X_variance):
    # Variance remains the same when shifting a random variable by a constant
    shifted_variance = X_variance
    
    # Return the shifted variance
    return shifted_variance

# Example usage
X_variance = 10

# Calculate the variance of the shifted random variable
result = variance_shift(X_variance)

# In other words, the variance of the sum of X and a constant "b" is equal to the variance of X alone. 
# The addition of a constant term does not affect the spread or dispersion of the random variable

print("Var(X + b) =", result)
# Var(X + b) = 10
```
### Correlation coefficient

> [!NOTE] Title
> Instead of covariance, we can work with dimensionless quality: **Correlation coefficient** of X and Y.
> 
> **Correlation coefficient is a measure of the strength and direction of the linear relationship between two variables**

$$Corr(X, Y) = \frac{Cov(X, Y)}{\sqrt{(Var(X))}\sqrt{(Var(Y))}}$$
- $Corr(X, Y)$: This represents the correlation coefficient between the random variables $X$ and $Y$. The correlation coefficient measures the strength and direction of the linear relationship between the two variables.
- $Cov(X, Y)$: This represents the covariance between the random variables $X$ and $Y$. Covariance measures the extent to which $X$ and $Y$ vary together or co-vary.
- $Var(X)$: This represents the variance of the random variable $X$. Variance measures the spread or dispersion of $X$.
- $Var(Y)$: This represents the variance of the random variable $Y$. Variance measures the spread or dispersion of $Y$.
- The correlation coefficient is a widely used measure in statistics and is **helpful for understanding the degree of association or dependence between two variables**. 
	- ***==It allows you to quantify the strength and direction of the linear relationship, independent of the scale or units of measurement of the variables.==***
```python
import numpy as np

# The formula for calculating the correlation coefficient is:

def calculate_correlation_coefficient(x_values, y_values):
    # Calculate the correlation coefficient using numpy's corrcoef function
    correlation_matrix = np.corrcoef(x_values, y_values)
    
    # The correlation coefficient is the element at index (0, 1) or (1, 0) in the correlation matrix
    correlation_coefficient = correlation_matrix[0, 1]
    
    # Return the correlation coefficient
    return correlation_coefficient

# Example usage
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]
result = calculate_correlation_coefficient(x_values, y_values)

# In this formula, the covariance between X and Y is divided by the product of the square roots of their variances. The correlation coefficient normalizes the covariance by scaling it with the standard deviations of X and Y.

# The correlation coefficient ranges between -1 and 1. A value of 1 indicates a perfect positive linear relationship, -1 indicates a perfect negative linear relationship, and 0 indicates no linear relationship between X and Y.

print("Correlation coefficient =", result)
```
