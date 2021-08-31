import unittest
import main


class MyTestCase(unittest.TestCase):
    """
    This is using the integration of unittest classes, but that
    does not support easy capturing of outputs like pytest.
    """
    def test_nothing(self):
        self.assertEqual(True, True)  # add assertion here


def test_something(capsys):
    main.print_hi('mate')
    captured = capsys.readouterr()
    assert captured.out == "Hi, mate\n"

def test_something_else(capsys):
    main.print_hi()
    captured = capsys.readouterr()
    assert captured.out == "Hi, World\n"

def test_something_different(capsys):
    main.print_hi(5)
    captured = capsys.readouterr()
    assert captured.out == "Hi, 5\n"


if __name__ == '__main__':
    unittest.main()
