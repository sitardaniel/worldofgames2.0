import os
import pytest
from Score import add_score
from Utils import SCORES_FILE_NAME


@pytest.fixture
def clean_scores_file():
    """Remove scores file before and after each test"""
    if os.path.exists(SCORES_FILE_NAME):
        os.remove(SCORES_FILE_NAME)
    yield
    if os.path.exists(SCORES_FILE_NAME):
        os.remove(SCORES_FILE_NAME)


def test_add_score_creates_file_if_not_exists(clean_scores_file):
    """Test that add_score creates the file if it doesn't exist"""
    add_score(1)
    assert os.path.exists(SCORES_FILE_NAME)


def test_add_score_calculates_correctly(clean_scores_file):
    """Test that score is calculated as (difficulty * 3) + 5"""
    add_score(1)  # Should be (1 * 3) + 5 = 8
    with open(SCORES_FILE_NAME, "r") as f:
        score = int(f.read().strip())
    assert score == 8


def test_add_score_accumulates(clean_scores_file):
    """Test that scores accumulate over multiple games"""
    add_score(1)  # 8
    add_score(2)  # 8 + 11 = 19
    with open(SCORES_FILE_NAME, "r") as f:
        score = int(f.read().strip())
    assert score == 19


def test_add_score_difficulty_levels(clean_scores_file):
    """Test scoring for different difficulty levels"""
    # Difficulty 1: (1 * 3) + 5 = 8
    # Difficulty 5: (5 * 3) + 5 = 20
    add_score(5)
    with open(SCORES_FILE_NAME, "r") as f:
        score = int(f.read().strip())
    assert score == 20
