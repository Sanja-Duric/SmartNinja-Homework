
import random
import json
import datetime


class Result():
    def __init__(self, name, attempts, date):
        self.name = name
        self.attempts = attempts
        self.date = date

secret = random.randint(1, 20)
attempts = 0
name = input("Unesi ime igrača: ")

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())

    for score_dict in score_list:
        print(str(score_dict["name"]) + " :" + str((score_dict["attempts"])) + " attempts, date: " + score_dict.get("date"))

while True:
    guess = int(input("Pogodi tajni broj: "))
    attempts += 1

    if guess == secret:

        result = Result(name=name, attempts=attempts, date=str(datetime.datetime.now()))

        score_list.append(result.__dict__)

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Bravo! Tajni broj je " + str(secret))
        print("Iskorišteno pogodaka: " + str(attempts))
        break
    elif guess < secret:
        print("Pokušaj s većim brojem!")
    elif guess > secret:
        print("Pokušaj s manjim brojem!")

print("Kraj igre.")
