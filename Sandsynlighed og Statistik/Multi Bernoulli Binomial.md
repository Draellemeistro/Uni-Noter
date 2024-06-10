# Example 1
### Problem
> [!NOTE] Info from problem
> - 60 games
> 	- 32 games agains class A teams
> 	- 28 games against class B teams
> - independent outcomes
> 	- outcome of a game is a **Bernoulli RV** (*win/lose*)
> - prob. of win
> 	- against class A team: $0.5$
> 	- against class B team: $0.7$
> - $X$: total number of victories this year

1) Is $X$ a Binomial RV?
2) Let $X_A$ and $X_B$ denote, respectively, the number of victories against class **A** and class **B** teams. What are their distributions?
3) What is the relationship between $X$, $X_{A}$ and $X_B$
4) Approximate the probability that the team wins 40 or more games this year
### Code
##### What are the distributions of $X_A$ and $X_B$ ?
``` python
# Parameters  
n_A = 32  
p_A = 0.5  
n_B = 28  
p_B = 0.7  
  
# Define the range of possible wins  
x_A = np.arange(0, n_A + 1)  
x_B = np.arange(0, n_B + 1)  
  
# Calculate the PMF for class A and class B teams  
pmf_A = binom.pmf(x_A, n_A, p_A)  
pmf_B = binom.pmf(x_B, n_B, p_B)  
  
# Plotting the PMF for class A teams  
plt.figure(figsize=(12, 6))  
  
plt.subplot(1, 2, 1)  
plt.bar(x_A, pmf_A, color='blue', alpha=0.7)  
plt.title('PMF of Wins against Class A Teams')  
plt.xlabel('Number of Wins')  
plt.ylabel('Probability')  
plt.grid(True)  
  
# Plotting the PMF for class B teams  
plt.subplot(1, 2, 2)  
plt.bar(x_B, pmf_B, color='green', alpha=0.7)  
plt.title('PMF of Wins against Class B Teams')  
plt.xlabel('Number of Wins')  
plt.ylabel('Probability')  
plt.grid(True)  
  
# Show plots  
plt.tight_layout()  
plt.show()
```

##### relationship between $X$, $X_{A}$ and $X_B$
```python
 ################
 ##
 ## IN ADDITION TO THE CODE FROM (b)
 ##
 ################
 # Calculate the PMF for total wins using convolution  
pmf_total = np.convolve(pmf_A, pmf_B)  
  
# Define the range of possible total wins  
x_total = np.arange(0, n_A + n_B + 1)  
  
# Plotting the PMF for total wins  
plt.figure(figsize=(12, 6))  
plt.bar(x_total, pmf_total, color='purple', alpha=0.7)  
plt.title('PMF of Total Wins')  
plt.xlabel('Number of Wins')  
plt.ylabel('Probability')  
plt.grid(True)  
plt.show()
```

##### Approximate the probability that the team wins 40 or more games this year
```python
# Parameters  
n_A = 32  
p_A = 0.5  
n_B = 28  
p_B = 0.7  
  
# Mean and variance for the normal distributions  
mu_X = n_A * p_A + n_B * p_B  
sigma_X2 = n_A * p_A * (1 - p_A) + n_B * p_B * (1 - p_B)  
sigma_X = np.sqrt(sigma_X2)  
  
# Calculate the probability using the normal approximation  
prob_40_or_more = 1 - 0.5 * (1 + erf((40 - mu_X) / (sigma_X * np.sqrt(2))))  
  
print("Probability of achieving 40 or more wins:", prob_40_or_more)
# Output:  
# Probability of achieving 40 or more wins: 0.0002687997035848194  
# Compare this to the output of exercise4c.py:
```
### Reasoning
Lets start by plotting the individual probabilities for $X$, or rather, the distributions for $X_A$ and $X_B$ **WE NEED TO DO THE FOLLOWING:**
1. Define the parameters for the Binomial distributions for class A and class B teams.
2. 1. Calculate the PMF for the number of wins against class A and class B teams.
$$X_{A}\sim Binomial(32,0.5)$$
$$X_{B}\sim Binomial(28,0.7)$$
##### is $X$ a Binomial RV?
both $X_A$ and $X_B$ are binomial distributions. Both are independent. $X$ as a joint distribution of those two, is simply just the sum of the two binomial distributions: $X=X_A+X_B$

##### What are the distributions of $X_A$ and $X_B$ ?

##### What is the relationship between $X$, $X_{A}$ and $X_B$
To find the total number of wins, we can combine the wins against class A teams and class B teams. Since the total number of wins $X$ is the sum of the two independent Binomial RVs, we need to compute the distribution of the sum. EZ PZ
 $$X=X_{A}+X_{B}$$
##### Approximate the probability that the team wins 40 or more games this year
$$P(X\geq 40)$$
**For a binomial distr. the PMF is given, where 
*n* is total number of games
*k* is number of wins
*p* is prob of win in a single game**
$$\text{PMF: }P(X=k)={n\choose k}p^k(1-p)^{{n-k}}$$
**The CDF gives the prob. of getting *k* or fewer wins:** $$P(X\leq k)=\sum_{i=0}^k{n\choose i}p^i(1-p)^{n-i}$$
**To find $P(X\geq 40)$** the complementary probability can be used: $$P(X\geq 40)=1-P(X\leq 40)=1-P(X\leq 39)$$
==**this means:** find $P(X\leq 39)$ and subtract it from 1==
Since $X_A$ and $X_B$ are independent, we should be able calculate them seperately: 
==!!!!! **PROBLEM: there are not enough games for either of the classes** !!!!!!!!==
To approximate the probability that the team wins 40 or more games, you can sum the probabilities of the PMF from 40 to the maximum number of games.
$$P(X\geq 40)=$$

$$\text{The probability that the team wins 40 or more games is approximately 0.1473}$$

We asssume that the distr. of $X_A$ and $X_B$ can be  approximated by normal distributions:
$N_{A}\sim N(n_{A}p_{A},n_{A}p_{A}(1-p_{A}))$ and $N_{B}\sim N(n_{B}p_{B},n_{B}p_{B}(1-p_{B}))$
the sum of them can be approximated: $X\sim N(\mu_{X},\sigma^2_{X})$ were $\mu_{X}=n_{A}p_{A}+n_{B}p_{B}$  and $\sigma^2_{X}=n_{A}p_{A}(1-p_{A})+n_{B}p_{B}(1-p_{B})$

with these, we approximate: $$P(X\geq 40)=11-\frac{1}{2}\left[ 1+erf\left( \frac{{40-\mu_{X}}}{\sigma_{X}\sqrt{ 2 }} \right) \right]=0.1187$$
