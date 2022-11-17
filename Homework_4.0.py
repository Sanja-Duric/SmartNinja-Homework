#uz score upisujemo i datum igre

import random
import json
import datetime

current_time = datetime.datetime.now()
print(current_time)


secret = random.randint(1, 30)
attempts = 0





while True:
    guess = int(input("Pogodi tajni broj: "))
    attempts += 1
    score_data = {"attempts": attempts, "date": datetime.datetime.now()}

    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())

        for score_dict in score_list:
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})

        with open("score_list.json", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Bravo! Tajni broj je " + str(secret) + "!")
        print("Iskorišteno pokušaja: " + str(attempts))
        break
    elif guess < secret:
        print("Pokušaj s većim brojem!")
    elif guess > secret:
        print("Pokušaj s manjim brojem!")

