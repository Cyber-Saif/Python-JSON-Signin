# Account Login System
### A simple user authentication system written in Python that facilitates account creation and login functionality. It uses a JSON file to store usernames and passwords in plain text. Key features include:

#### Account Creation:
- Prompts users to create a secure password by enforcing criteria (length, capital letters, digits, special characters).
- Allows users to generate strong passwords automatically.
#### Login Validation:
- Verifies credentials from the JSON file to authenticate users.
#### Password Management:
- Provides a password strength checker and feedback.
- Includes a customizable password generator.

#### Important Note: The system does not encrypt stored passwords, so it is intended for educational purposes and should not be used in production or for sensitive applications. For improved security, consider implementing password hashing (e.g., using bcrypt) and encrypting the JSON file.
