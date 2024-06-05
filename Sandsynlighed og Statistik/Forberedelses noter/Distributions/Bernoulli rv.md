An experiment with 2 possible outcomes (*success* or *failure*) is called a **Bernoulli trial**. The indicator of event A is called the Bernoulli r.v. since it describes outcome of a Bernoulli trial.

> [!NOTE] ELI5: Bernoulli
> Every Bernoulli trial, regardless of the definition of A, is equivalent to the ***tossing of a biased coin***.

![[Pasted image 20240602153113.png]]

# $E[X] Var(X)$

$$E[I]=p$$
$$Var(I)=p(1-p)$$
# Example
a r.v. I is an indicator of the event A The expected value of the indicator of an event is equal to the probability event:
$$I = \begin{cases} 1 & \text{if A occurs} \\ 0 & \text{if A does not occur} \end{cases}$$
$$E[I]=1*P(A)+0*P(A^c)=P(A)$$
$$Var(I) = E[I^2]-E[I]^2 = E[I]-E[I]^2 = E[I]*(1-E[I])=P(A)P(A^c)$$
```python
def bernoulli_expected_value(p):
    # Calculate the expected value of a Bernoulli random variable
    return p

def bernoulli_variance(p):
    # Calculate the variance of a Bernoulli random variable
    return p * (1 - p)

# Example usage
p = 0.6  # Probability of success (event A)

expected_value = bernoulli_expected_value(p)
variance = bernoulli_variance(p)

print("Expected Value:", expected_value)
print("Variance:", variance)
# Expected Value: 0.6
# Variance: 0.24
```

