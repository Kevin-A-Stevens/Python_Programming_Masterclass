"""
Program to copy and paste emails and phone numbers
pyperclip must be installed with pip3
"""
import re, pyperclip

# Create a regex for phone numbers
phone_regex = re.compile(r'''
# 415-555-000, 555-0000, (415) 555-0000 ext 12345, ext. 12345 x12345

(
((/d/d/d) | (\(/d/d/d\)))? # area code optional
(\s|-)                     # first seperator
\d\d\d                     # first three digits
-                          # separator
\d\d\d\d                   # last 4 digits
((ext(\.)?\s |x)           # extension words optional
(\d{2,5}))?                # extension number optional
)
''', re.VERBOSE)

# Create a regex for email addresses
email_regex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com
[a-zA-Z0-9_.+]+             # name part
@                           # @ symbol
[a-zA-Z0-9_.+]+             # domain part

''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

all_phone_numbers = []
for phone_number in extracted_phone:
    all_phone_numbers.append(phone_number[0])

print(all_phone_numbers)

# Copy the extracted text to the clipboard
results = '\n'.join(all_phone_numbers) + '\n' + '\n'.join(extracted_email)
pyperclip.copy(results)

