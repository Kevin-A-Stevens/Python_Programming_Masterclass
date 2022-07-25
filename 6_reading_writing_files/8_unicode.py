"""
Some computers cannot display unicode
characters properly

My linux typically does so the issue may not
be seen on a linux PC such as the mdash
"""
with open('jabberwocky.txt', encoding='utf-8') as jabber:
    for line in jabber:
        print(line.rstrip())

