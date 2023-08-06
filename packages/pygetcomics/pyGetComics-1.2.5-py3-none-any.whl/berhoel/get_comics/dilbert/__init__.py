#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Download Dilberts since Apr 16, 1989.
"""

from __future__ import annotations, generator_stop

# Standard libraries.
import os
import sys
import stat
import os.path
import datetime
import subprocess
from pathlib import Path

# Third party libraries.
import requests
from PIL import ImageFile
from lxml.html import fromstring

from . import day_get

__date__ = "2022/07/18 17:44:12 hoel"
__author__ = "Berthold Höllmann"
__copyright__ = "Copyright © 2011, 2022 by Berthold Höllmann"
__credits__ = ["Berthold Höllmann"]
__maintainer__ = "Berthold Höllmann"
__email__ = "berhoel@gmail.com"

START_YEAR = 1989
START_MONTH = 4
START_DAY = 16

START_DATE = datetime.date(START_YEAR, START_MONTH, START_DAY)

DELTA = datetime.timedelta(days=1)

PNG_PATH_FMT = str(Path.home() / "Bilder" / "Dilbert" / "%Y" / "%m" / "%d.png")
TOUCH_FMT = "%Y%m%d0300"
URL_FMT = "http://dilbert.com/strip/%Y-%m-%d"


def retr_gif(url):
    doc = fromstring(requests.get(url).content)
    url = doc.xpath(".//img[@class='img-responsive img-comic']")[0].get("src")
    if url.startswith("//"):
        url = f"https:{url}"
    return requests.get(url).content


def mk_dir_tree(path):
    """Generate directory including missing upper directories."""
    if not path.is_dir():
        mode = (
            stat.S_ISGID
            | stat.S_IRWXU
            | stat.S_IRGRP
            | stat.S_IXGRP
            | stat.S_IROTH
            | stat.S_IXOTH
        )
        path.mkdir(mode=mode, parents=True)
        path.chmod(mode)


def main():
    """Main routine."""
    cur_date = datetime.date.today()

    mode = stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH

    cnt = 100

    while cur_date >= START_DATE:
        png_path = Path(f"{cur_date:{PNG_PATH_FMT}}")
        try:
            if not png_path.is_file():

                cnt -= 1

                mk_dir_tree(png_path.parent)
                p = ImageFile.Parser()
                p.feed(retr_gif(f"{cur_date:{URL_FMT}}"))
                im = p.close()

                im.save(png_path)

                os.chmod(png_path, mode)

                print(png_path, end=" ")

                process = subprocess.Popen(
                    f"touch -t {cur_date:{TOUCH_FMT}} {png_path}", shell=True
                )
                os.waitpid(process.pid, 0)
                print(day_get.DilbertPdf(cur_date.year, cur_date.month, cur_date.day)())
        except IOError:
            print(
                f"*** Failed to download {cur_date:{URL_FMT}}.",
                file=sys.stderr,
            )

        cur_date -= DELTA
        if cnt < 0:
            break


if __name__ == "__main__":
    main()

# Local Variables:
# mode: python
# compile-command: "cd ../../../ && python setup.py test"
# time-stamp-pattern: "30/__date__ = \"%:y/%02m/%02d %02H:%02M:%02S %u\""
# End:
