from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    try:
        with open(SCORES_FILE_NAME, "r") as f:
            current_score = int(f.read().strip())
        new_score = points_of_winning + current_score
    except FileNotFoundError:
        new_score = points_of_winning

    with open(SCORES_FILE_NAME, "w") as f:
        f.write(str(new_score))


