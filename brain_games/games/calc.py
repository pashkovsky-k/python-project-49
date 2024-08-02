import random
import prompt


def brain_calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    correct_answers = 0

    while correct_answers < 3:
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        operators = ['+', '-', '*']
        operator = random.choice(operators)
        question = f'{a} {operator} {b}'
        correct_answer = eval(question)
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if int(user_answer) == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'"
                  )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
