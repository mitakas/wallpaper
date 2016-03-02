Wallpaper |build-status|
========================

|logo|

This project generates (various) wallpapers using `Python <https://www.python.org/>`_
and `Pillow <https://python-pillow.org/>`_. The  default colorscheme is the `Colorbrewer <http://colorbrewer2.org/>`_
11-class diverging BrBG palette (supplied by `Palettable <https://jiffyclub.github.io/palettable/>`_).

Run ``wallpaper`` in your console to get a PNG image with the name ``wallpaper-<current-time>.png``.

Python 2 and 3 are supported.

Quick Start
===========

Install and run::

    $ pip install wallpaper
    $ wallpaper

Usage
=====

* Creating a wallpaper

  .. code:: python

      from wallpaper import Cubic

      image = Cubic()
      image.paint()

* Implementing your own

  Inherit from ``wallpaper.Wallpaper`` and implement the ``paint_pattern`` function.

TODO
====

* Better color selection

.. |logo| image:: https://raw.githubusercontent.com/mitakas/wallpaper/master/docs/wallpaper.png
    :alt: Logo

.. |build-status| image:: https://travis-ci.org/mitakas/wallpaper.svg?branch=master
    :target: https://travis-ci.org/mitakas/wallpaper
    :alt: Build status
