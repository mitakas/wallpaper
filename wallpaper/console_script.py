import argparse
import time

from . import Cubic


def create_wallpaper():
    current_time = time.strftime('%Y-%m-%d-%H-%M-%S')

    parser = argparse.ArgumentParser(prog='wallpaper')
    parser.add_argument('--width',
                        default=1600, type=int,
                        help='Set the width of the wallpaper.')
    parser.add_argument('--height',
                        default=900, type=int,
                        help='Set the height of the wallpaper.')
    parser.add_argument('--filename', type=str,
                        default='wallpaper-%s.png' % current_time,
                        help='Specify the filename.')
    parser.add_argument('--cube-size',
                        default=50, type=int,
                        help='Choose a size of the cube. Use a common denominator for width and height.')

    args = parser.parse_args()

    w = Cubic(width=args.width, height=args.height, filename=args.filename,
              cube_size=args.cube_size)
    w.paint()


create_wallpaper()
