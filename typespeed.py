import random
import wikipediaapi
from sys import exit
from time import time

quick_test_lines = [
    "Hallownest prospered until the Radiance began appearing in the dreams of its people.",
    "The Pale King chose a Vessel known as the Hollow Knight to trap the Radiance.",
    "No mind to think. No will to break. No voice to cry suffering. Born of God and Void.",
    "You shall seal the blinding light that plagues their dreams. You are the Vessel.",
    "In attempting the feat, one proves their courage. May your Shade at last find rest."
]

def main():
    print(
        "\n--------- WELCOME TO TYPING SPEED TEST ⌨ ---------\n",
        "Which type of test do you want?",
        "1. Quick Test (Single line - Random text)",
        "2. Custom Test (Custom topic and lines)",
        sep = "\n"
    )

    speed , mistakes , accuracy = execute_test(input("Enter respective code(1 or 2): "))

    speed_word = round(speed*60/4.7)   #according to the internet, on an average one word is 4.7 characters

    print(f"\nYou typed with a speed of {round(speed)} chars/sec or {speed_word} words/min with {mistakes} words typed incorrect ({accuracy}% accuracy)")
    print(f"{speed_comment(speed_word)}\n")

def execute_test(decision):
    try:
        decision = int(decision)
    except ValueError:
        exit("Invalid type of decision 🥲")

    if decision == 1:
        test_qn =  random.choice(quick_test_lines)
    elif decision == 2:
        test_qn = custom_test()
    else:
        exit("Thought you got me? That's the wrong number 😏")

    print(f"\n{test_qn}\n")

    start = input("Press Enter to start typing (Your timer will start as soon as you press Enter): ")
    if start != "":
        exit("I told you to just press enter 🙄")

    start_time = time()
    test_ans = input()
    end_time = time()

    speed = type_speed(test_ans , (end_time - start_time))
    mistakes = type_mistakes(test_qn , test_ans)
    accuracy = type_accuracy(test_qn , mistakes)
    return speed , mistakes , accuracy

def type_mistakes(question , answer):
    mistakes = 0
    question_words = question.split(" ")
    answer_words = answer.split(" ")
    for i in range(len(question_words)):
        try:
            if question_words[i] != answer_words[i]:
                mistakes += 1
        except:     #if some error like IndexError occurs
            mistakes += 1
    return mistakes

def type_accuracy(question , mistakes):
    total_words = len(question.split(" "))
    accuracy = ((total_words-mistakes)/total_words)*100
    return round(accuracy , 1)

def type_speed(answer , time_taken):
    time_taken = round(time_taken, 2)
    char_speed = len(answer)/time_taken
    return char_speed

def speed_comment(speed):
    if speed <= 40:
        return ("Looks like you've just started. Keep practicing 😉")
    elif speed>40 and speed<=50:
        return ("You are a Good typer 😁")
    elif speed>50 and speed<=80:
        return ("You are a Pro typer 🤩")
    elif speed>80 and speed<=120:
        return ("You are a Mega typer 🤯")
    elif speed>120:
        return ("You are in the top league now. Keep pushing your limits 🔥")

def custom_test():
    print("\nApologies if any non-keyboard character is given in the searched topic. Hope you understand 🥹")
    topic = input("Enter the topic you want to type: ").strip().title()
    try:
        num_lines = int(input("Enter the number of lines to type (preferably less than 10): "))
    except ValueError:
        exit("You were meant to give a number 🙄")

    if num_lines>15:
        exit("Do you really think you need to type that much? 🧐")
    lines_list = get_wikipedia_lines(topic , num_lines)
    lines = ""
    for line in lines_list:
        lines += f"{line}."

    return lines

def get_wikipedia_lines(page_title, num_lines=5):
    wiki_wiki = wikipediaapi.Wikipedia('CoolBot/0.0')
    page_py = wiki_wiki.page(page_title)

    lines = []

    if page_py.exists():
        for section in page_py.sections:
            lines.extend(section.text.split('.'))
    else:
        exit("Sorry, Couldn't find the topic ☹️")

    return lines[:num_lines]

if __name__ == "__main__":
    main()
