

> [!NOTE] **Salt:**
> - Unique, random value added to each user's password before hashing.
> - Ensures that identical passwords have different hashes.
> - Stored alongside the hashed password in the database.



> [!NOTE] **Pepper:**
> - A secret value added to passwords before hashing.
> - Common for all passwords but kept secret from the database.
> - Typically stored securely, separate from the database (e.g., in environment variables). 



> [!NOTE] **Key Differences:**
> - **Salt** is unique per user and stored with the hash
> - **pepper** is common and kept secret.
> - **PURPOSE**
> 	- **Salt** defends against rainbow table attacks by ensuring unique hashes
> 	- **pepper** adds an extra layer of security by making it harder to reverse hashes even if the salt and hash are compromised.