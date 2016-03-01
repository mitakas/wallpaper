from wallpaper import Cubic

class TestCubic:
    def test_parameters(self):
        x = Cubic()
        assert x.width == 1600
        assert x.height == 900
        assert x.cube_size == 50
        assert x.filename == 'wallpaper.png'
