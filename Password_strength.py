print("--- Password Strength Evaluator ---")

password = input("Please enter your password: ")

# 1. Length Check
if len(password) < 8:
    print("⚠️ Warning: This password is very short!")

# 2. Complexity Analysis
special_characters = ".,//;:[]{}*+-!@#$%^\&()=~` "
numbers = lowercase = uppercase = symbols = 0

for char in password:
    if char.isdigit():
        numbers += 1
    elif char.islower():
        lowercase += 1
    elif char.isupper():
        uppercase += 1
    elif char in special_characters:
        symbols += 1
    else:
        print(f"Note: Character '{char}' is an unrecognized symbol.")

# 3. Strength Classification Logic
password_class = 5 # Default

if (lowercase + uppercase == 0) and symbols == 0:
    print("❌ Very Weak: Only numeric values.")
    password_class = 4
elif (lowercase + uppercase >= 1) and symbols == 0:
    if uppercase == 0:
        print("🟠 Weak: No uppercase or special characters.")
        password_class = 3
    else:
        print("🟡 Good: But could use special characters.")
        password_class = 2
elif (lowercase + uppercase >= 1) and symbols != 0:
    if uppercase != 0:
        print("✅ Very Strong!")
        password_class = 0
    else:
        print("🟢 Strong: Consider adding uppercase.")
        password_class = 1

# 4. Wordlist Check (Line by Line)
try:
    with open("test_file.txt", "r") as file:
        # Using a set for faster lookups and exact matching
        common_passwords = {line.strip() for line in file}
    
    if password in common_passwords:
        print("🚨 ALERT: This password is in a common wordlist/leak!")
except FileNotFoundError:
    print("Note: 'test_file.txt' not found, skipping wordlist check.")