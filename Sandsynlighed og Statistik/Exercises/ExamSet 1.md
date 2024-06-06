# Problem P.1
In order to produce a robot, a company purchases a special chip from external suppliers. 10% of these chips are bought from AuroraRed; 15% are from BluePrint; and the rest 75% are from ColorCode. Some of the chips are defective. It is known that the percentage of defective chips made by AuroraRed, BluePrint and ColorCode are 8%, 5%, and 1%, respectively. A robot is selected at random. It is tested and it is found out that it containes a defective chip. What is the probability that this chip is produced by BluePrint?
- 10% chips come from AuroraRed
- 15% chips come from BluePrint
- 75% chips come from ColorCode
- some chips are defective
	- 8% AuroraRed chips are defective 
	- 5% BluePrint chips are defective
	- 1% ColorCode chips are defective
- Chip for robot is selected at random
- **What is the probability that this chip is produced by BluePrint?**

0.15 prob that it is used in bot
0.05 prob that it is defective
$C = \{1, 2, 3\}$ (the three manufactorers)
$D$ : The RV for robots failure: **Bernoulli**
$D_{flat}$ : Which chip fuck
$D_{flat}=\{1,2,3\}$

$P(A)=\frac{10}{100}=0.10$ Chip used in a given bot is by AuroraRed

$P(C)=\frac{70}{100}=0.75$ Chip used in a given bot is by ColorCode



$(C=2|D)$


$P(D_{A})=\frac{8}{100}=0.08$ Bot is faulty (defective) and made by BluePrint
$P(D_{C})=\frac{1}{100}=0.01$ Bot is faulty (defective) and made by BluePrint
2.3% chance robot is screwed

$P(S)=\frac{25}{125}=0.2$ mail is spam

$P(S_{flat})=1-0.023=0.977$ mail is not good

$P(D_{flat}|S)=1-0.98=0.02$ mail is spam and is not put in spam folder
$P(D|S)=0.98$  The mail is spam, and is put in spam-folder

$P(D|S_{flat})=0.07$ mail is not spam, and is put in spam-folder

$P(D_{flat}|S_{flat})=1-0.07=0.93$ mail is not spam and is not put in spam folder


$P(D|B)=\frac{5}{100}=0.05$ Bot is faulty (defective) and made by BluePrint
$P(B)=\frac{15}{100}=0.15$ Chip used in a given bot is by BluePrint

$P(D_{AuroraRed})P(D)*P(C_{AuroraRed})=0.08*0.10=0.008$
$P(D_{BluePrint})P(D)*P(C_{B})=0.01*0.75=0.0075$
$P(D_{ColorCode})P(D)*P(C_{ColorCode})=0.05*0.15=0.0075$
$P(D)=0.008+0.0075+0.0075=0.023$ 

$$P(B|D)=\frac{P(D|B)\cdot P(B)}{P(D)}$$
$$P(B|D)=\frac{P(\text{faulty chip, by blueprint})\cdot P(\text{chip made by blueprint})}{P(\text{chip is defect})}$$

$$=\frac{0.005\cdot 0.15}{0.023}$$
$$=0.0326$$

# Problem P.2
Suppose that sensor temperature measurements are normally distributed with mean 0 degrees and standard deviation 1 degrees. Find the probabilities that a randomly selected temperature measurement agrees with each of the following:
1) Greater than 0 degrees
2) less than -2 degrees
3) between 0.5 and 1.5 degrees
4) is exactly 0 degrees

> [!NOTE] Info from problem
> - **normally distributed**
> - **mean**: 0
> - **std. deviaton:** 1
> - **Problem:** *probabilities that a randomly selected temperature measurement agrees with* (1), (2), (3), (4)

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
### Please answer an additional question: 
What characteristics must a normal probability distribution have to be a standard normal probability distribution?
1. **Mean (μ) of Zero**: The mean (average) of the distribution must be 0. This centers the distribution at zero on the horizontal axis.
2. **Standard Deviation (σ) of One**: The standard deviation (a measure of the spread or dispersion of the distribution) must be 1. This standardizes the spread of the distribution so that it conforms to the standard normal scale.
3. **Symmetry**: The distribution must be symmetric about the mean. This means that the left and right sides of the distribution are mirror images of each other.
4. **Bell-shaped Curve**: The distribution must have the characteristic bell shape of a normal distribution, indicating that data near the mean are more frequent in occurrence than data far from the mean.

When these conditions are met, the distribution is known as the standard normal distribution, often denoted as **N(0,1)**.


# Problem P.3
A student takes a 10-question multiple-choice exam with four choices for each question. He/ she does not know the right answers and guesses on each question. Calculate the probability of guessing at least 8 out of 10 correctly

> [!NOTE] Info from problem
> - n: 10
> - $C=\{0,1,2,3\}$
> - probabilities equal
> - **problem:** *find prob of guessing at least 8 out of 10 correctly*

$N$ answer is incorrect
$Y:$ answer is correct
$P(Y)=\frac{1}{4}=0.25$
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


# Problem S.1
According to ourworldindata.org, $92\%$ of the households in the US had a microwave in 2017. You’re making a market study for a danish company and visited $200$ households in Denmark. Out of these $200$ households, $175$ have a microwave.

> [!NOTE] Info from problem (Who has **Microwave**)
> - 92% of households in **US**, 2017
> - ***n:*** 200, **DK**
> - 175 have a microwave, **DK**
> - **problem:** Estimate prob that a **danish** household has microwave
> - **Problem2:** 5% significance, $H_0$: percentage of **danish** households with a microwave is greater than that of **US**

### Estimate the probability that a danish household has a microwave.
0.875
### Your company assumes that the percentage of danish households with a microwave is greater than that of US households in 2017. Can you reject this claim with 5% significance? Provide the means to support your conclusion.
- Calculate the sample proportion (p_hat) which is the proportion of Danish households with a microwave.
- Calculate the hypothesized population proportion (p0) which is the proportion of US households with a microwave in 2017.
- Calculate the standard error (SE) using the formula SE = sqrt[(p0 * (1 - p0)) / n], where n is the number of households visited in Denmark.
- Calculate the z-score using the formula z = (p_hat - p0) / SE.
- Compare the z-score with the critical z-value for a one-tailed test at 5% significance level (z_critical = 1.645). If the z-score is greater than the critical z-value, reject the null hypothesis.
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
    print("We reject the null hypothesis.")  
else:  
    print("We fail to reject the null hypothesis.")
```
he estimated probability that a Danish household has a microwave is 0.875
z-score = -2.3457871581420937
critical z-value = 1.6448536269514722
We fail to reject the null hypothesis. There is not enough evidence to conclude that the proportion of Danish households with a microwave is significantly greater than the proportion of US households with a microwave in 2017 at a 5% significance level.
# Problem S.2
Table I shows the yearly average CO2 emissions per capita in 2021 for numerous countries in America and Europe


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
### Obtain the 90% confidence interval for the CO2 emissions per capita in America and Europe

Europe: Confidence Interval (90.0%): (4.603065436166803, 7.111934563833197)
America: Confidence Interval (90.0%): (0.859632305634789, 9.15236769436521)
```python
import math  
import numpy as np  
from scipy.stats import norm  
  
# To estimate the population mean µ, you calculate the sample mean by taking the sum of all observations and dividing it by the sample size:  
  
def calculate_confidence_interval(data, confidence_level):  
    n = len(data)  # Sample size  
    sample_mean = sum(data) / n  # Sample mean  
  
    # Standard deviation of the sample    sample_std = math.sqrt(sum([(x - sample_mean) ** 2 for x in data]) / (n - 1))  
  
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
### Can you conclude with 0.1 significance that the mean CO2 emissions per capita in Europe than in America are equal?

> [!NOTE] info from problem
> - $mean\_emissions\_eu = mean\_emissions\_america$
> - $0.1 \text{ significance}$

# Problem S.3
Table II shows the number of oil spills (from tankers) recorded globally at every year from 2010 to 2022
| year | \# of oil spills |

| 2010 | 9   |
| ---- | --- |
| 2011 | 5   |
| 2012 | 7   |
| 2013 | 8   |
| 2014 | 5   |
| 2015 | 8   |
| 2016 | 5   |
| 2017 | 6   |
| 2018 | 7   |
| 2019 | 3   |
| 2020 | 4   |
| 2021 | 6   |
| 2022 | 7   |


| ---- | ------------- |
| 2010 | 9                |
| 2011 | 5                |
| 2012 | 7                |
| 2013 | 8                |
| 2014 | 5                |
| 2015 | 8                |
| 2016 | 5                |
| 2016 | 6                |
| 2018 | 7                |
| 2019 | 3                |
| 2020 | 4                |
| 2021 | 6                |
| 2022 | 7                |
### Obtain the sample mean and variance for the yearly number of oil spills.

The sample mean of the yearly number of oil spills is 6.153846153846154
The sample variance of the yearly number of oil spills is 2.9743589743589745
```python
n= 13  # SUPERFLUOUS?
x = np.array([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])  
y = np.array([9, 5, 7, 8, 5, 8, 5, 6, 7, 3, 4, 6, 7])  
  
# Calculate the sample mean  
mean = np.mean(y)  
  
# Calculate the sample variance  
variance = np.var(y, ddof=1)  # ddof=1 provides an unbiased estimator of the variance  
  
print(f"The sample mean of the yearly number of oil spills is {mean}")  
print(f"The sample variance of the yearly number of oil spills is {variance}")
```
#### Obtain the linear regression parameters $\hat{\beta}_{0}$ and $\hat{\beta_{1}}$ 

```python
# Obtain the linear regression parameters  
beta1, beta0 = np.polyfit(x, y, 1)  
  
print(f"The linear regression parameters are: beta0 = {beta0}, beta1 = {beta1}")
```
The linear regression parameters are: beta0 = 360.61538461543046, beta1 = -0.17582417582419863
![[Pasted image 20240606010057.png]]
### Estimate the mean number of oil spills for 2023.
The estimated mean number of oil spills for 2023 is 4.923076923076621
