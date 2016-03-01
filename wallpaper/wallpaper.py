from PIL import Image


class Wallpaper(object):
    """
    Base class for all wallpapers.

    Creates a (very) simple single-color wallpaper.

    Parameters
    ----------
    width: int
    height: int
    filename: str

    Attributes
    ----------
    width: int
    height: int
    filename: str
    image: PIL Image
        The image which holds the wallpaper.

    """
    def __init__(self, width=1600, height=900, filename='wallpaper.png'):
        self.width = width
        self.height = height
        self.filename = filename

    def paint_pattern(self):
        """
        Paints the pattern. The default is just a random color.

        """
        pass

    def paint(self):
        """
        Saves the wallpaper as the specified filename.

        """
        # nice blue color
        self.image = Image.new(mode='RGB', size=(self.width, self.height),
                               color=(47, 98, 135))
        self.paint_pattern()
        self.image.save(fp=self.filename)
