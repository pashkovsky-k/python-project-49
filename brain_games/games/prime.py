import random
import prompt
from brain_games.cli import welcome_user


def is_prime(number):
    if number <= 1:
        return 'no'
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def brain_prime():

    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers = 0

    while correct_answers < 3:
        number = random.randint(1, 1000)
        correct_answer = is_prime(number)

        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
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
