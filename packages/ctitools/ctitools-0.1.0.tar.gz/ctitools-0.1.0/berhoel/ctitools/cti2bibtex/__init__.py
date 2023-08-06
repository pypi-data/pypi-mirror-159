#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Export cti as BiBTeX for Zotero.
"""
# Standard library imports.
import argparse
from pathlib import Path

# Local library imports.
from .. import CTI

__date__ = "2022/07/19 20:52:00 hoel"
__author__ = "Berthold Höllmann"
__copyright__ = "Copyright © 2022 by Berthold Höllmann"
__credits__ = ["Berthold Höllmann"]
__maintainer__ = "Berthold Höllmann"
__email__ = "berhoel@gmail.com"


class BiBTeXEntry:
    def __init__(self, entry):
        """Intitalize

        :param `entry`:
        :type entry:
        """
        self.entry = entry

    def __str__(
        self,
    ):
        """Return string for entry"""
        authors = " and ".join(
            ", ".join(i.split(maxsplit=1)[::-1]) for i in self.entry.author
        )
        papershort = {"c't magazin für computertechnik": "c't"}.get(
            self.entry.journaltitle, self.entry.journaltitle
        )
        res = f"""\
@article{{{self.entry.pages}|{papershort} {self.entry.issue},
  title = {{{self.entry.title}}},"""
        if self.entry.shorttitle is None:
            res = f"""{res}
  shorttitle = {{{self.entry.shorttitle}}},"""
        return f"""{res}
  author = {{{authors}}},
  date = {{{self.entry.date}}},
  journaltitle = {{{self.entry.journaltitle}}},
  pages = {{{self.entry.pages}}},
  issue = {{{self.entry.issue}}},
  keywords = {{{self.entry.keywords}}},
}}
"""


def main():
    parser = argparse.ArgumentParser("Read cti file.")
    parser.add_argument("cti", type=Path)
    parser.add_argument("bibtex", type=Path, nargs="?", default=None)
    args = parser.parse_args()

    cti = CTI(args.cti)

    out = args.cti.with_suffix(".bib") if args.bibtex is None else args.bibtex

    with out.open("w") as outp:
        for entry in cti.entries:
            outp.write(str(BiBTeXEntry(entry)))


# Local Variables:
# mode: python
# compile-command: "poetry run tox"
# time-stamp-pattern: "30/__date__ = \"%:y/%02m/%02d %02H:%02M:%02S %u\""
# End:
