##### This lecture is the continuation of Lecture 5. We will talk about principles of secure applications, cookies and web security. For the exercises will mainly use Haaukins.
- Cross-site scripting: [https://owasp.org/www-community/attacks/xss/](https://owasp.org/www-community/attacks/xss/)
- More Cross-site scripting: [https://www.cyber.aau.dk/education/Cybersecurity+Advanced/Cross-site+scripting/](https://www.cyber.aau.dk/education/Cybersecurity+Advanced/Cross-site+scripting/)
- Cross-site request forgery: [https://owasp.org/www-community/attacks/csrf](https://owasp.org/www-community/attacks/csrf)
- More Cross-site request forgery: [https://www.cyber.aau.dk/education/Cybersecurity+Advanced/Cross-site+request+forgery/](https://www.cyber.aau.dk/education/Cybersecurity+Advanced/Cross-site+request+forgery/)
# Summary
asd

## Begreber 
- [[Web security]]
	- Web attacks: [[XSS]] and [[CSRF]]
	- [[Buffer overflow Attack]] (**==example== Heartbleed**)
- [[Regular expressions (Regex)]]
- [[Principles of Software Security]]

# Some additional assignments
- ftp server, ftplogin.com
	- Hint: “*Find a way to log in as admin and get the flag from an FTP server at ftplogin.com. (Go john!)*”
	- ==Hydra -l admin -P /usr/share/john/password.lst -vV ftplogin.com ftp==
	- [[Hydra]]
- SSHtay Hydrated
- Exposed Logging Login Blogging
**Hint:**
1. Password 4 letters
2. Subset of I, V, X, C, M, L, D