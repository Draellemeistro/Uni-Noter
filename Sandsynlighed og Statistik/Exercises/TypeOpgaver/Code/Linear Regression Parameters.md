
# Example 1
## Code #StatCode 

```python
import numpy as np  
from matplotlib import pyplot as plt

n= 13  # SUPERFLUOUS?
year = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])  
oil_spill_amount = np.array([9, 5, 7, 8, 5, 8, 5, 6, 7, 3, 4, 6, 7]) 

# Obtain the linear regression parameters  
# The slope (beta1) and the y-intercept (beta0).  
beta1, beta0 = np.polyfit(x, y, 1)  
  
print(f"The linear regression parameters are: beta0 = {beta0}, beta1 = {beta1}")  
  
# Year for which we want to estimate the number of oil spills  
year = 2023  
  
# Estimate the number of oil spills for the given year  
estimated_oil_spills = beta1 * year + beta0  
  
print(f"The estimated mean number of oil spills for {year} is {estimated_oil_spills}")  
  
# Plot the individual data points  
plt.scatter(x, y, color='blue', label='Data points')  
  
# Plot the line of best fit  
plt.plot(x, beta1 * x + beta0, color='red', label='Line of best fit')  
  
# Add labels and title  
plt.xlabel('Year')  
plt.ylabel('Number of oil spills')  
plt.title('Number of oil spills per year')  
  
# Add a legend  
plt.legend()  
  
# Display the plot  
plt.show()

```


## Problem
1. **Obtain the linear regression parameters** $\hat{\beta}_{0}$ **and** $\hat{\beta_{1}}$  **for the data**
2. **Estimate the mean number of oil spills for 2023.**

| year | \# of oil spills  |
| ---- | ----------------- |
| 2010 | 9                 |
| 2011 | 5                 |
| 2012 | 7                 |
| 2013 | 8                 |
| 2014 | 5                 |
| 2015 | 8                 |
| 2016 | 5                 |
| 2017 | 6                 |
| 2018 | 7                 |
| 2019 | 3                 |
| 2020 | 4                 |
| 2021 | 6                 |
| 2022 | 7                 |

