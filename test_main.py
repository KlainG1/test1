
from main import hello


def test_hello(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Привет, мир!\n"
