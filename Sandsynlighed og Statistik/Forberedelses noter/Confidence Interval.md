# [[Parameter Estimation]]
A confidence interval is a range of values that is likely to contain the true population parameter with a certain level of confidence. In the case of the population mean, the equation you mentioned allows us to estimate the sample mean ($\hat{\mu}$) based on the observed data.
$$\hat{µ} = \frac{1}{n} \sum \limits _ {i=1} ^{n} X_{i} ~ N (µ, \frac{σ^2}{n})$$
- $\hat{\mu}$ This represents the estimate of the population mean µ. The hat symbol (\hat{}) is often used to denote an estimate.
- $X_i$ hese are the individual observations or values in the sample. The subscript "i" indicates the i-th observation.
- n: This represents the size of the sample, or the number of observations.
- $N(µ, σ^2/n)$ This represents the distribution of the sample mean. The sample mean is assumed to follow a normal distribution with mean µ and variance $\frac{\sigma^2}{n}$ 
The equation also provides information about the distribution of the sample mean. It states that the sample mean follows a normal distribution with mean µ and variance σ^2/n. The variance of the sample mean decreases as the sample size increases, reflecting a more precise estimation of the population mean.

## The confidence interval is found as:
$$\hat{µ} ± Z_{value} * (\frac {σ}{n})$$
- $\hat{\mu}$ This represents the sample mean, which is an estimate of the population mean.
- Z-value: This is the critical value from the standard normal distribution corresponding to the desired confidence level. It determines the width of the confidence interval.
- σ: This is the population standard deviation, which is assumed to be known.
- n: This represents the sample size, i.e., the number of observations in the sample.
- This equation is applicable in situations where you have a known population standard deviation and want to estimate the population mean based on a sample. It is commonly used in statistical inference and hypothesis testing to make conclusions about the population mean using sample data.
# z-score
## 2-sided CI using z-score
To find the two-sided confident interval using the z_score from a sample using this formular
$$CI = \left(\text{{sample\_mean}} - \text{{z\_score}} \cdot \frac{{\text{{sigma}}}}{{\sqrt{n}}}, \text{{sample\_mean}} + \text{{z\_score}} \cdot \frac{{\text{{sigma}}}}{{\sqrt{n}}}\right)$$
## 1-sided CI using z-score
using that formula, to find 1-sided confidence interval using z-score
$$CI lower boundery = \left(\text{{sample\_mean}} - \text{{z\_score}} \cdot \frac{{\text{{sigma}}}}{{\sqrt{n}}}\right)$$
$$CI upper aboundery = \left(\text{{sample\_mean}} + \text{{z\_score}} \cdot \frac{{\text{{sigma}}}}{{\sqrt{n}}}\right)$$
# T-score
## CI using T-score with unknown variance
Coin toss example, determining if the coin is a fair coin Rejection mean this is a type I error
$$Threshold_{a}=t_{score}\frac{\sigma}{\sqrt{ n }}$$
$$sample_{mean}=\frac{1}{n}\sum_{i=1}^n\{samples\}_{i}$$




# Examples from [Kilde](https://github.com/agangster1/Sandsynlighed-og-statestik-formelsamling/blob/main/MM4_Hypothesis%20testing%201.ipynb)

## Example 2-sided CI using z-score
```python
import numpy as np
import math
from scipy.stats import norm

#inset the observations in a array
sample = [176.2, 157.9, 160.1, 180.9, 165.1, 167.2, 162.9, 155.7, 166.2]

#Based on the array we calculate the mean
sample_mean = np.mean(sample)

#choose one of the three confidence levels
#standards being 0.1, 0.05, 0.01
confidence_level = 0.05
conf_lvl_pro = (1 - confidence_level)*100

#the z_score of the most common confidence levels is shown and used here
z_score = norm.ppf(1-confidence_level/2)

#sigma is the confidence interval
#offent shown as +-sigma
#also known as standard error
#this is the number being squred
sigma = np.std(sample)

#based on the array we calculate the sample size
n = len(sample)

#Then to Confidence interval is being calculated
CIlower = (sample_mean - z_score * sigma / math.sqrt(n))
CIupper = (sample_mean + z_score * sigma / math.sqrt(n))

print(f"The {conf_lvl_pro}% confidence interval is {CIlower}, {CIupper}.")
```

```python
import numpy as np
import math
from scipy.stats import norm

#inset the observations in a array
sample = [176.2, 157.9, 160.1, 180.9, 165.1, 167.2, 162.9, 155.7, 166.2]

#Based on the array we calculate the mean
sample_mean = np.mean(sample)

#choose one of the three confidence levels
#standards being 0.1, 0.05, 0.01
confidence_level = 0.05
conf_lvl_pro = (1 - confidence_level)*100

#the z_score of the most common confidence levels is shown and used here
z_score = norm.ppf(1-confidence_level/2)

#sigma is the confidence interval
#offent shown as +-sigma
#also known as standard error
#this is the number being squred
sigma = 0.02

#based on the array we calculate the sample size
n = len(sample)

#Then to Confidence interval is being calculated
CIlower = (sample_mean - z_score * sigma / math.sqrt(n))
CIupper = (sample_mean + z_score * sigma / math.sqrt(n))

Expected_result_for_h0 = 170

print(f"Testing for an expected value {Expected_result_for_h0}")
print(f"With {conf_lvl_pro}% confidence, the interval is between {CIlower}, {CIupper}.")

if CIlower < Expected_result_for_h0 < CIupper:
    print("Therefore h0 is accepted")
else:
    print("Therefore h0 is rejected")
```

## Example 1-sided CI using z-score
```python
import numpy as np
import math
from scipy.stats import norm

#inset the observations in a array
sample = [8.18, 8.17, 8.16, 8.15, 8.17, 8.21, 8.22, 8.16, 8.19, 8.18]

#Based on the array we calculate the mean
sample_mean = np.mean(sample)

#choose one of the three confidence levels
#standards being 0.1, 0.05, 0.01
confidence_level = 0.05
conf_lvl_pro = (1 - confidence_level)*100

#the z_score of the most common confidence levels is shown and used here
z_score = norm.ppf(1-confidence_level)

#sigma is the confidence interval
#offent shown as +-sigma
#also known as standard error
#this is the number being squred
sigma = 0.02

#based on the array we calculate the sample size
n = len(sample)

#Then to Confidence interval is being calculated
CIlower = (sample_mean - z_score * sigma / math.sqrt(n))
CIupper = (sample_mean + z_score * sigma / math.sqrt(n))

print(f"With {conf_lvl_pro}% confidence, the interval is below {CIupper}.")

print("\n ----------------------------------------------- \n")

print(f"With {conf_lvl_pro}% confidence, the interval is above {CIlower}.")
```

### Then preforming the h0 testing with one-sided confidence intervals
```python
import numpy as np
import math
from scipy.stats import norm

#inset the observations in a array
sample = [8.18, 8.17, 8.16, 8.15, 8.17, 8.21, 8.22, 8.16, 8.19, 8.18]

#Based on the array we calculate the mean
sample_mean = np.mean(sample)

#choose one of the three confidence levels
#standards being 0.1, 0.05, 0.01
confidence_level = 0.05
conf_lvl_pro = (1 - confidence_level)*100

#the z_score of the most common confidence levels is shown and used here
z_score = norm.ppf(1-confidence_level)

#sigma is the confidence interval
#offent shown as +-sigma
#also known as standard error
#this is the number being squred
sigma = 0.02

#based on the array we calculate the sample size
n = len(sample)

#Then to Confidence interval is being calculated
CIlower = (sample_mean - z_score * sigma / math.sqrt(n))
CIupper = (sample_mean + z_score * sigma / math.sqrt(n))

Expected_result_for_h0 = 8.2

print(f"Testing for an expected value {Expected_result_for_h0}")
print(f"With {conf_lvl_pro}% confidence, the interval is above {CIlower}.")

if CIlower < Expected_result_for_h0:
    print("Therefore h0 is accepted")
else:
    print("Therefore h0 is rejected")

print("\n ----------------------------------------------- \n")

print(f"Testing for an expected value {Expected_result_for_h0}")
print(f"With {conf_lvl_pro}% confidence, the interval is below {CIupper}.")

if CIupper < Expected_result_for_h0:
    print("Therefore h0 is accepted")
else:
    print("Therefore h0 is rejected")
```


## Example T-score and threshold coin toss (a [[Bernoulli rv]])

```python
import random
import numpy as np
import math
from scipy.stats import t

def bernoulli(p):
    #random.random gives a random value between 0 and 1
    if random.random() < p:
        return 1
    else:
        return 0

# Testing the Bernoulli distribution
n = 100

#p_success is excepted probability of the chosen result
#in a coin toss both are 50% and there is only two
p_success = 0.5

#confidence level is the alpha
confidence_level = 0.05
conf_lvl_pro = (1 - confidence_level)*100

#samples is the randomly generated sample of coin tosses
samples = [bernoulli(p_success) for _ in range(n)]

# μ^ is the estimated mean, from the samples
sample_mean = np.mean(samples)

#test result is the distance from the known probability to the sample mean from the generated sample
Test_result = np.round(abs(sample_mean - p_success), 3)

#sigma is the standard deviation of the sample
sigma = np.std(samples, ddof=0)

#T score is the distance from the sample mean contained within the threshold
t_score = abs(t.ppf(confidence_level/2, n-1))

# a is the threshold for acceptance
a = t_score * sigma / math.sqrt(n)

print(f"Testing if the sample mean is acceptable knowing the excepted probability")

print(f"With a {conf_lvl_pro}% confidence the threshold is {a}")

if a > Test_result:
    print(f"Therefore h0 is accepted, given a sample mean of {sample_mean}")
else:
    print(f"Therefore h0 is rejected, given a sample mean of {sample_mean}")
```
## finding CI using T-score with unknown variance:
```python
import numpy as np
import math
from scipy.stats import t

#inset the observations in a array
sample = [36.1, 40.2, 33.8, 38.5, 42, 35.8, 37, 41, 36.8, 37.2, 33, 36]

#Based on the array we calculate the mean
sample_mean = np.mean(sample)

#Based on the array we calculate the standard deviation
sample_std = np.std(sample, ddof=1)

#based on the array we calculate the sample size
n = len(sample)

#insert the procent of confidence needed
#standards being 0.1, 0.05, 0.01
alpha = 0.05

#Based on the array and alpha the t score for two sided is calculated
t_score_two = abs(t.ppf(alpha/2, n-1))

#Based on the array and alpha the t score for one sided is calculated
t_score_one = abs(t.ppf(alpha, n-1))

#Then a lower Confidence interval is being calculated
CIlower = (sample_mean - t_score_one * sample_std / math.sqrt(n))
#Then a upper Confidence interval is being calculated
CIupper = (sample_mean + t_score_one * sample_std / math.sqrt(n))

#Then to Confidence interval is being calculated
CI = (sample_mean - t_score_two * sample_std / math.sqrt(n), sample_mean + t_score_two * sample_std / math.sqrt(n))

print(f"With {(1-alpha)*100}% confidence, the interval is below {CIupper}.")
print(f"With {(1-alpha)*100}% confidence, the interval is above {CIlower}.")
print(f"With {(1-alpha)*100}% confidence, the interval is {CI}.")
```
### What is this #StatsTODO

```python
import numpy as np
import math
from scipy.stats import t

#Based on the array we calculate the mean
sample_mean = 90.9

#Based on the array we calculate the standard deviation
sample_std = 12.2

#based on the array we calculate the sample size
n = 29

#insert the procent of confidence needed
#standards being 0.1, 0.05, 0.01
alpha = 0.05

#Based on the array and alpha the t score for two sided is cal  culated
t_score_two = abs(t.ppf(alpha/2, n-1))

#Based on the array and alpha the t score for one sided is calculated
t_score_one = abs(t.ppf(alpha, n-1))

#Then a lower Confidence interval is being calculated
CIlower = (sample_mean - t_score_one * sample_std / math.sqrt(n))
#Then a upper Confidence interval is being calculated
CIupper = (sample_mean + t_score_one * sample_std / math.sqrt(n))

#Then to Confidence interval is being calculated
CI = (sample_mean - t_score_two * sample_std / math.sqrt(n), sample_mean + t_score_two * sample_std / math.sqrt(n))

print(f"With {(1-alpha)*100}% confidence, the interval is below {CIupper}.")
print(f"With {(1-alpha)*100}% confidence, the interval is above {CIlower}.")
print(f"With {(1-alpha)*100}% confidence, the interval is {CI}.")
```
