#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate pdf from Dilbert png.
"""

from __future__ import annotations, generator_stop

# Standard libraries.
import sys
import subprocess
from string import Template
from pathlib import Path

__date__ = "2022/05/28 17:17:10 hoel"
__author__ = "Berthold Höllmann"
__copyright__ = "Copyright © 2012, 2022 by Berthold Höllmann"
__credits__ = ["Berthold Höllmann"]
__maintainer__ = "Berthold Höllmann"
__email__ = "berhoel@gmail.com"


PATH = Path.home() / "Bilder" / "Dilbert"


def latex(f_name):
    """lualatex --jobname='today'  '\nonstopmode\input{today.tex}'"""
    for _ in range(3):
        pipe = subprocess.Popen(
            [
                "lualatex",
                f"--jobname={f_name}",
                rf"\nonstopmode\input{{{f_name}.tex}}",
            ],
            stdout=subprocess.PIPE,
            cwd=PATH,
        ).stdout
        pipe.read()
    (Path(PATH) / (f"{f_name}.log")).unlink()
    (Path(PATH) / (f"{f_name}.aux")).unlink()
    (Path(PATH) / (f"{f_name}.tex")).unlink()


class DilbertPdf(object):

    """
    >>> tmp = DilbertPdf(2012, 3, 1)
    >>> tmp.year
    2012
    >>> tmp.month
    03
    >>> tmp.day
    01"""

    def __init__(self, year, month, day):
        self.data = dict(year=f"{year:d}", month=f"{month:02d}", day=f"{day:02d}")
        self.template = Template(self.loadTemplate())

    @staticmethod
    def loadTemplate():
        """Load template from file."""
        template_path = Path(__file__).with_name("template.tex")
        return template_path.open("r").read()

    def __call__(self):
        f_name = Template("Daily_Dilbert_$year-$month-$day").substitute(self.data)

        with (PATH / (f"{f_name}.tex")).open("w") as out_f:
            out_f.write(self.template.substitute(self.data))

        latex(f_name)

        return (PATH / f_name).with_suffix(".pdf")


if __name__ == "__main__":
    if len(sys.argv) == 4:
        YEAR, MONTH, DAY = [int(i) for i in sys.argv[1:]]
    else:
        YEAR, MONTH, DAY = (2012, 3, 14)
        print(DilbertPdf(YEAR, MONTH, DAY)())


# Local Variables:
# mode: python
# compile-command: "cd ../../../ && python setup.py test"
# time-stamp-pattern: "30/__date__ = \"%:y/%02m/%02d %02H:%02M:%02S %u\""
# End:
