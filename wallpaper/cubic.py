import random

from .wallpaper import Wallpaper

from PIL import ImageColor
from PIL import ImageDraw

from palettable.colorbrewer.diverging import BrBG_11


class Cubic(Wallpaper):
    """
    Create a wallpaper consisting of cubes.

    Parameters
    ----------
    width: int
    height: int
    cube_size: int
        Split the image into cubes with some color.
    filename: str

    Attributes
    ----------
    width: int
    height: int
    cube_size: int
        Split the image into cubes with some color.
    filename: str
    image: PIL Image
        The image which holds the wallpaper.

    """
    def __init__(self, width=1600, height=900, filename='wallpaper.png',
                 cube_size=50):
        self.cube_size = cube_size
        super(Cubic, self).__init__(width=width, height=height,
                                    filename=filename)

    def next_color(self):
        """
        Returns the next color. Currently returns a random
        color from the Colorbrewer 11-class diverging BrBG palette.

        Returns
        -------
        next_rgb_color: tuple of ImageColor

        """
        next_rgb_color = ImageColor.getrgb(random.choice(BrBG_11.hex_colors))
        return next_rgb_color

    def paint_cube(self, x, y):
        """
        Paints a cube at a certain position a color.

        Parameters
        ----------
        x: int
            Horizontal position of the upper left corner of the cube.
        y: int
            Vertical position of the upper left corner of the cube.

        """
        # get the color
        color = self.next_color()
        # calculate the position
        cube_pos = [x, y, x + self.cube_size, y + self.cube_size]
        # draw the cube
        draw = ImageDraw.Draw(im=self.image)
        draw.rectangle(xy=cube_pos, fill=color)

    def paint_pattern(self):
        """
        Paints all the cubes.

        """
        x = 0
        while x < self.width:
            y = 0
            while y < self.height:
                self.paint_cube(x, y)
                y += self.cube_size
            x += self.cube_size
