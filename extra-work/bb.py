def greet():
    print("Hello, welcome to the backend world!")

def greet_user(name):
    print(f"Hello, {name}!")

def add(a, b): #Fuction with return value
    return a + b
 
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Invalid credentials"

print(login("admin", "1234"))  # Example usage of the login function
print(login("user", "pass"))  # Example usage of the login function with invalid credentials