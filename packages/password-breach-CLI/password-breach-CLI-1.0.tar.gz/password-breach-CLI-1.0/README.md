
# Password Breach Checker
This simple project checks if the user's password was breached in any data leaks using API from haveibeenpwned.com

There are 2 ways to use the application.
1) By installing the package from PyPi and running command "breach facebook123" from command line.
2) Simply clone the repository and install the required packages available in requirements.txt. 
   Then run python main " facebook123 "

Just replace any word you wish to check with  "facebook123"

Some details about the Application and it's working:
1) It is a command line application which accepts a password as a
parameter and checks how many times the password was present in a
data breach.
2) Takes the password and hashes it using sha1 password hash
3) Split the hashed password into two parts.
 query_character = 1st five characters
 tail = remaining .
4) call the api of pwnedpasswords.com and append the query character
5) The api compares the query_character against first 5 characters of all the hashed
 password in the database.
6) All the matching hashes tail along with their breach count is returned.
7) Now, we compare our tail against all the tails returned by the api.
8) If a match is found, we return the breached count and appropriate message.
9) If no, we return appropriate message.

