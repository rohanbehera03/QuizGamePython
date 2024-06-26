import math 
from quiz_database import question_bank
from quiz_database import options

number_of_questions = 0
current_score = 0

print("***********************")
print("Welcome to my quiz game!!!")

def check_answer(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False

for question_num in range(len(question_bank)):
    print("************************")
    print(question_bank[question_num]["text"])
    number_of_questions += 1
    for i in options[question_num]:
        print(i)
    guess = input("Enter your answer (A/B/C/D): ").upper()
    is_correct = check_answer(guess, question_bank[question_num]["answer"])
    correct_answer = question_bank[question_num]["answer"]
    if is_correct:
        current_score += 1
        print("Correct answer")
        print(f"You current score is {current_score}/{number_of_questions}")
    else:
        print("Incorrect answer")
        print(f"The correct answer is {correct_answer}")
        print(f"You current score is {current_score}/{number_of_questions}")

final_score = (current_score/number_of_questions)*100
print(f"You have given {current_score} correct answers.")
print(f"Your score is {final_score} %")
