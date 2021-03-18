import numpy as np


class TetrisFigures:
    """This class is responsible for generating and delivering figures to other objects"""

    def __init__(self):
        self.figures: list = []

    def __call__(self):
        return list(self.tetris_figure_factory())

    def tetris_figure_factory(self) -> list:
        """Generating all shapes figures"""
        self.figures.append(np.array([(1, 1, 1, 1)]))
        self.figures.append(np.array([(1, 0, 0), (1, 0, 0), (1, 1, 0)]))
        self.figures.append(np.array([(0, 1, 0), (0, 1, 0), (1, 1, 0)]))
        self.figures.append(np.array([(0, 1, 0), (1, 1, 0), (1, 0, 0)]))
        self.figures.append(np.array([(1, 1, 0), (1, 1, 0)]))
        return self.figures
