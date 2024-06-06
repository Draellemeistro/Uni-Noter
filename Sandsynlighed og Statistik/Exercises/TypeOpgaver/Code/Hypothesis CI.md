
# Example 1
## Code #StatCode

```python
import numpy as np  
from scipy.stats import norm  
  
# Number of households visited  
total_households = 200  
  
# Number of households with a microwave  
households_with_microwave = 175  
  
# Estimate the probability that a Danish household has a microwave  
probability_microwave = households_with_microwave / total_households  
  
print(f"The estimated probability that a Danish household has a microwave is {probability_microwave}")  
  
# Proportion of US households with a microwave in 2017  
p0 = 0.92  
  
# Sample proportion of Danish households with a microwave  
p_hat = households_with_microwave / total_households  
  
# Calculate the standard error  
SE = np.sqrt((p0 * (1 - p0)) / total_households)  
  
# Calculate the z-score  
z = (p_hat - p0) / SE  
  
# Calculate the critical z-value for a one-tailed test at 5% significance level  
z_critical = norm.ppf(0.95)  
  
# Print the results  
print(f"z-score = {z}")  
print(f"critical z-value = {z_critical}")  
  
# Check if we can reject the null hypothesis  
if z > z_critical:  
    print("We reject the null hypothesis. The proportion of Danish households with a microwave is significantly greater than the proportion of US households with a microwave in 2017 at a 5% significance level.")  
else:  
    print("We fail to reject the null hypothesis. There is not enough evidence to conclude that the proportion of Danish households with a microwave is significantly greater than the proportion of US households with a microwave in 2017 at a 5% significance level.")
```

## Problem

> [!NOTE] Info from problem (Who has **Microwave**)
> - 92% of households in **US**, 2017
> - ***n:*** 200, **DK**
> - 175 have a microwave, **DK**
> - **problem:** Estimate prob that a **danish** household has microwave
> - **Problem2:** 5% significance, $H_0$: percentage of **danish** households with a microwave is greater than that of **US


# Example 2
### Code
#StatsTODO 
### Reasoning
Consider the case of flipping a fair coin $n$ times and let $H_{n}$ be the random variable (RV) of the number of heads. Also recall that the sum of n Bernoulli RVs is a Binomial random variable with mean $np$ and variance $np(2−p)$. Calculate and compare the probability of observing $H_{10} ≥ 7$ and $H_{100} ≥ 70$ using each of the following methods.


> [!NOTE] info from problem
> - $H_{n}$: RV for the number of heads
> - sum of n Bernoulli RVs is a Binomial random variable with:
> 	- mean $np$
> 	- variance $np(2-p)$
> - $H_{10}$: number of heads after 10 coin-flips. 100 flips for $H_{100}$
> 	- so calc and compare probability of flipping 7 or more heads in 10 flips
> - $p$: assuming the coin is fair: $p=0.5$

![[Pasted image 20240603192450.png]]

#### a) Summing over the formula for the probability mass function (pmf) of Binomial RVs $$P(H_{n}\geq k)=\sum_{i=1}^{n}{n\choose k}p^k(1-p)^{n-i}$$
##### $H_{10}$ 
$$P(H_{10}\geq 7)=\sum_{i=1}^{10}{10\choose 7}0.5^7(0.5)^{10-i}$$
##### $H_{100}$ 
$$P(H_{100}\geq 70)=\sum_{i=1}^{100}{100\choose 70}0.5^{70}(0.5)^{100-i}$$
##### Fra gpten
The probability of observing 𝐻𝑛≥𝑘Hn​≥k for a Binomial random variable 𝐻𝑛Hn​ with parameters 𝑛n and 𝑝p is given by:
$$P(H_{n}\geq k)=\sum_{i=k}^{n}{n\choose i}p^i(1-p)^{n-i}$$

###### Case 1: $𝐻10≥7$
we need to calculate $P(H_{10}\geq 7)$
$$P(H_{n}\geq 7)=\sum_{i=7}^{10}{10\choose i}(0.5)^i(0.5)^{10-i}$$
This can be calculated as:

$$P(H_{n}\geq 7)=\sum_{i=7}^{10}{10\choose 7}(0.5)^{10}+{10\choose 8}(0.5)^{10}+{10\choose 9}(0.5)^{10}+{10\choose 10}(0.5)^{10}$$

###### Case 2: $𝐻100≥70$
we need to calculate $P(H_{100}\geq 70)$
$$P(H_{100}\geq 70)=\sum_{i=70}^{100}{100\choose i}(0.5)^i(0.5)^{100-i}$$
This can be calculated similarly, but due to the large number of terms, it's typically computed using statistical software.

#### b) Using the central limit theorem
he CLT approximates the distribution of the sum of a large number of i.i.d. random variables by a normal distribution. For a Binomial distribution $H_n$ with parameters $n$ and $p$:
$$\text{Mean: }\mu=np$$
$$\text{Variance: }\sigma^2=np(1-p)$$
We can approximate $H_n$ by a normal distribution $N(np,np(1-p))$. The probability $$P(H_n\geq k)\approx P\left( Z\geq \frac{k-np}{\sqrt{ np(1-p) }} \right)$$
Where $Z$ is a standard normal variable.
###### Case 1: $𝐻_{10}≥7$
$$\mu=10*0.5=5$$
$$\sigma=\sqrt{ 10*0.5*0.5}=\sqrt{ 2.5 }\approx1.58$$
$$P(H_{10}\geq 7)\approx P\left( Z\geq \frac{7-5}{\sqrt{ 10*0.5*0.5}} \right)=$$
$$P\left( Z\geq \frac{7-5}{1.58} \right)=$$
$$=P(Z\geq1.27)$$
Using standard normal tables or a calculator
$$P(Z\geq1.27)\approx 1-0.8980=0.1020$$

###### Case 2: $𝐻_{100}≥70$
$$\mu=100*0.5=50$$
$$\sigma=\sqrt{ 100*0.5*0.5}=\sqrt{ 25 }=5$$

$$P(H_{100}\geq 70)\approx P\left( Z\geq \frac{70-0}{\sqrt{ 100*0.5*0.5}} \right)=$$
$$P\left( Z\geq \frac{70-50}{5} \right)=$$
$$=P(Z\geq4)$$
Using standard normal tables or a calculator
$$P(Z\geq 4)\approx 1-0.99997=0.00003$$

