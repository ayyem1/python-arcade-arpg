"""

Main entry point for game.

"""

import arcade

from game import game

if __name__ == "__main__":
    arcade.enable_timings()

    game = game.Game()
    game.setup()
    arcade.run()
