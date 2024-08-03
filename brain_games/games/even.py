import random
import prompt
from brain_games.cli import welcome_user


def brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0

    while correct_answers < 3:
        random_number = random.randint(1, 9999)
        is_even_random_number = random_number % 2 == 0

        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')

        is_correct_yes = user_answer == "yes" and is_even_random_number
        is_correct_no = user_answer == "no" and not is_even_random_number

        if is_correct_yes or is_correct_no:
            print('Correct!')
            correct_answers += 1
        else:
            correct_answer = 'yes' if is_even_random_number else 'no'
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
