from PIL import Image
from wallpaper import wallpaper

class TestWallpaper:
    def test_parameters(self):
        x = wallpaper.Wallpaper()
        assert x.width == 1600
        assert x.height == 900
        assert x.filename == 'wallpaper.png'

    # def test_paint(self, tmpdir):
        # tempfile = tmpdir.mkdir("sub").join('wallpaper.png')
        # x = wallpaper.Wallpaper()
        # x.paint()

        # im = Image.open(fp=tempfile)
        # color = im.getpixel(xy=(0, 0))
        # assert color == (47, 98, 135)
