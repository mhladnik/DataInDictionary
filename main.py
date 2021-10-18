import random
import json
import datetime

secret = random.randint(1, 30)
attempts = 0
wrong_guesses = list()

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

#sort lists in  dictionary by number of attempts
print((sorted(score_list, key=lambda person: person['attempts']))[:3])

name = input("What is your name? ")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"name": name, "attempts": attempts, "date": str(datetime.datetime.now()), "wrong_guesses": wrong_guesses})
        for score_dict in score_list:
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print(f"You've guessed it - congratulations {name}! It's number {secret}.")
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
        wrong_guesses.append(guess)
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
        wrong_guesses.append(guess)
