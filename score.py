def get_score_list():
    import json


    with open("score_list.json","r") as score_file:
        score_list = json.loads(score_file.read())

    for score_dict in score_list:
        print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
