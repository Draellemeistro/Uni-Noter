### For poisson process:

> [!NOTE] Poisson process
> Poisson process is useful when you encounter scenarios that involve counting the number of events occurring within a given interval or spatial region, where the events are assumed to happen independently and at a constant average rate.
> $$P(k,\lambda)=\frac{e^{-\lambda}*\lambda^k}{k!}$$


```python
import numpy as np
import math
from scipy.stats import norm
from scipy.stats import t
import matplotlib.pyplot as plt

# True average temperature
mu = 6

# Known variance if not know put 1 and only look at the Ta/2,n-1
sigma2 = 1

# Sample sizes
n1 = 10
n2 = 1000

#choose one of the three confidence levels also known as alpha
#standards being 0.1, 0.05, 0.01
alpha = 0.01

conf= (1 - alpha)*100
conf = str(conf)
#the z_score of the most common confidence levels is shown and used here
z_score = norm.ppf(1-alpha/2)

#sigma is the confidence interval
#offent shown as
#+-sigma
#this is the number being squred
sigma = math.sqrt(1)

# Generate a random sample of temperatures
x = mu + np.random.randn(n2)*np.sqrt(sigma2)
y = mu + np.random.randn(n1)*np.sqrt(sigma2)

# Calculate MLEs for different sample sizes
mu_hat1 = np.mean(y[:n1])
mu_hat2 = np.mean(x[:n2])

CIz1 = (mu_hat1 - z_score * sigma / math.sqrt(n1), mu_hat1 + z_score * sigma / math.sqrt(n1))
CIz2 = (mu_hat2 - z_score * sigma / math.sqrt(n2), mu_hat2 + z_score * sigma / math.sqrt(n2))

#Based on the created array and alpha the t score is calculated
t_score1 = abs(t.ppf(alpha/2, n1-1))
#Based on the array and alpha the t score is calculated
t_score2 = abs(t.ppf(alpha/2, n2-1))

#Then to Confidence interval is being calculated
CIt1 = (mu_hat1 - t_score1 * sigma / math.sqrt(n1), mu_hat1 + t_score1 * sigma / math.sqrt(n1))
#Then to Confidence interval is being calculated
CIt2 = (mu_hat2 - t_score2 * sigma / math.sqrt(n2), mu_hat2 + t_score2 * sigma / math.sqrt(n2))

# Count samples outside CIs
frac_outside1 = sum((y[:n1] < CIt1[0]) | (y[:n1] > CIt1[1])) / n1
frac_outside2 = sum((x[:n2] < CIt2[0]) | (x[:n2] > CIt2[1])) / n2

# Plot the collected measurements and the estimated MLEs
plt.plot(x, label="Measurements")
plt.axhline(y=mu_hat1, color='r', linestyle='--', label=r"$\hat{\mu}_{10}$")
plt.axhline(y=mu_hat2, color='g', linestyle='--', label=r"$\hat{\mu}_{1000}$")

plt.axhline(y=mu, color='b', linestyle='--', label="True average")

plt.axhline(y=CIz1[0], color='r', linestyle=':', label=r"$CI_{10}$")
plt.axhline(y=CIz1[1], color='r', linestyle=':', label=r"$CI_{10}$")
plt.axhline(y=CIz2[0], color='g', linestyle=':', label=r"$CI_{1000}$")
plt.axhline(y=CIz2[1], color='g', linestyle=':', label=r"$CI_{1000}$")

# Print results
print("True average temperature: mu =", mu)
print("Sample sizes: n1 =", n1, ", n2 =", n2)
print("MLEs: mu_hat1 =", mu_hat1, ", mu_hat2 =", mu_hat2)

print(f"The {conf}% confidence interval is using Za/2 {CIz1} when n is {n1}.")
print(f"The {conf}% confidence interval is using Za/2 {CIz2} when n is {n2}.")

print(f"The {conf}% confidence interval is using Ta/2,n-1 {CIt1} when n is {n1}.")
print(f"The {conf}% confidence interval is using Ta/2,n-1 {CIt2} when n is {n2}.")

print(f"The fraction outside is {frac_outside1 * 100}% when n is {n1}.")
print(f"The fraction outside is {frac_outside2 * 100}% when n is {n2}.")

plt.title("99% conf")
plt.legend()
plt.xlabel("Sample index")
plt.ylabel("Temperature")
plt.show()
# True average temperature: mu = 6
# Sample sizes: n1 = 10 , n2 = 1000
# MLEs: mu_hat1 = 5.5659818058951975 , mu_hat2 = 6.003987449651919
# The 99.0% confidence interval is using Za/2 (4.7514330595932215, 6.380530552197174) when n is 10.
# The 99.0% confidence interval is using Za/2 (5.922532575021721, 6.085442324282116) when n is 1000.
# The 99.0% confidence interval is using Ta/2,n-1 (4.538293571889102, 6.593670039901293) when n is 10.
# The 99.0% confidence interval is using Ta/2,n-1 (5.9223766641799624, 6.085598235123875) when n is 1000.
# The fraction outside is 10.0% when n is 10.
# The fraction outside is 93.89999999999999% when n is 1000.
```
![[Pasted image 20240605125137.png]]

```python
import numpy as np
import matplotlib.pyplot as plt

# True average temperature
mu = 6

# Known variance
sigma2 = 1

# Sample sizes
n1 = 10
n2 = 1000

# Generate a random sample of temperatures
x = mu + np.random.randn(n2)*np.sqrt(sigma2)

# Calculate MLEs for different sample sizes
mu_hat1 = np.mean(x[:n1])
mu_hat2 = np.mean(x[:n2])

# Plot the collected measurements and the estimated MLEs
plt.plot(x, label="Measurements")
plt.axhline(y=mu_hat1, color='r', linestyle='--', label=r"$\hat{\mu}_{10}$")
plt.axhline(y=mu_hat2, color='g', linestyle='--', label=r"$\hat{\mu}_{1000}$")
plt.legend()
plt.xlabel("Sample index")
plt.ylabel("Temperature")
plt.show()
```
![[Pasted image 20240605125212.png]]
```python
import math

def poisson_probability(lmbda, k):
    """
    Calculates the probability of a Poisson process.

    Parameters:
    - lmbda: The average rate of the Poisson process. How many events are expected to happend within the frame
    - k: The number of events to calculate the probability for.

    Returns:
    - The probability of k events occurring in a Poisson process with rate lmbda.
    """
    return (math.exp(-lmbda) * (lmbda ** k)) / math.factorial(k)

# Example usage:
# 5 cars are expected to cross the brigde every hour
# what is the probability that only 3 cars cross the bridge at any given hour?:
lmbda = 5  # Average rate of the Poisson process
k = 3  # Number of events

probability = poisson_probability(lmbda, k)
print(f"{probability}")
# 0.14037389581428056
```

> [!NOTE] Maximum Likelihood Estimation (MLE):
> $$\text{MLE}(\theta) = \arg\max_{\theta} \prod_{i=1}^{n} f(x_i; \theta)$$
