
import random
import json
import datetime


class Result():
    def __init__(self, name, score, date):
        self.name = name
        self.score = score
        self.date = date

secret = random.randint(1, 20)
score = 0
name = input("Unesi ime igrača: ")

while True:
    guess = int(input("Pogodi tajni broj: "))
    score += 1

    if guess == secret:

        result = Result(name=name, score=score, date=str(datetime.datetime.now()))

        with open("result.json", "w") as result_file:
            result_file.write(str(result.__dict__))

        print("Bravo! Tajni broj je " + str(secret))
        print("Iskorišteno pogodaka: " + str(score))
        break
    elif guess < secret:
        print("Pokušaj s većim brojem!")
    elif guess > secret:
        print("Pokušaj s manjim brojem!")

print("Kraj igre.")
