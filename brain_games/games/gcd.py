import random
import prompt


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def brain_gcd():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')

    correct_answers = 0

    while correct_answers < 3:
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        correct_answer = gcd(a, b)

        print(f'Question: {a} {b}')
        user_answer = prompt.string('Your answer: ')

        if int(user_answer) == gcd(a, b):
            print('Correct!')
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')