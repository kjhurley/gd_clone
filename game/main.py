import time
from engine import engine


screen = (1500, 700)

level = engine.SquareOnlyLevel()

win = engine.start(screen, level)
