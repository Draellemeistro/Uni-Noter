
# Basics of buffer overflow vulnerability
- **Buffer** is a contiguous memory associated with a variable. 
- **Overflow of a buffer**: process tries to put/get more data in/from the buffer than it can hold. 
	- What can possibly go wrong? 
- The C standard states that such process is undefined 
- Compiler and OS protections can be applied to detect and prevent out-of-bound accesses 
	- but many compilers ignore these checks and assume the program is safe/just raise a warning

### Program Memory Layout (32 bit system)
![[Pasted image 20240608200009.png]]
### Stack
![[Pasted image 20240608200036.png]]
### Oops!
- When strcpy will work…
```
void func(char *arg1) { 
	char buffer[4]; 
	strcpy(buffer, arg1);
	 … 
} 

int main() { 
	char *mystr = “AuthMe!”; 
	func(mystr); 
	… 
}
```
![[Pasted image 20240608202430.png]]

## Example: [[HeartBleed]] Vulnerability