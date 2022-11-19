
import random
import json
import datetime

secret = random.randint(1, 30)
attempts = 0
name = 0
score_data = {"name": name, "attempts": attempts, "secret_num": secret, "date": datetime.datetime.now()}


with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())
for score_dict in score_list:
    print(str(score_dict["name"]) + ": " + str(score_dict["attempts"]) + " attempts, secret number: " + str(score_dict["secret_num"]) + " date: " + score_dict.get("date"))
name = input("Unesi ime igrača: ")

while True:
    guess = int(input("Pogodi tajni broj: "))
    attempts += 1


    if guess == secret:
        score_list.append({"name": name, "attempts": attempts, "secret_num": secret, "date": str(datetime.datetime.now())})

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