# Cross-site Request Forgery (CSRF)
- Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they are currently authenticated.
- Avoided by correct authentication, so it is not enough to just send a request in a URL without further information from the server
![[Pasted image 20240608193641.png]]

## CSRF principles
- Browser requests automatically include any credentials associated with the site 
	- user's session cookie, IP address, credentials... 
- The attacker makes an authenticated user to submit a malicious, unintentional request 
	- This can happen from a different source (hostile website) 
- If the user is currently authenticated, the site will have no way to distinguish between a legitimate and a forged request sent by the victim 
	- The attacker does not see anything...

## CSRF explained with GET
- The victim visits `http://www.bank.com` and performs a successful [[Authentication]]
	- she receives the session token
- The victim opens another browser tab or window and visits a malicious web site
- The malicious web page contains something like:
	- `<img src=”http://www.bank.com/transfer.php?to=1337&amount=10000” />`
- that makes the browser to ask something like:
	- `GET http://www.bank.com/transfer.php?to=1337&amount=10000`
- The request contains the right cookie (session token)
- The bank websites satisfies the request...

## CSRF explained with POST
1. If the bank uses POST and the vulnerable request looks like this: 
	- `POST http://bank.com/transfer.do TTP/1.1acct=1337&amount=10000`
2. Such a request cannot be delivered using standard A or IMG tags but can be delivered using a FORM tag:
	- `<form action="http://bank.com/transfer.php"method="POST">`
	  `<input type="hidden" name="acct" value="1337" />`
	  `<input type="hidden" name="amount" value="10000" />`
	  `<input type="submut" value="Click me" />`
	  `</form>`
	  
3. This form will require the user to click on the submit button, but this can be also executed automatically using JavaScript:
	- `<body onload="document.forms[0].submit()">`
	  `<form...`

# CSRF countermeasures
- Use secret “**CSRF tokens**”
	- No Web request may take an action on behalf of someone unless it also presents that person’s token
	- Since attackers cannot easily discover the CSRF token, they generally aren't able to impersonate the intended victim
	- more [details](https://brightsec.com/blog/csrf-token/)
