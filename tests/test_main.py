from src.main import welcome_message
from src.main import favorite_color

def test_welcome_message():
    assert welcome_message("Ammy") == "Ammy, welcome to the Data Engineering course. The course will be a great learning experience!"

def test_favorite_color():
    assert favorite_color("Purple") == "Purple is an amazing color!"