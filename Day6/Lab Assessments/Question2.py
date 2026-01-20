# QUESTION 1: Strong Password Validation


import re
password = "StrongPass1!"

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'

if re.match(pattern, password):
    print("Valid Strong Password")
else:
    print("Invalid Password")

# QUESTION 2: Lookahead Assertions (?=...)



pattern_lookahead = r'^(?=.*\d)(?=.*[A-Z]).{8,}$'
test_password = "TestPass1"

if re.match(pattern_lookahead, test_password):
    print("Password satisfies lookahead conditions")
else:
    print("Password does not satisfy lookahead conditions")

# QUESTION 3: Regular Expression Modifiers



# IGNORECASE
print("\nIGNORECASE Example:")
print(re.search("hello", "HELLO"))                   
print(re.search("hello", "HELLO", re.IGNORECASE))    

# MULTILINE
print("\nMULTILINE Example:")
text = "First\nSecond\nThird"
print(re.search("^Second", text))                    
print(re.search("^Second", text, re.MULTILINE))      

# DOTALL
print("\nDOTALL Example:")
text = "Start\nEnd"
print(re.search("Start.*End", text))                 
print(re.search("Start.*End", text, re.DOTALL))      

# QUESTION 4: Effect of Modifiers on Pattern Matching



text = "Hello\nWorld"
pattern = r'Hello.World'

print("Without DOTALL:", re.search(pattern, text))
print("With DOTALL:", re.search(pattern, text, re.DOTALL))
