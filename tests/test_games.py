import pytest
from MemoryGame import generate_sequence, is_list_equal
from GuessGame import generate_number
from CurrencyRouletteGame import get_money_interval


class TestMemoryGame:
    def test_generate_sequence_length(self):
        """Test that sequence length matches difficulty"""
        for difficulty in range(1, 6):
            sequence = generate_sequence(difficulty)
            assert len(sequence) == difficulty

    def test_generate_sequence_range(self):
        """Test that numbers are in valid range (1-101)"""
        sequence = generate_sequence(5)
        for num in sequence:
            assert 1 <= num <= 101

    def test_is_list_equal_same_lists(self):
        """Test that identical lists return True"""
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        assert is_list_equal(list1.copy(), list2.copy()) == True

    def test_is_list_equal_different_lists(self):
        """Test that different lists return False"""
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        assert is_list_equal(list1.copy(), list2.copy()) == False


class TestGuessGame:
    def test_generate_number_range(self):
        """Test that generated number is within difficulty range"""
        for difficulty in range(1, 6):
            for _ in range(10):  # Test multiple times due to randomness
                num = generate_number(difficulty)
                assert 1 <= num <= difficulty


class TestCurrencyRouletteGame:
    def test_get_money_interval(self):
        """Test money interval calculation"""
        # With difficulty 5, interval should be (rate-0, rate+0) = (rate, rate)
        interval = get_money_interval(5, 3.5)
        assert interval == (3.5, 3.5)

    def test_get_money_interval_difficulty_1(self):
        """Test money interval with difficulty 1"""
        # With difficulty 1, interval should be (rate-4, rate+4)
        interval = get_money_interval(1, 3.5)
        assert interval == (-0.5, 7.5)
