from turtle import *
from winsound import PlaySound

class gif:
    ".gif"

def window(title, size_width, size_height, dark_mode):
    window = Screen()
    window.title(title)
    window.setup(width=size_width, height=size_height)
    if dark_mode == True:
        window.bgcolor("gray")
        while True:
            window.update()
    elif dark_mode == False:
        window.bgcolor("white")
        while True:
            window.update()
    else:
        print(dark_mode + " is not a boolean")

def game(root_player: gif) -> None:
    game = Screen()
    game.addshape(root_player)
    player = Turtle(root_player)

    while True:
        game.update()

def sound(sound_root):
    PlaySound(sound_root)