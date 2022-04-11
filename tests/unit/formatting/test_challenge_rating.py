from formatting import challenge_rating

def test_format_challenge_rating_greater_than_0():
    assert challenge_rating.format_challenge_rating(1) == "1"
    assert challenge_rating.format_challenge_rating(5) == "5"
    assert challenge_rating.format_challenge_rating(20) == "20"

def test_format_challenge_rating_below_1():
    assert challenge_rating.format_challenge_rating(0) == "1\u20442"
    assert challenge_rating.format_challenge_rating(-1) == "1\u20444"
    assert challenge_rating.format_challenge_rating(-2) == "1\u20448"
    assert challenge_rating.format_challenge_rating(-3) == "0"