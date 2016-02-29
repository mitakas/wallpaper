import argparse
import time

from . import Cubic


def create_wallpaper():
    current_time = time.strftime('%Y-%m-%d-%H-%M-%S')

    parser = argparse.ArgumentParser(prog='wallpaper')
    parser.add_argument('--filename',
                        default='wallpaper-%s.png' % current_time,
                        help='Specify the filename.')

    args = parser.parse_args()

    w = Cubic(filename=args.filename)
    w.paint()


create_wallpaper()
