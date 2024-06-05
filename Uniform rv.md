# Stuff
Uniform random variable in 2D space:$$C=\frac{1}{A}$$
The equation states that for each point in the pdf is all equal likely For calculation the properbility of a constinous random variable in the spectrum of a to b in a uniform [[Cumulative distribution function (CDF)]].
## Mean and Variance
$$E[X] = \int_{\alpha}^{\beta} \frac{x}{\beta-\alpha} \cdot dx = \frac{{\beta + \alpha}}{2}$$ 
$$E[X^2] = \int_{\alpha}^{\beta} \frac{x^2}{\beta-\alpha} \cdot dx = \frac{{\beta^3 - \alpha^2}}{3(\beta - \alpha)}$$
$$\text{Var}(X) = E[X^2] - E[X]^2 = \frac{{(\beta - \alpha)^2}}{12}$$ 
```python
def calculate_uniform_rv_mean_variance(a, b):
    # Calculate mean
    mean = (a + b) / 2

    # Calculate mean^2
    mean2 = (a**3 - b**2) / 3*(a - b)
    
    # Calculate variance
    variance = ((b - a) ** 2) / 12

    return mean, mean2, variance

# Example usage
lower_bound = 2
upper_bound = 1

mean, mean2, variance = calculate_uniform_rv_mean_variance(lower_bound, upper_bound)

print("Mean:", mean)
print("Mean^2:", mean2)
print("Variance:", variance)
# Mean: 1.5
# Mean^2: 2.3333333333333335
# Variance: 0.08333333333333333
```

## For random PDF can be defined manually for a set of values:
##### When all events are not equally likely:

```python
import numpy as np
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt
import random
from scipy.integrate import quad

def create_pdf(data):
    # Create a probability density function (PDF) of the data using kernel density estimation (KDE)
    kde = gaussian_kde(data)

    # Evaluate the PDF on a grid of points
    x_vals = np.linspace(min(data), max(data), num=200)
    y_vals = kde(x_vals)

    # Return the x and y values of the PDF
    return x_vals, y_vals

def calculate_integral(pdf, x_start, x_end, num_points=10000):
    # Define a lambda function for the PDF that takes a single argument x
    pdf_func = lambda x: np.interp(x, pdf[0], pdf[1])
    
    # Calculate the integral of the PDF over the given range using the quad function from scipy
    x_vals = np.linspace(x_start, x_end, num=num_points)
    y_vals = pdf_func(x_vals)
    dx = (x_end - x_start) / (num_points - 1)
    integral = np.sum(y_vals) * dx
    
    if integral >= 1:
        integral = 1
    
    return integral

# Generate a list of random values
data = []
for i in range(1000):
    value = random.uniform(-2, 3)
    data.append(value)

#
# Data can manually be difined as a list of values
#

# Create a probability density function (PDF) of the data
x_vals, y_vals = create_pdf(data)

# Calculate the integral of the PDF over a given range (x_start to x_end):
x_start = -1
x_end = 1
integral = calculate_integral((x_vals, y_vals), x_start, x_end)
print("Integral of PDF over [{}, {}]: {}".format(x_start, x_end, integral))

# Plot the PDF
plt.plot(x_vals, y_vals)
plt.axvline(x=x_start, color='r', linestyle='--', label='a')
plt.axvline(x=x_end, color='g', linestyle='--', label='b')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Probability Density Function')
plt.show()

# Integral of PDF over [-1, 1]: 0.4076685338438103
```
![[Pasted image 20240605124659.png]]


## Ex: What er the probability that the temperature is between 15 and 20 degrees when i know that the min is 10 and the max is 30?

```python
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

def calculate_probability_cdf(a, b, min_val, max_val):
    cdf_b = (b - min_val) / (max_val - min_val)
    cdf_a = (a - min_val) / (max_val - min_val)
    probability = cdf_b - cdf_a
    return probability

def calculate_probability_pdf(a, b, min_val, max_val):
    pdf_b = 1 / (max_val - min_val)
    pdf_a = 1 / (max_val - min_val)
    probability = (b - a) * (pdf_b + pdf_a) / 2
    return probability

# Example usage
a = 15  # Lower bound
b = 20  # Upper bound
min_val = 10  # Minimum 
max_val = 30  # Maximum 

probability_cdf = calculate_probability_cdf(a, b, min_val, max_val)
probability_pdf = calculate_probability_pdf(a, b, min_val, max_val)

print(f"The probability (CDF) between {a} and {b} is: {probability_cdf}")
print(f"The probability (PDF) between {a} and {b} is: {probability_pdf}")

#:::::::::
#Plots
#:::::::::

# Plotting the CDF
x_cdf = np.linspace(min_val, max_val, 1000)
y_cdf = stats.uniform.cdf(x_cdf, loc=min_val, scale=max_val-min_val)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(x_cdf, y_cdf)
plt.axvline(x=a, color='r', linestyle='--', label='a')
plt.axvline(x=b, color='g', linestyle='--', label='b')
plt.xlabel('Temperature')
plt.ylabel('CDF')
plt.title('Uniform Distribution CDF')
plt.legend()

# Plotting the PDF
x_pdf = np.linspace(min_val, max_val, 1000)
y_pdf = stats.uniform.pdf(x_pdf, loc=min_val, scale=max_val-min_val)

plt.subplot(1, 2, 2)
plt.plot(x_pdf, y_pdf)
plt.axvline(x=a, color='r', linestyle='--', label='a')
plt.axvline(x=b, color='g', linestyle='--', label='b')
plt.xlabel('Temperature')
plt.ylabel('PDF')
plt.title('Uniform Distribution PDF')
plt.legend()

plt.tight_layout()
plt.show()
# The probability (CDF) between 15 and 20 is: 0.25
# The probability (PDF) between 15 and 20 is: 0.25
```
![[Pasted image 20240605124531.png]]
```python
def calculate_uniform_rv_mean_variance(a, b):
    # Calculate mean
    mean = (a + b) / 2

    # Calculate mean^2
    mean2 = (a**3 - b**2) / 3*(a - b)
    
    # Calculate variance
    variance = ((b - a) ** 2) / 12

    return mean, mean2, variance

# Example usage with temperature
lower_bound = 30 
upper_bound = 10

mean, mean2, variance = calculate_uniform_rv_mean_variance(lower_bound, upper_bound)

print("Mean:", mean)
print("Mean^2:", mean2)
print("Variance:", variance)
# Mean: 20.0
# Mean^2: 179333.3333333333
# Variance: 33.333333333333336
```