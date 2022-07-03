"""
Guessing game

functions used
print()
int() = converts input to an integer
input()

Note the else picks up everything else and must come last
"""
answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher")
elif guess > answer:
    print("Please guess lower")
else:
    print("You got it first time")


