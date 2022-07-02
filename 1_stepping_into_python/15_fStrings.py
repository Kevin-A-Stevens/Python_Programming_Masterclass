"""
f strings
No plans to back port them to earlier Python versions
They will not work with Python 3.4 or earlier
String formatting also works with f strings
"""

age_in_words = "34 years"
name = "Kevin"

# Using an f string
print(name + f" is {age_in_words} years old")
print(f"Pi is approximately {22/7:12.50f}")

pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
