import json

points = 0

def show_questions(question):
    global points
    print()
    print(question["pytanie"])
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    print()

    answer = input("Jaka jest twoja odpowiedź: (a,b,c,d) ")

    if answer == question["prawidłowa_odpowiedź"]:
       print("Zgadza się !")
       print()
       points += 1
    else:
        print('Niestety, zła odpowiedź')
        print()




with open("quiz.json", "r", encoding="utf-8") as json_file:
    questions = json.load(json_file)


for i in range(0, len(questions)):
    show_questions(questions[i])
    
print(f"Zdobyłeś {points} punktów !")