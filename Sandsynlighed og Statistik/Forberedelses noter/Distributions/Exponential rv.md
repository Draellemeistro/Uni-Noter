> [!NOTE] Exponential random variables
> $$E[X]=\frac{1}{\lambda}$$
> $$Var(X)=\frac{1}{\lambda^2}$$
> For calculating mean and variance of exponential random variables

```python
import numpy as np

# Sample data from an exponential distribution
data = np.random.exponential(scale=1.0, size=100)

# Data can manually be difined

# Estimate the rate parameter
rate = 1 / np.mean(data)

import numpy as np

def calculate_exponential_rv_mean_variance(rate):
    # Calculate mean
    mean = 1 / rate

    # Calculate variance
    variance = 1 / (rate ** 2)

    return mean, variance

mean, variance = calculate_exponential_rv_mean_variance(rate)

print("Mean:", mean)
print("Variance:", variance)
# Mean: 0.9299556570930331
# Variance: 0.8648175241593349
```

## MAYBE SEE: [[Poisson process]]
