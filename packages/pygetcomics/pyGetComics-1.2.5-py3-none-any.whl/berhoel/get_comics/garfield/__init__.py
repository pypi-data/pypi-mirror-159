#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Download Garfield comic strips.
"""

from __future__ import annotations, generator_stop

# Standard libraries.
import os
from pathlib import Path

from ..gocomics import GoComics

__date__ = "2022/07/04 23:16:51 hoel"
__author__ = "Berthold Höllmann"
__copyright__ = "Copyright © 2017, 2022 by Berthold Höllmann"
__credits__ = ["Berthold Höllmann"]
__maintainer__ = "Berthold Höllmann"
__email__ = "berhoel@gmail.com"


class Garfield(GoComics):

    "Download daily Garfield comcs fromGoComics."

    # June 19, 1978
    start_year = 1978
    start_month = 6
    start_day = 19

    garfield_path = Path.home() / "Bilder" / "Garfield"

    gif_path_fmt = f'{garfield_path / "%Y" / "%m" / "%d.gif"}'
    png_path_fmt = f'{garfield_path / "%Y" / "%m" / "%d.png"}'
    url_fmt = "http://www.gocomics.com/garfield/%Y/%m/%d"

    statefile_name = garfield_path / "garfield.statfile"


def main():
    "Main Program."
    Garfield()()


if __name__ == "__main__":
    main()

# Local Variables:
# mode: python
# compile-command: "cd ../../../ && python setup.py test"
# time-stamp-pattern: "30/__date__ = \"%:y/%02m/%02d %02H:%02M:%02S %u\""
# End:
