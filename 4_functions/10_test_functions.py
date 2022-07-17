"""
writing a function to test programs
use caps for constants

testing is the process of finding out if there
are any bugs in your code

debugging is the process of finding out what
the bugs are and fixing them

"""
LOW = 1
HIGH = 1000

# print("Please think of a number between 1 and 1000")
# input("Press ENTER to start")


def guess_binary(answer: int, low: int, high: int) -> int:
    """
    Tests the Hi-Lo game using the range function to use
        numbers between 1 and 1000
    :param answer: The correct answer
    :param low: The start of the range to test
    :param high: The end of the range to test
    :return: Returns number of guesses
    """
    guesses = 1
    while True:
        # print("\tGuessing in the range {} to {}".format(low, high))
        guess = low + (high - low) // 2
        # high_low = input("My guess is {}. Should I guess higher or lower? Enter h or l, or c if my guess was correct."
        #                  .format(guess)).casefold()

        # if high_low == "h":
        if guess < answer:
            # I have to guess higher.  The low end of the range becomes 1 greater than the guess.
            low = guess + 1
        # elif high_low == "l":
        elif guess > answer:
            # I have to guess lower.  The high end of the range becomes 1 less than the guess.
            high = guess - 1
        # elif high_low == "c":
        elif guess == answer:
            # print("I got it in {} guesses!".format(guesses))
            # break
            return guesses
        # else:
        #     print("Please enter h, l or c")

        guesses += 1


correct_count = 0
max_guesses = 0
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1

print("I guessed without being told {} times. Max {} guesses"
      .format(correct_count, max_guesses))


