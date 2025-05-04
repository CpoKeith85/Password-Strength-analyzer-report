import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None
    
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )
    
    errors = {
        'length': length_error,
        'digit': digit_error,
        'uppercase': uppercase_error,
        'lowercase': lowercase_error,
        'symbol': symbol_error,
    }
    
    return password_ok, errors

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to check: ")
    is_strong, issues = check_password_strength(password)
    
    if is_strong:
        print("✅ Password is strong!")
    else:
        print("❌ Password is weak. Issues:")
        for issue, failed in issues.items():
            if failed:
                print(f" - {issue} requirement not met")
