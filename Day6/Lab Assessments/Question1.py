import re

# 1. re.match() – Check if string starts with EMP + 3 digits

emp_text = "EMP123 joined the company"

emp_pattern = r'^(EMP\d{3})'
emp_match = re.match(emp_pattern, emp_text)

if emp_match:
    print("Employee ID Match Found:")
    print("Full Match:", emp_match.group(0))   # Captured group
else:
    print("No valid Employee ID found")


# 2. re.search() – Find first valid email in text

email_text = "For queries contact hr.team@wipro.com or support@example.org"

email_pattern = r'([\w.+-]+@[\w-]+\.[\w.]+)'
email_match = re.search(email_pattern, email_text)

if email_match:
    print("\nEmail Match Found:")
    print("Full Match:", email_match.group(0))
    print("Username Part:", email_match.group(1).split('@')[0])
else:
    print("No email found")


# 3 & 4. Meta-characters + Special sequences + Capturing groups

sample_text = "User EMP456 logged in at 10 AM"

pattern = r'(EMP\d{3})\s+(\w+)\s+in\s+at\s+(\d+\s\w+)'
match = re.search(pattern, sample_text)

if match:
    print("\nDetailed Pattern Match:")
    print("Full Match:", match.group(0))
    print("Employee ID:", match.group(1))   # \d and capturing ()
    print("Action:", match.group(2))        # \w+
    print("Time:", match.group(3))          # \d+ \s \w+
