# Example 1
X and Y are random variables that can take on values 0 and 1. It is known that: $$P(X=0,Y=0)=\frac{1}{2};$$
$$P(X=1,Y=0)=\frac{1}{4};$$
$$P(X=0,Y=1)=\frac{1}{4};$$
$$P(X=1,Y=1)=0 $$
### (A) Explain why the probabilities specified above give us a valid joint pmf
Bernoulli 
$P(X=0,Y=0)=\frac{1}{2};P(X=1,Y=0)=\frac{1}{4};P(X=0,Y=1)=\frac{1}{4}$

$$P(X=0,Y=0)+P(X=1,Y=0)+P(X=0,Y=1)$$
$$\frac{1}{2}+\frac{1}{4}+\frac{1}{4}=1$$
### (B) Write down the pmf of X.



| X\Y       | 0   | 1   |     |
| --------- | --- | --- | --- |
| **0**     | 1/2 | 1/4 | 3/4 |
|  **1**    | 1/4 | 0   | 1/4 |
|           | 3/4 | 1/4 |     |

### (C) Is X a discrete or continuous random variable? Does a distribution for X has a special name or it is a ”no-name” distribution?
X is discrete and a Bernoulli r.v
### (D) Are X and Y independent?
no $P(X=1)=\frac{1}{4}$ and $P(Y=1)=\frac{1}{4}$ 
if independent it should be= $P(X=1,Y=1)=P(X=1)*P(Y=1)=\frac{1}{4}*\frac{1}{4}$

### (E) Calculate the mean and variance for r.v. X.
$E[X]=\frac{1}{4}$ 
$Var(X)=E[(X-E[X])^2]=E[X^2]-E[X]^2$

$E[X^2]=E[X]$
$Var(X)=E[X]-E[X]^2=\frac{1}{4}-\left( \frac{1}{4} \right)^2=\frac{1}{4}\left( 1-\frac{1}{4} \right)=\frac{1}{4}*\frac{3}{4} = \frac{3}{16}$
### (F) Calculate $Cov(X,Y)$
$Cov(X,Y)=E[(X-E[X])*(Y-E[Y])]$ 
$Cov(X,Y)=E[XY]-E[X]*E[Y]$
$E[XY]=$


### (G) calculate $E[4X+8Y-3]$
we know a few things:
- $E[c*X]=c*E[X]$
- $E[X+Y]=E[X]+E[Y]$
- $E[X]=\frac{1}{4}$ (from earlier problems)

therefore:
$$E[4X+8Y-3]$$$$=4E[X]+8E[Y]-3$$
$$=4\frac{1}{4}+8 \frac{1}{4}-3$$
$$=1+2-3=0$$

