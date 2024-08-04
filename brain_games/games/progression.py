import random
import prompt
from brain_games.cli import welcome_user


def brain_progression():

    def arithmetic_progression(start, difference, terms):
        progression = []
        count = 0
        while count < terms:
            progression.append(start + difference * count)
            count += 1
        return progression

    name = welcome_user()
    print('What number is missing in the progression?')

    correct_answers = 0

    while correct_answers < 3:
        start = random.randint(1, 99)
        difference = random.randint(2, 20)
        terms = random.randint(5, 10)
        task_of_progression = arithmetic_progression(start, difference, terms)
        progression_len = len(task_of_progression)
        random_index = random.randint(1, progression_len) - 1
        task_of_progression_copy = task_of_progression
        correct_answer = task_of_progression_copy[random_index]
        task_of_progression_copy[random_index] = '..'
        question = ' '.join(map(str, task_of_progression_copy))
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if int(user_answer) == correct_answer:
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
