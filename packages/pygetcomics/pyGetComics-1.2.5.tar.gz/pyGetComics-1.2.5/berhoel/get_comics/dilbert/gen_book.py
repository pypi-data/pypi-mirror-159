#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate Book of all Dilbert comics from images.
"""

from __future__ import annotations, generator_stop

# Standard libraries.
import datetime
from pathlib import Path

__date__ = "2022/07/18 17:40:37 hoel"
__author__ = "Berthold Höllmann"
__copyright__ = "Copyright © 2011, 2022 by Berthold Höllmann"
__credits__ = ["Berthold Höllmann"]
__maintainer__ = "Berthold Höllmann"
__email__ = "berhoel@gmail.com"

START_YEAR = 1989
START_MONTH = 4
START_DAY = 16

START_DATE = datetime.date(START_YEAR, START_MONTH, START_DAY)
TODAY = datetime.date.today()

DELTA = datetime.timedelta(days=1)

PATH_FMT = Path("%Y") / "%m" / "%d"


class DilbertBook(object):
    """Generate LaTeX file for Dilbert comic book."""

    def __init__(self, fname):
        self.cur_date = START_DATE
        self.out = file(fname, "w")
        self.grpath = None
        self.outp_done = False

    def run(self):
        """Do the actual processing."""
        self.write_prologue()

        while self.cur_date <= TODAY:
            self.wr_image(self.cur_date)
            if self.cur_date.isoweekday() == 7 and self.outp_done:
                self.outp_done = False
                self.out.write("\\clearpage\n")

            self.cur_date += DELTA

        self.write_epilog()

    def write_prologue(self):
        """Write LaTeX prologue."""
        self.out.write(
            r"""
\documentclass[a4paper,landscape]{book}
\usepackage{graphicx}
\usepackage{textpos}
\usepackage[textwidth=277.0mm,textheight=189.9mm,headsep=1mm]{geometry}
\makeatletter
%\g@addto@macro\Gin@extensions{,.gif}
%\makeatother
%\DeclareGraphicsRule{.gif}{png}{.png}{%
%  `convert '#1' `dirname '#1'`/`basename '#1' .gif`-gif-converted-to.png%
%}
\TPGrid[12mm,12mm]{2}{4}
\setlength{\parindent}{0pt}
\usepackage{fontspec}
\setmainfont{Linux Libertine O}
\begin{document}
"""
        )

    def wr_image(self, date):
        """Write information for including image."""
        path = Path(f"{date:{PATH_FMT}}")
        if path.with_suffix(".png").is_file():
            self.graphicspath(path)
            weekday = date.isoweekday()
            {
                1: self.do_mo,
                2: self.do_di,
                3: self.do_mi,
                4: self.do_do,
                5: self.do_fr,
                6: self.do_sa,
                7: self.do_so,
            }[weekday](path.name)
            self.outp_done = True

    def graphicspath(self, path):
        """Write appropriate Graphicspath information."""
        grpath = path.parent()
        if grpath != self.grpath:
            self.out.write(f"\\graphicspath{{{{{grpath}/}}}} \n")
            self.grpath = grpath

    def do_mo(self, fname):
        "Place Monday figure."
        self.place_img(1, 1, fname, "Mo")

    def do_di(self, fname):
        "Place Tuesday figure."
        self.place_img(1, 2, fname, "Di")

    def do_mi(self, fname):
        "Place Wednesday figure."
        self.place_img(1, 3, fname, "Mi")

    def do_do(self, fname):
        "Place Thursday figure."
        self.place_img(1, 4, fname, "Do")

    def do_fr(self, fname):
        "Place Friday figure."
        self.place_img(2, 1, fname, "Fr")

    def do_sa(self, fname):
        "Place Saturday figure."
        self.place_img(2, 2, fname, "Sa")

    def do_so(self, fname):
        "Place Sunday figure."
        self.place_img(2, 3, fname, "So")

    def place_img(self, x, y, fname, dummy):
        "Place image in grid."
        self.out.write(
            f"""\
\\begin{{textblock}}{{1}}({x-1},{y-1})
  {self.cur_date:%a %d. %B %Y}\\par
  \\centering%%
    \\includegraphics[width=.95\\linewidth]{{{fname}}}
\\end{{textblock}}
"""
        )

    def write_epilog(self):
        "Write LaTeX epilogue."
        self.out.write(
            r"""
\end{document}
"""
        )


def main():
    "Main processing"
    book = DilbertBook(fname="Dilbert_book.tex")
    book.run()


if __name__ == "__main__":
    main()

# Local Variables:
# mode: python
# compile-command: "cd ../../../ && python setup.py test"
# time-stamp-pattern: "30/__date__ = \"%:y/%02m/%02d %02H:%02M:%02S %u\""
# End:
