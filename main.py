questions = ["What is the capital of India?", "What is 2 + 2?", "What color is the sky?"]
answers = ["New Delhi", "4", "Blue"]

def run_quiz():
    score = 0

    for i in range(len(questions)):

        print(questions[i])
        
        answer = input("Your answer: ")

        if answer == answers[i]:

            print("Correct!")

            score += 1

        else:


            print("Oops! The correct answer is", answers[i])



        print("You scored", score, "out of", len(questions))

run_quiz()
