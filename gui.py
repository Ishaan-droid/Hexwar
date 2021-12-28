from tkinter import *

import numpy as np


class GUI:
    def __init__(self, controller):
        self._controller = controller
        self._grid = self._controller._grid

        """ Initializing the window. """
        self._screen = Tk()
        self._screen.title("HexWar")
        #self._screen.resizable(0, 0)
        self._menu = MenuBar(self._screen, self)

        """ Initializing the Canvas containing the maze. """
        self._grid_canvas = Canvas(self._screen, width=int(np.sqrt(3) * 20 * self._grid.get_size()*1.6), height=int(2 * 20 * self._grid.get_size()*0.9))
        self._grid_canvas.pack()

        """ Initializing the command to slow or accelerate the simulation. """
        self._screen.bind("<Up>", self._accelerate)
        self._screen.bind("<Down>", self._slow)
        self._screen.bind("<space>", self._reset_speed)
        self._simulation_speed = 200

        self.stop = False
        self.launch = False
        self._draw()
        self.run()

    def run(self):
        """
        Run the simulation
        """
        while not self.stop:
            if self.launch:
                self._screen.after(self._simulation_speed, self._controller.update())
                self._draw()
                self._screen.update()
                self.check_win()
            else:
                self._screen.after(self._simulation_speed, self._screen.update())

    def check_win(self):
        if self._controller._winner != 0:
            self.launch = False
            Winner(self)

    def _draw(self):
        """
        Draw the game.
        Player one is in red and player two is in blue.
        """
        size_hex = 20
        w = np.sqrt(3) * size_hex
        h = 2 * size_hex
        for x in range(1, self._grid.get_size()+1):
            pos_y = w + (h * 3 / 4) * -1
            pos_x = w / 2 + (-1 * w / 2) + x * w
            self._draw_hex_no_border([pos_x, pos_y], 'blue')
        for x in range(1, self._grid.get_size()+1):
            pos_y = w + (h * 3 / 4) * self._grid.get_size()
            pos_x = w / 2 + (self._grid.get_size() * w / 2) + x * w
            self._draw_hex_no_border([pos_x, pos_y], 'blue')
        for y in range(self._grid.get_size()):
            pos_y = w + (h * 3 / 4) * y
            pos_x = w / 2 + (y * w / 2) + 0 * w
            self._draw_hex_no_border([pos_x, pos_y], 'red')
        for y in range(self._grid.get_size()):
            pos_y = w + (h * 3 / 4) * y
            pos_x = w / 2 + (y * w / 2) + (self._grid.get_size() + 1) * w
            self._draw_hex_no_border([pos_x, pos_y], 'red')

        for y in range(self._grid.get_size()):
            for x in range(1, self._grid.get_size()+1):
                pos_x = w/2 + (y*w/2) + x*w
                pos_y = w + (h*3/4)*y
                color ='grey'
                player = self._grid.get_hex([x-1, y])
                if player == 1:
                    color ='red'
                elif player == 2:
                    color ='blue'
                self._draw_hex([pos_x, pos_y], color)

    def _draw_hex(self, coordinates, color='gray'):
        """
        Draw an hex at a specific location
        :param coordinates: coordinate in the game
        :param color: color of the hex.
        """
        size = 20
        points = []
        for i in range(6):
            angle_deg = 60 * i - 30
            angle_rad = np.pi / 180 * angle_deg
            points.append([coordinates[0] + size * np.cos(angle_rad), coordinates[1] + size * np.sin(angle_rad)])
        self._grid_canvas.create_polygon(points, outline='white', fill=color, width=2)

    def _draw_hex_no_border(self, coordinates, color='gray'):
        size = 20
        points = []
        for i in range(6):
            angle_deg = 60 * i - 30
            angle_rad = np.pi / 180 * angle_deg
            points.append([coordinates[0] + size * np.cos(angle_rad), coordinates[1] + size * np.sin(angle_rad)])
        self._grid_canvas.create_polygon(points, fill=color, width=2)

    def _slow(self, event):
        """Slow the game by adding 250 milliseconds before the next simulation step."""
        self.simulation_speed += 250

    def _accelerate(self, event):
        """Accelerate the game by removing 250 milliseconds before the next simulation step."""
        self.simulation_speed -= 250

    def _reset_speed(self, event):
        """Reset to the default time step."""
        self.simulation_speed = 500


class MenuBar:
    """
    Class representing the MenuBar.
    """
    def __init__(self, window, viewer):
        """
        Initializing the menu
        :param window: The window where the menu bar will be
        :param viewer: the class Viewer
        """
        self.window = window
        self.menu = Menu(self.window)
        self.viewer = viewer

        """ Initializing the menu file """
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="New game", command=self.new_game)
        self.file_menu.add_command(label="Quit", command=self.quit)

        """ Initializing the command menu """
        self.command_menu = Menu(self.menu, tearoff=0)
        self.command_menu.add_command(label="Start", command=self.start)
        self.command_menu.add_command(label="Stop", command=self.stop)

        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.menu.add_cascade(label="Command", menu=self.command_menu)

        self.window.config(menu=self.menu)

    def new_game(self):
        """
        New game
        """
        # Scenario(self.viewer, False)
        pass

    def quit(self):
        """
        Quit the simulation
        """
        self.viewer.stop = True
        pass

    def start(self):
        """
        Start the simulation
        """
        self.viewer.launch = True

    def stop(self):
        """
        Stop the simulation
        """
        self.viewer.launch = False

class Winner(Toplevel):

    def __init__(self, gui, new=True, **kw):
        super().__init__(**kw)
        self.title = "Winner"
        self.gui = gui
        self.new = new

        """ Init spinbox for size of the maze """
        winner = self.gui._controller._winner
        player_name = ""
        if winner == 1:
            player_name = self.gui._controller._player1.name
        if winner == 2:
            player_name = self.gui._controller._player2.name
        Label(self, text=player_name + " wins!").grid(row=0, column=0, columnspan=4)


