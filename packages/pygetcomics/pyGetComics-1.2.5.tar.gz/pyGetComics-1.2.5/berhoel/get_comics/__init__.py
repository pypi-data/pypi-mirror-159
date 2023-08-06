#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Download various daily comics.
"""

from __future__ import annotations, generator_stop

from . import dilbert, peanuts, garfield

__date__ = "2022/05/28 16:44:35 hoel"
__author__ = "Berthold Höllmann"
__copyright__ = "Copyright © 2017, 2022 by Berthold Höllmann"
__credits__ = ["Berthold Höllmann"]
__maintainer__ = "Berthold Höllmann"
__email__ = "berhoel@gmail.com"


def main():
    """Get all supported comics.
    """
    print("Get Dilbert.")
    dilbert.main()
    print("Get Peanuts.")
    peanuts.main()
    print("Get Garfield.")
    garfield.main()

if __name__ == '__main__':
    main()

# Local Variables:
# mode: python
# compile-command: "cd ../../ && python setup.py test"
# time-stamp-pattern: "30/__date__ = \"%:y/%02m/%02d %02H:%02M:%02S %u\""
# End:
