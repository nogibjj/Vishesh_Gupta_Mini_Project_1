from main_python import multiply


def test_add():
    """testing out multiply function"""
    assert multiply(3, 10) == 30
    assert multiply(2, 0) == 0
    assert multiply(5, 6) == 30


if __name__ == "__main__":
    test_add()
