# Example 1
## Code #StatCode

```python
import math  
import scipy.stats as stats  
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
p = 0.25  # Probability of success  
i = 8    # Number of successes  
ii = 9  
iii = 10  
# Calculate the pmf  
pmf1 = binomial_pmf(n, p, i)  
pmf2 = binomial_pmf(n, p, ii)  
pmf3 = binomial_pmf(n, p, iii)  
pmf = pmf1+ pmf2 + pmf3  
print(f"P(X = {i}) = {pmf1:.4f}")  
print(f"P(X = {ii}) = {pmf2:.4f}")  
print(f"P(X = {iii}) = {pmf3:.4f}")  
# Parameters  
for i in range(11):  
    print(f"P(X = {i}) = {binomial_pmf(n, p, i):.4f}")  
  
sums = 0  
for i in range(11):  
    sums = sums+ binomial_pmf(n, p, i)  
  
print(f"sum = {sums:.4f}")  
k = 8   # Minimum number of correct guesses needed  
  
  
# Calculate the cumulative probability of getting 0 to 7 correct answers  
cumulative_prob_up_to_7 = sum(stats.binom.pmf(i, n, p) for i in range(k))  
  
# The probability of getting at least 8 correct answers is 1 minus this cumulative probability  
probability_at_least_8 = 1 - cumulative_prob_up_to_7  
  
print(f'The prdddddddddobability of guessing at least 8 out of 10 correctly is: {probability_at_least_8:.6f}')  
# Parameters  
  
  
# Calculate the probability of getting at least 8 correct answers  
probability_at_least_8_new = stats.binom.sf(k-1, n, p)  # sf(k-1, n, p) gives P(X >= k)  
  
print(f'Tssssssssssssshe probability of guessing at least 8 out of 10 correctly is: {probability_at_least_8_new:.6f}')
```

## Problem

> [!NOTE] Info from problem
> - n: 10
> - $C=\{0,1,2,3\}$
> - probabilities equal
> - **problem:** *find prob of guessing at least 8 out of 10 correctly*

$N$ answer is incorrect
$Y:$ answer is correct
$P(Y)=\frac{1}{4}=0.25$
