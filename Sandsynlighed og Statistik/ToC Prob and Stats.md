# Probability part
## [[ProbSession 1]]
- 
## [[ProbSession 2]]
- [[random variables]]
- [[Discrete Random Variables]]
- [[Probability Mass Function (PMF)]]
- [[Continuous Random Variables and their Distributions]]
- [[Probability Density Function (PDF)]]
- [[Cumulative distribution function (CDF)]]
- [[Expected Value and Variance]]
- [[Jointly distributed random variabless]]
- [[Independent random variabless]]
## [[ProbSession 3]]
- Special Distributions
	- Bernoulli Distribution
	- Geometric Distribution
	- Binomial Distribution
		- Binomial random variable as a sum of Bernoulli random variables
	- Negative Binomial (Pascal) Distribution
	- Hypergeometric Distribution
	- Poisson Distribution
		- Poisson as an approximation for binomial
	- Uniform Distribution
	- Exponential Distribution
	- Normal (Gaussian) Distribution
	- Gamma Distribution
	- Other Distributions
	- 
## [[ProbSession 4]]
# Stats
## Session 1: Introduction to statistics and parameter estimation
- Introduction
	- Definition and classification of statistics
	- Law of large numbers
	- the normal (Gaussian) distribution
	- the central limit theorem
- Parameter estimation
	- Intro. to parameter estimation
	- Estimating mean and variance
	- Maximum likelihood estimation (MLE)
## Session 2: Confidence intervals and regression
- Confidence intervals
	- Definition and classification of confidence intervals
	- Finding confidence intervals with known variance
	- Finding confidence intervals with unknown variance
- Regression
	- Linear regression
	- Least square estimators
	- Residual analysis
## Session 3: Hypothesis testing
- Introduction to hypothesis testing
	- Definition and classification of tests
	- Tests with one normally distributed population and known variance
- Advanced hypothesis testing
	- Tests with one normally distributed population and unknown variance
	- Tests with multiple populations
# [[ProbBasics]]
- Variance
- Standard deviation
- Covariance
- Correlation
- Events
	- when all events are equally likely to happen
	- any event E, the probability P(E) is non-negative
	- For any two disjoint events E and F, the probability of their union is the sum of their individual probabilities
- Sampling
	- Sampling with or without replacement
	- Sampling without Replacement and with Ordering
	- Sampling without Replacement and without Ordering
	- Sampling with replacement and without ordering
	- Bayes formula
- [[Cumulative distribution function (CDF)]]
- [[Probability Mass Function (PMF)]] for discrete R.V
- [[Probability Density Function (PDF)]] continuous r.v
- Mixed type
- multi rv Joint distribution functions
	- Multiple r.v joint CDF:
	- |Joint distributed discrete r.vs. [[joint PMF]]
	- Jointly distributed continous r.vs.
	- independent r.v. You can split the formulas
		- CDF
		- PMF and PDF
	- relationship between two random variables|relationship between two random variables
- [[Bernoulli rv]]
- [[Binomial rv]]
- [[Geometric rv]]
- hypergeometric rv (see: [[Geometric rv]])
- [[Poisson rv]]
- [[Uniform rv]]
		-[[Probability Density Function (PDF)]]
		- [[Cumulative distribution function (CDF)]]
- [[Exponential rv]]
		- [[Probability Density Function (PDF)]]
		- [[Cumulative distribution function (CDF)]]
		- Reliability function: (The probability that X is greater than some number)
		- Memoryless property
- Poisson process
- Normal r.v. (Gaussian r.v.)
		- [[Probability Density Function (PDF)]]
	- Sample mean:
	- Sample variance:
	- Gaussian distribution:
	- Standard normal distribution:
	- The central limit theorem:



# [[Expectation Variance and Covariance]]
- Expectation E\[X]
	- if X is a continuous RV
- Variance
	- covariance
	- Some useful identities concerning variances
		- Variance of Linear Transformations
		- Variance of constants
		- Variance of shifted rv
		- Correlation coefficient

# [[Multiple random variables]]
- Joint functions
	- [[joint CDF]]
	- [[joint PMF]]
	- [[joint PDF]]
- Conditional distributions
	- [[conditional PDF]]
	- [[conditional PMF]]
	- Example conditional Distributions
- General Stuff
# [[Regression]]
Simple Linear regression
- Least Squares Estimators
	- Least Square Regression
	- Finding the least squares estimates
		- example code-use

# [[Different Distributions]]

> [!NOTE] Distributions
> - **==DISCRETE==**
> 	- **[[Bernoulli rv]]**
> 	- **[[Binomial rv]]**
> 	- **[[Geometric rv]]**
> 	- **[[Poisson rv]]**
> - **==CONTINUOUS??==**
> 	- **[[Uniform rv]]**
> 	- **[[Exponential rv]]**
> 	- Normal?
> 	- Poisson process?

- Properties Discrete Distributions
	- [[Bernoulli rv]]
	- [[Binomial rv]]
	- Computing the binomial distribution function
	- [[Geometric rv]]
		- Hypergeometric rv: see [[Geometric rv]]
	- [[Poisson rv]]
		- Events that can be moddelled by Poisson distribution

# [[Poisson process]]
- For poisson process
- code snippets

# [[test confidence interval]]
- [[Parameter Estimation]]
	- The confidence interval is found as
- z-score
	- 2-sided CI using z-score
	- 1-sided CI using z-score
- T-score
	- CI using T-score with unknown variance
- Code examples:
	- Example 2-sided CI using z-score
	- Example 1-sided CI using z-score
		- Then preforming the h0 testing with one-sided confidence intervals
	- Example T-score and threshold coin toss (a [[Bernoulli rv]])
	- finding CI using T-score with unknown variance
		- What is this #StatsTODO
# [[Parameter Estimation]]
- big ol code example 
- Sample mean
	- estimate the sample mean ($\hat{\mu}$) based on the observed data.
		- The confidence interval is found as
			- Example code
	- The conservative approach or approach 1
		- code example
		- Finding sample size from confidence intervals - using approach 1
			- code example
	- approach 2
		- Code example
			- Finding sample size from confidence intervals - using approach 2
- Sample variance
	- Finding confidence interval
	- finding sample size
# Others
- ## [[Independence and r.v]]
- ## [[formler]]
	- Sample mean
	- Sample variance
	- Law of large numbers
	- Gaussian distribution (normal distribution)
		- Standard normal distribution
		- PDF of normal distribution based on mean and standard deviation
	- multiple RVs
		- The linearity of expectation and sample mean
			- Expectation formula
			- The formula for the sample mean