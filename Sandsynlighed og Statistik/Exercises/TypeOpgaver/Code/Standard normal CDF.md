
# Example 1
## Code #StatCode

```python
import scipy as scp  
# This is the mean and standard deviation of the first random variable  
X1 = scp.stats.norm(0, 1)  # Create object of a 'frozen' normal RV with mean = 0 and std = 1  
  
print(dir(X1))  
  
# Calculate the probabilities  
prob_greater_than_0 = 1 - X1.cdf(0)  
prob_less_than_neg_2 = X1.cdf(-2)  
prob_between_0_5_and_1_5 = X1.cdf(1.5) - X1.cdf(0.5)  
prob_exactly_0 = 0 # The probability of a continuous random variable being # exactly equal to a specific value is always 0  
  
print(f"Probability of a measurement being greater than 0 degrees: {prob_greater_than_0}")  
print(f"Probability of a measurement being less than -2 degrees: {prob_less_than_neg_2}")  
print(f"Probability of a measurement being between 0.5 and 1.5 degrees: {prob_between_0_5_and_1_5}")  
print(f"Probability of a measurement being exactly 0 degrees: {prob_exactly_0}")
```

## problem
> [!NOTE] Info from problem
> - **normally distributed**
> - **mean**: 0
> - **std. deviaton:** 1
> - **Problem:** *probabilities that a randomly selected temperature measurement agrees with* (1), (2), (3), (4)

Suppose that sensor temperature measurements are normally distributed with mean 0 degrees and standard deviation 1 degrees. Find the probabilities that a randomly selected temperature measurement agrees with each of the following:
1) Greater than 0 degrees
2) less than -2 degrees
3) between 0.5 and 1.5 degrees
4) is exactly 0 degrees