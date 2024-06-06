
# Example 1
## Code #StatCode 

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
## Problem
Obtain the sample mean and variance for the yearly number of oil spills.

| year | \# of oil spills  |
| ---- | ----------------- |
| 2010 | 9                 |
| 2011 | 5                 |
| 2012 | 7                 |
| 2013 | 8                 |
| 2014 | 5                 |
| 2015 | 8                 |
| 2016 | 5                 |
| 2017 | 6                 |
| 2018 | 7                 |
| 2019 | 3                 |
| 2020 | 4                 |
| 2021 | 6                 |
| 2022 | 7                 |



# Example 2
## Code #StatCode 
## Problem
> [!quote] Table I
> 
> *NUMBER OF SIGNIFICANT EARTHQUAKES RECORDED GLOBALLY FROM 2010 TO 2017. SOURCE: OURWORLDINDATA.ORG*

| year | # of recorded earthquakes |
| ---- | ------------------------- |
| 2010 | 62                        |
| 2011 | 59                        |
| 2012 | 48                        |
| 2013 | 52                        |
| 2014 | 55                        |
| 2015 | 47                        |
| 2016 | 47                        |
| 2017 | 53                        |
### 1) Obtain the sample mean and variance

MEAN : 52.875
VAR : 31.2678