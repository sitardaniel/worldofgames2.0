from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    try:
        f = open(SCORES_FILE_NAME, "r")
        f = f.read()
        currentScore = POINTS_OF_WINNING + int(f)
        f = open(SCORES_FILE_NAME, "w")
        f.write(str(currentScore))
        f.close()
    except FileNotFoundError as e:
        g = open("Scores.txt", "w")
        g.write(str(POINTS_OF_WINNING))
        g.close()


