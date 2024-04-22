"""

Handles game loop.

"""

import arcade

from game import settings


class Game(arcade.Window):
    def __init__(self) -> None:
        super().__init__(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT, settings.GAME_NAME)

        arcade.set_background_color(arcade.color.AMAZON)

        self.perf_graph_list = None

        self.frame_count = 0

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # Create a sprite list to put the performance graph into
        self.perf_graph_list = arcade.SpriteList()

        # Create the FPS performance graph
        graph = arcade.PerfGraph(settings.GRAPH_WIDTH, settings.GRAPH_HEIGHT, graph_data="FPS")
        graph.center_x = settings.GRAPH_WIDTH / 2
        graph.center_y = self.height - settings.GRAPH_HEIGHT / 2
        self.perf_graph_list.append(graph)

        # Create the on_update graph
        graph = arcade.PerfGraph(settings.GRAPH_WIDTH, settings.GRAPH_HEIGHT, graph_data="on_update")
        graph.center_x = settings.GRAPH_WIDTH / 2 + (settings.GRAPH_WIDTH + settings.GRAPH_MARGIN)
        graph.center_y = self.height - settings.GRAPH_HEIGHT / 2
        self.perf_graph_list.append(graph)

        # Create the on_draw graph
        graph = arcade.PerfGraph(settings.GRAPH_WIDTH, settings.GRAPH_HEIGHT, graph_data="on_draw")
        graph.center_x = settings.GRAPH_WIDTH / 2 + (settings.GRAPH_WIDTH + settings.GRAPH_MARGIN) * 2
        graph.center_y = self.height - settings.GRAPH_HEIGHT / 2
        self.perf_graph_list.append(graph)

    def on_update(self, delta_time: float):
        super().on_update(delta_time)

        if self.frame_count % 60 == 0:
            # arcade.print_timings()
            arcade.clear_timings()

    def on_draw(self):
        """Render the screen."""
        self.clear()

        self.perf_graph_list.draw()

        # Get FPS for the last 60 frames
        text = f"FPS: {arcade.get_fps(60):5.1f}"
        arcade.draw_text(text, settings.SCREEN_WIDTH - 150, 10, arcade.color.BLACK, 22)
