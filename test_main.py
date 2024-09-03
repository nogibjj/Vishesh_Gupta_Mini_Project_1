from main_python import number_product


def test_number_product():
    """testing the number_product function written in main.py"""
    assert number_product(3, 2) == 6
    assert number_product(2, 2) == 4
    assert number_product(5, 1) == 5


if __name__ == "__main__":
    test_number_product()
