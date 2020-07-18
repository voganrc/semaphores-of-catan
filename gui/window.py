from PyQt5.QtWidgets import QMainWindow

from gui.drawing.base import DrawingMixin
from gui.mouse.base import MouseMixin


class Window(QMainWindow, DrawingMixin, MouseMixin):

    def __init__(self, gui):
        super().__init__()

        self.gui = gui
        self.game = None

        self.setWindowTitle("Semaphores of Catan")
        self.showMaximized()

        self.setMouseTracking(True)
        self.mouse_x = None
        self.mouse_y = None
        self.mouse_click_drawings = []

    @property
    def center(self):
        return self.width() / 2, self.height() / 2

    def paintEvent(self, event):
        # for drawing in self.mouse_click_drawings + self.mouse_move_drawings():
        #     drawing.apply()
        # for vertex in self.game.board.vertex_grid.elements:
        #     self.draw_vertex(vertex)
        # for edge in self.game.board.edge_grid.elements:
        #     self.draw_edge(edge)
        self.draw_board()
