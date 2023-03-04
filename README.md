# Password Generator

This is a simple Python script that generates a random password of the specified length. The password contains a mix of lowercase and uppercase letters, numbers, and special characters.

## Usage

To use this script, simply run it in your terminal and enter the desired length of the password when prompted:

```
$ python password_generator.py
Enter password length: 12
Your new password is: Gv8&$m4@pJ7w
```

You can also import this script into your own Python projects and use the password_generator function to generate passwords programmatically:

```
from password_generator import password_generator

password = password_generator(12)
print(password)
```
