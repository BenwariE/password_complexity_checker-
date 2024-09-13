import re

def password_complexity_checker(password):
    rating = 0
    criteria = {
        "length": len(password) >= 8,
        "uppercase": re.search(r"[A-Z]", password) is not None,
        "lowercase": re.search(r"[a-z]", password) is not None,
        "digit": re.search(r"[0-9]", password) is not None,
        "special": re.search(r"[!@#$%^&*()_+=\-`~[\]{}|;:'\",.<>?/]", password) is not None
    }

 
    if all(criteria.values()):
        print("Password is strong.")
        rating = 'good'
        return print(rating)
    else:
        print("Password is weak. Suggestions to improve:")
        if not criteria["length"]:
            print("- Password should be at least 8 characters long.")
            rating += -1
        if not criteria["uppercase"]:
            print("- Password should include at least one uppercase letter.")
            rating+= -1
        if not criteria["lowercase"]:
            print("- Password should include at least one lowercase letter.")
            rating+= -1
        if not criteria["digit"]:
            print("- Password should include at least one digit.")
            rating+= -1
        if not criteria["special"]:
            print("- Password should include at least one special character (e.g., !@#$%^&*).")
            rating+= -1
    return print(f'password rating is{rating}')
def input_password():
    if __name__ == "__main__":
        password = input("Enter a password to check its complexity: ")
        password_complexity_checker(password)
    else:
        pass
    return password_complexity_checker(password)  
input_password()
    
