
> [!NOTE] Why?
> It is not practical to protect against every possible attack. An approach is to make use of a set of guiding principles when designing and building software
1. Secure the weakest link 
2. Practice defense in depth 
3. Fail securely 
4. Follow the principle of least privilege
5. Compartmentalize 
6. Keep it simple 
7. Promote privacy
8. Remember that hiding secrets is hard 
9. Be reluctant to trust
10. Use your community resources

# in-depth
## Secure the weakest link 
- A software security system is only as secure as its weakest component. 
- Sometimes is the infrastructure the weakest link, not the software 
- Identify the weakest link (using risk analysis)

## Practice defense in depth
- Manage risk with diverse defensive strategies 
- The main idea: defenses takes a whole can be stronger than the weakest link 
- May seem contradictory with “secure the weakest link”. However, “secure the weakest link” applies when components have functionality that does not overlap 
- Consider what happens when your input validation is insufficient? When you crypto is broken?...

## Fail securely 
- Handle failure scenarios in a secure way 
- ... when the password file is not found
- ... when the database does not respond 
- ... when a protocol state is inconsistent

## Follow the principle of least privilege 
- Perform all operations with a minimum of privileges 
- Isolate og limit operations that require extended privileges 
- “Drop” unnecessary privileges as soon as possible

## Compartmentalize 
- Split application into smaller modules 
- Functionality 
- Security level/privileges 
- Threat level 
- Separate (physically if possible) sensitive data from “normal” data: (Example: TPM, TrustZone in Rasberry Pi)

## Keep it simple 
- Software design and implementation should be as straightforward as possible 
- Complex design is more likely to include subtle problems that will be missed during analysis • Typically: 2–3 bugs pr. 1000 lines of code

## Promote privacy 
- “Privacy” : Try not to do anything that may compromise the privacy of the user 
- There is very often a trade off between privacy and usability (e.g., systems forgetting credit card numbers) 
- What is logged (usernames, passwords, ...)? 
- What happens to sensitive data after use? 
- Secure deletion?

## Remember that hiding secrets is hard 
- Keys must be kept secret to avoid eavesdropping and tampering. Top-secret algorithms need to be protected from competitors. 
- Passwords/backdoors hardcoded in source code

## Be reluctant to trust 
- Input validation of everything: user input, files (including file names),
-  network, environment, ... 
- Accept-list vs. reject-list 
- Use a parser that is powerful enough: reg.exp. vs. contect-free languages

## Use your community resources 
- Don’t roll your own crypto!