import random

def get_tof_statements():
    statements = []
    statements.append(["Tigers have stripes", "T"])
    statements.append(["The capital of France is Madrid", "F"])
    statements.append(["The Queen owns one sixth of the land on the Earth", "T"])
    
    return statements

def get_general_statements():
    statements = []
    statements.append(["What is the capital of Spain?", "MADRID"])
    statements.append(["What comes after A?", "B"])
    statements.append(["Who was the first U.S. President?", "GEORGE WASHINGTON"])

    return statements

def play_tof_quiz():
    tof_statements = get_tof_statements()
    random.shuffle(tof_statements)
    score = 0
    for s in tof_statements:
        print("True or false: " + s[0])
        guess = input("Enter T or F: ").upper()
        if guess == s[1]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect :(")
    print("Your final score is " + str(score))

def play_general_quiz():
    general_statements = get_general_statements()
    random.shuffle(general_statements)
    score = 0
    for s in general_statements:
        print(s[0])
        guess = input("Enter your answer: ").upper()
        if guess == s[1]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect :(")
    print("Your final score is " + str(score))

def main_menu():
    print("+------------------------------------+")
    print("|  Welcome to the Quiz!              |")
    print("+------------------------------------+")
    print("| Please select an option:           |")
    print("|                                    |")
    print("| 1. Play True or False quiz         |")
    print("| 2. Play General Knowledge quiz     |")
    print("| 0. Quit                            |")
    print("+------------------------------------+")
    choice = input("Enter 1, 2, or 0: ")
    if choice == "1":
        play_tof_quiz()
    elif choice == "2":
        play_general_quiz()
    elif choice == "0":
        print("Thanks for playing!")
        quit()

while True:
    main_menu()