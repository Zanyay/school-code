#0: question
#1-4: possible answers
#5: category
#6: difficulty

import random

def print_question(q,p):
    print() #to have a new empty line
    print(q[0],"(difficulty:",q[6]+"/3)")
    for i in range(0,4):
        print(i+1, q[p[i]])

def raw_read_answer():
    try:
        ans = int(input("Please choose an answer (1,2,3 or 4):"))
        return ans
    except:
        print("Enter a number you dumb bitch")

def read_answer():
    ans = raw_read_answer()
    while ans not in [1,2,3,4]:
        ans = raw_read_answer()
    return ans

lines = open("quiz.csv").read().split("\n")

questions =[]
for line in lines:
    questions.append(line.split("\t"))

again = 'yes'
while again in 'yesYES':
    lives = 3
    score = 0
    while lives >0:
        p = [1,2,3,4]
        random.shuffle(p)
        question_index = random.randrange(0,len(lines))
        question_part = questions[question_index]
        print_question(question_part,p)

        answer = read_answer()
        if answer == p.index(1)+1:
            print("Congradulations!")
            score += int(question_part[6])
            print("score:",score)
        else:
            print("L + Ratio + be smarter. The correct answer is:",question_part[1])
            lives -= 1
            print('Lives left:',lives)
    print("final score:",score)
    again = input("would you like to play again? ")
print("Fuck You!")

