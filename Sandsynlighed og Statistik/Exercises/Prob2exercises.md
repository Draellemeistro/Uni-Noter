![[Sandsynlighed og Statistik/Exercises/ExerciseFiles/Probability_Session2_Exercises.pdf]]

## problemAttempts
### warmup
1. we know marg pdfs of RV X and Y, are we able to find joint pdf
	1. no
2. X cont RV. find $P(X=100)$
	1. 0, continuous. can't find specifc, but small interval is not zer
3. yes
4. no change
5. wat
6. idk

### Prob1

### Prob2
X = time before breaking down, continuous RV
![[Pasted image 20240606153015.png]]
##### what is prob computer will function between 50 and 150hours before breaking down?
The probability that 50 < X < 150 is approximately 0.3834

##### Probability that it will function less than 100
The probability that -1 < X < 100 is approximately 0.6422

```python
from scipy.integrate import quad  
import numpy as np  
from sympy import symbols, exp, oo, integrate, solve  
  
# Define the PDF  
def pdf(x, lambda_value):  
    return lambda_value * np.exp(-x / 100)  
  
# Define the lambda value  
lambda_value = 1/100  
# Adjust this value as needed  
  
# Define the limits of integration  
a = -1  
b = 100  
  
# Perform the integration  
result, _ = quad(pdf, a, b, args=(lambda_value))  
  
print(f"The probability that -1 < X < 100 is approximately {result:.4f}")  
  
  
# Define the symbols  
x, lambda_value = symbols('x lambda_value')  
  
# Define the PDF  
pdf = lambda_value * exp(-x / 100)  
  
# Set up the equation  
equation = integrate(pdf, (x, 0, oo)) - 1  
  
# Solve the equation for lambda  
solution = solve(equation, lambda_value)  
  
print(f"The value of lambda is {solution[0]}")
```
### Prob3
- $X=\{0,1,2,3\}$
- $P(X=2)=P(X=1)$
- $P(X=0)=P(X=3)$
- $P(X=1)=\frac{1}{2}P(X=0)$
- sum of all probabilities is equal to 1
thus: $$2x+2x+x+x=1$$
$$P(X=0)=\frac{1}{3},P(X=3)=\frac{1}{3}$$
$$P(X=1)=\frac{1}{6},P(X=2)=\frac{1}{6}$$

### Prob4
Joint density of **X** and **Y** is
$$f(x)=\{_{0, otherwise}^{xe^{-(x+y)}:x>0,y>0}$$
```python
from sympy import symbols, exp, oo, integrate  
  
# Define the symbols  
x, y = symbols('x y')  
  
# Define the joint density  
f_xy = x * exp(-(x+y))  
  
# Compute the density of X by integrating the joint density over y  
f_x = integrate(f_xy, (y, 0, oo))  
  
# Compute the density of Y by integrating the joint density over x  
f_y = integrate(f_xy, (x, 0, oo))  
  
print(f"The density of X is {f_x}")  
print(f"The density of Y is {f_y}")
```
##### a) Compute the density of X

$$\text{ANSWER:   }f_{X}(x)={{x\cdot e^{-x},\space x>0}\brace{0, \space \text{otherwise}}}$$
$$f_{X}(x)=\int _{-\infty}^{\infty} \,f(x,y) dy=\int_{0}^{\infty}  \, x\cdot e^{-(x+y)}dy  $$
$$=x\cdot e^{-x}\int_{0}^{\infty}  \,e^{-y} dy $$
$$=x\cdot e^{-x} [-e^{-y}]_{0}^{\infty} $$
$$=x\cdot e^{-x}$$

##### b) compute the density of Y
$$f_{Y}(y)={{e^{-y},\space y>0}\brace{0, \space \text{otherwise}}}  $$
![[Pasted image 20240606163329.png]]
##### c) are X and Y independent
They're independent. 

### Prob5

### Prob6

### Prob7
$$f(x)={{a+bx^2,\space 0\leq x\leq 1}\brace{0, \space \text{otherwise}}}$$
if $E[X]=\frac{3}{5}$, find a and b
### Prob8

### Prob9

### Prob10

### Prob11



# Answers
