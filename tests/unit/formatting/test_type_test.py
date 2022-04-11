from formatting import type_test

def test_is_intlike_basic_ints():
    assert type_test.is_intlike(1)
    assert type_test.is_intlike("1")
    assert type_test.is_intlike(1.1)
    assert type_test.is_intlike(True)
    
def test_is_intlike_negative_ints():
    assert type_test.is_intlike(-1)
    assert type_test.is_intlike("-1")
    assert type_test.is_intlike(-1.1)
    
def test_is_intlike_not_ints():
    assert type_test.is_intlike("test") == False
    assert type_test.is_intlike("1.0") == False