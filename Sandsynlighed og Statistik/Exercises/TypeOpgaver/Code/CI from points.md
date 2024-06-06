
# Example 1
## Code #StatCode 


```python
import math  
import numpy as np  
from scipy.stats import norm  
  
# To estimate the population mean µ, you calculate the sample mean by taking the sum of all observations and dividing it by the sample size:  
  
def calculate_confidence_interval(data, confidence_level):  
    n = len(data)  # Sample size  
    sample_mean = sum(data) / n  # Sample mean  
  
    # Standard deviation of the sample    
    sample_std = math.sqrt(sum([(x - sample_mean) ** 2 for x in data]) / (n - 1))  
  
    # Z-value corresponding to the desired confidence level  
    z_value = norm.ppf(1 - (1 - confidence_level) / 2)  
  
    # Margin of error  
    margin_of_error = z_value * (sample_std / math.sqrt(n))  
  
    # Confidence interval bounds  
    lower_bound = sample_mean - margin_of_error  
    upper_bound = sample_mean + margin_of_error  
  
    return (lower_bound, upper_bound)  
  
if __name__ == "__main__":  
    eu_emissions = np.array([5.05, 5.55, 4.74, 8.09])  
    america_emissions = np.array([4.12, 1.78, 1.06, 3.21, 14.86])  
    confidence_level = 0.90  
    lower_eu, upper_eu = calculate_confidence_interval(eu_emissions, confidence_level)  
    lower_america, upper_america = calculate_confidence_interval(america_emissions, confidence_level)  
    print(f"Europe: Confidence Interval ({confidence_level * 100}%): ({lower_eu}, {upper_eu})")  
    print(f"America: Confidence Interval ({confidence_level * 100}%): ({lower_america}, {upper_america})")
```

## Problem

**Obtain the 90% confidence interval for the CO2 emissions per capita in America and Europe**

| Region      | Country   | yrly CO2 per capita (tonnes) |
| ----------- | --------- | ---------------------------- |
| **america** | Argentina | 4.12                         |
| **america** | Columbia  | 1.78                         |
| **america** | Honduras  | 1.06                         |
| **america** | Mexico    | 3.21                         |
| **america** | US        | 14.86                        |
| **Europe**  | Denmark   | 5.05                         |
| **Europe**  | Italy     | 5.55                         |
| **Europe**  | France    | 4.74                         |
| **Europe**  | germany   | 8.09                         |
