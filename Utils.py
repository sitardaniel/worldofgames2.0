import os
import subprocess

SCORES_FILE_NAME = "Scores.txt"

BAD_RETURN_CODE = 8

def Screen_cleaner():
    cmd = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(cmd, shell=True, check=False)
