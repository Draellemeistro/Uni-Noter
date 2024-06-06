
# Example 1
## Code
```python

```
## Problem
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
# Example 2
## Code
```python

```
## Problem
On average **Peter receives 125 emails per day**. Out of these 125 emails, **25 emails are spam**. A special software is used that allows to automatically filter the spam emails and put them in a special Spam folder. Specification of this software states that the detection rate of spam is **98%** and the **probability of a false positive is 7%**. Peter never checks the messages in Spam folder. What are the c**hances that he overlooks an important message** ( in other words, what is the probability that **an email that is classified as a spam and put in Spam folder is in fact not a spam**)?
**Note that a false positive in this case is a situation when a non-spam email is marked as spam. A false positive refers to a situation when a spam email is not marked as spam.**

**EVENTS**
S: received mail is spam
$S_{flat}$ mail is not spam
D: mail is put in spam folder
$D_{flat}$ mail is not put in spam folder

$P(S)=\frac{25}{125}=0.2$ mail is spam

$P(S_{flat})=1-0.2=0.8$ mail is not spam

$P(D_{flat}|S)=1-0.98=0.02$ mail is spam and is not put in spam folder
$P(D|S)=0.98$  The mail is spam, and is put in spam-folder

$P(D|S_{flat})=0.07$ mail is not spam, and is put in spam-folder

$P(D_{flat}|S_{flat})=1-0.07=0.93$ mail is not spam and is not put in spam folder

**If it was thrown in spam, what is the prob. that it is not a spam mail?** 
this is: $P(S_{flat}|D)$

The prob that a mail is in spam depends on the probability of whether or not it is spam, together with whether or not it is put into the spam folder, so: $P(D)$ 
$=P(D|S)*P(S)+ P(D|S_{flat})*P(S_{flat})$
$=0.98*0.2+0.07*0.8=0.252$

$P(S_{flat}|D)$ Can now be found through \____ 

$$P(S_{flat}|D)=\frac{P(D | S_{flat})*P(S_{flat})}{P(D)}$$
$$=\frac{P(D | S_{flat})*P(S_{flat})}{P(D|S)*P(S)+P(D|S_{flat}*P(S_{flat}))}$$
$$=\frac{0.07*0.8}{0.98*0.2+0.07*0.8}=\frac{0.07*0.8}{P(D)}=\frac{0.07*0.8}{0.252}$$
$$=0.22$$

