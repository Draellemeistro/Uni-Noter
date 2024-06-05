#The BER of a communication channel is 10^-3. What is a probability that a block of 1000 bits has five or more errors?  
# using the poisson r.v. in python
from scipy.stats import poisson

lambda_val = 1000 * 10**-3  # Mean of the Poisson distribution (λ = np)

# Calculate the probability using the survival function (1 - cumulative distribution function)
probability = 1 - poisson.cdf(4, lambda_val)  # P(X >= 5) = 1 - P(X <= 4)

print(f"The probability of having five or more errors in a block of 1000 bits is: {probability:.4f}")
# The probability of having five or more errors in a block of 1000 bits is: 0.0037
