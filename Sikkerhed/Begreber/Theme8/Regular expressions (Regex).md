



# Quiz regular expressions

![[Pasted image 20240608211023.png]]
![[Pasted image 20240608211034.png]]
![[Pasted image 20240608211049.png]]

## Explanation
- **\\w+**: Matches one or more word characters (letters, numbers, and underscore) - captures the username. 
- **@**: Matches the "@" symbol. 
- **\\w+**: Matches one or more word characters - captures the domain name. 
- **\\.**: Matches a literal dot (separates domain name from extension). 
- **\\w{2,}**: Matches two or more word characters - captures the domain extension (minimum 2 letters).
## Python Code
```python
import re 

regex = r"\w+@\w+\.\w{2,}" 

# Sample emails
emails = ["user@example.com", "user123!@#$.com", "username@domain", "this.is.not.an.email"] 

for email in emails: 
	if re.match(regex, email): 
		print(f"{email} - Valid Email") 
	else: 
		print(f"{email} - Not a Valid Email")
```
# wat
1. **Literal Characters**
	- Pattern: hello - Usage: Matches the exact sequence of characters. - Use Case: Find the word "hello" in a text. 
2. **Wildcard Character** 
	- Pattern: **.**
	- Usage: Matches any single character except newline characters. 
	- Use Case: Match "a_e" to find "ace", "ape", etc. 
3. **Digit** 
	- Pattern: \\d 
	- Usage: Matches any digit (0-9). 
	- Use Case: Validate that a string contains a numerical value.
4. **Non-Digit** 
	- Pattern: \\D
	- Usage: Matches any character that's not a digit.
	- Use Case: Find non-numeric characters in a string of numbers. 
5. **Word Character** 
	- Pattern: \\w 
	- Usage: Matches any alphanumeric character (letters, digits, and underscore). 
	- Use Case: Validate usernames that can contain letters, numbers, and underscores. 
6. **Non-Word Character** 
	- Pattern: \\W 
	- Usage: Matches any character that's not a word character. 
	- Use Case: Find characters in a text that are not part of words, such as punctuation.
7. **Whitespace** 
	- Pattern: \\s 
	- Usage: Matches any whitespace character (space, tab, newline). 
	- Use Case: Find and replace extra spaces between words. 
8. **Non-Whitespace** 
	- Pattern: \\S 
	- Usage: Matches any character that's not a whitespace character. 
	- Use Case: Extract non-space characters from a string. 
9. **Beginning of String** 
	- Pattern: ^ 
	- Usage: Matches the beginning of a string. 
	- Use Case: Ensure a string starts with a specific word or character.
10. **End of String** 
	- Pattern: $ 
	- Usage: Matches the end of a string. 
	- Use Case: Ensure a string ends with a specific word or character. 
11. **Character Class** 
	- Pattern: \[abc] 
	- Usage: Matches any one of the characters enclosed in the square brackets. 
	- Use Case: Match "a", "b", or "c" in a string. 
12. **Negated Character Class** 
	- Pattern: [^abc] 
	- Usage: Matches any character that is not in the square brackets. 
	- Use Case: Find any character that is not "a", "b", or "c".
13. **Quantifiers: 0 or More** 
	- Pattern: * 
	- Usage: Matches 0 or more occurrences of the preceding element. 
	- Use Case: Match "lo*" to find "l", "lo", "loo", etc.
14. **Quantifiers: 1 or More** 
	- Pattern: +
	- Usage: Matches 1 or more occurrences of the preceding element. 
	- Use Case: Match "lo+" to find "lo", "loo", "looo", etc.
15. **Quantifiers: 0 or 1** 
	- Pattern: ? 
	- Usage: Matches 0 or 1 occurrences of the preceding element. 
	- Use Case: Match "colou?r" to find both "color" and "colour".
16. **Exact Number of Times** 
	- Pattern: {n} 
	- Usage: Matches exactly n occurrences of the preceding element. 
	- Use Case: Match "\d{4}" to find exactly four digits in a row. 
17. **17. Range of Times** 
	- Pattern: {n,m} 
	- Usage: Matches between n and m occurrences of the preceding element. 
	- Use Case: Match "\d{2,4}" to find numbers that are at least two digits long but no more than four digits long. 
18. **Grouping** 
	- Pattern: (abc) 
	- Usage: Matches the exact sequence of characters in the parentheses. 
	- Use Case: Find repetitions or use in string replacement.
19. **Or Operator** 
	- Pattern: a|b 
	- Usage: Matches either a or b. 
	- Use Case: Find occurrences of either "a" or "b" in a text.
