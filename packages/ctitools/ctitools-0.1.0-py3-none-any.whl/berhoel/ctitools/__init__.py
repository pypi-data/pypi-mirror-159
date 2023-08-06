#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Work with cti index files for the Heise papers c't and iX
"""

# Standard library imports.
import re
import argparse
import datetime
from pathlib import Path
from collections import namedtuple

__date__ = "2022/07/19 18:50:56 hoel"
__author__ = "Berthold Höllmann"
__copyright__ = "Copyright © 2022 by Berthold Höllmann"
__credits__ = ["Berthold Höllmann"]
__maintainer__ = "Berthold Höllmann"
__email__ = "berhoel@gmail.com"

try:
    # Local library imports.
    from ._version import __version__
except ImportError:
    __version__ = "0.0.0.invalid0"

MONTH_ISSUE_MAP = {
    1: "Januar",
    2: "Februar",
    3: "März",
    4: "April",
    5: "Mai",
    6: "Juni",
    7: "Juli",
    8: "August",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Dezember",
}


class CTI:
    # Bürokratie: Mit analoger Wucht
    #
    # Tim Gerber
    # tig
    #   3
    # 16
    # c22
    #
    # Standpunkt,Immer in c't,Gesellschaft,Ukraine-Krieg,Ukraine-Hilfe,Digitalisierung,eGovernment,Ukraine-Flüchtlinge

    paper_year = re.compile(r"(?P<paper>[ci])(?P<year>[0-9]{2})")
    paper_map = {"i": "iX", "c": "c't magazin für computertechnik"}

    def __init__(self, infile):
        """Read inoput file.

        infile: inputfile"""
        self.inp = Path(infile)
        self.entries = []
        self._issue_map = None
        with self.inp.open(encoding="cp437") as inp:
            for shorttitle in inp:
                shorttitle = shorttitle.strip()
                title = next(inp).strip()
                author = self.fix_author(next(inp))
                next(inp)  # author shortsign
                pages = int(next(inp).strip())
                issue = int(next(inp).strip())
                info = self.paper_year.match(next(inp).strip()).groupdict()
                journal = info["paper"]
                year = int(info["year"])
                year += 1900 if year > 80 else 2000
                references = next(inp).strip()
                keywords = next(inp).strip()
                {"c": self.add_ct, "i": self.add_ix}[journal](
                    shorttitle,
                    title,
                    author,
                    pages,
                    issue,
                    info,
                    journal,
                    year,
                    references,
                    keywords,
                )

    def add_ix(
        self,
        shorttitle,
        title,
        author,
        pages,
        issue,
        info,
        journal,
        year,
        references,
        keywords,
    ):
        """Add information for a iX issue.

        :param `self`:
        :type self:
        :param `shorttitle`:
        :type shorttitle:
        :param `title`:
        :type title:
        :param `author`:
        :type author:
        :param `pages`:
        :type pages:
        :param `issue`:
        :type issue:
        :param `info`:
        :type info:
        :param `journal`:
        :type journal:
        :param `year`:
        :type year:
        :param `keywords`:
        :type keywords:

        :return:
        :rtype: ``
        """
        if not title:
            shorttitle, title = None, shorttitle
            issue = (
                {
                    2016: "iX Special 2016",
                    2017: "iX Special 2017",
                    2018: "iX Special 2018",
                    2021: "iX Special 2021",
                    2022: "iX Special Green IT",
                }[year]
                if issue > 12
                else MONTH_ISSUE_MAP[issue]
            )
        full_issue = f"{year} / {issue}"

        self.entries.append(
            CTIEntry(
                shorttitle,
                title,
                author,
                pages,
                full_issue,
                info,
                self.paper_map[journal],
                f"{year}-{issue:02}-01",
                references,
                keywords,
            )
        )

    def add_ct(
        self,
        shorttitle,
        title,
        author,
        pages,
        issue,
        info,
        journal,
        year,
        references,
        keywords,
    ):
        """Add information for a c't issue.

        :param `self`:
        :type self:
        :param `shorttitle`:
        :type shorttitle:
        :param `title`:
        :type title:
        :param `author`:
        :type author:
        :param `pages`:
        :type pages:
        :param `issue`:
        :type issue:
        :param `info`:
        :type info:
        :param `journal`:
        :type journal:
        :param `year`:
        :type year:
        :param `keywords`:
        :type keywords:

        :return:
        :rtype: ``
        """
        full_issue = self.year_issue2full_issue(year, issue)
        date = self.issue_map[full_issue]
        if not title:
            shorttitle, title = None, shorttitle
        journaltitle = self.paper_map[journal]

        self.entries.append(
            CTIEntry(
                shorttitle,
                title,
                author,
                pages,
                full_issue,
                info,
                journaltitle,
                date,
                references,
                keywords,
            )
        )

    def year_issue2full_issue(self, year, issue):
        """retrieve full issue for c't from year and issue number.

        :param `yesr`:
        :type year:
        :param `issue`:
        :type issue:
        """
        if year > 2015 and issue == 27:
            issue = "retro"
        if year < 1997 or year == 1997 and issue < 11:
            return f"{year:04d} / {MONTH_ISSUE_MAP[issue]}"
        else:
            return f"{year:04d} / {issue}"

    @property
    def issue_map(self):
        """Generate release dates for c't."""
        if self._issue_map is None:
            diff = datetime.timedelta(days=14)
            date = datetime.datetime(year=2022, month=7, day=16)
            issue = 16
            issue_year = 2022
            self._issue_map = {}

            while date > datetime.datetime(1983, 11, 1):
                key = self.year_issue2full_issue(issue_year, issue)
                self._issue_map[key] = date.strftime("%Y-%m-%d")
                if date < datetime.datetime(1997, 11, 1):
                    year = date.year
                    month = date.month - 1
                    if month < 1:
                        month = 12
                        year -= 1
                    date = datetime.datetime(year, month, 1)
                else:
                    date -= diff
                if date == datetime.datetime(2014, 6, 28):
                    date += datetime.timedelta(days=2)

                issue -= 1
                if issue < 1:
                    issue_year -= 1
                    if issue_year in {2015}:
                        issue = 27
                    elif date < datetime.datetime(1997, 1, 1):
                        issue = 12
                    elif date < datetime.datetime(1998, 1, 5):
                        issue = 16
                    else:
                        issue = 26
                if issue_year == 1997 and issue == 10:
                    date = datetime.datetime(1997, 10, 1)

            for year in range(2018, 2023):
                self._issue_map[f"{year} / retro"] = {
                    2018: "2018-10-23",
                    2019: "2019-10-21",
                    2020: "2020-10-20",
                    2021: "2021-10-19",
                    2022: "2022-1-1",
                }[year]

        return self._issue_map

    @staticmethod
    def fix_author(author):
        """Fix author infoprmation

        :param `author`:
        :type author:

        :return:
        :rtype: ``
        """
        author = author.replace(" und ", ", ")
        author = author.replace("Von Dusan Zivadinovic", "Dušan Živadinović")
        author = author.replace("Duzan", "Dušan")
        author = author.replace("Dusan", "Dušan")
        author = author.replace("Zivadinovic", "Živadinović")
        author = author.replace("Zivadinovi∩c", "Živadinović")
        author = author.replace("Zivadinovi'c", "Živadinović")
        author = author.replace("Zivadanovic", "Živadinović")
        author = author.replace("Zivadinivic", "Živadinović")

        return author.strip().split(",")


CTIEntry = namedtuple(
    "CTIEntry",
    [
        "shorttitle",
        "title",
        "author",
        "pages",
        "issue",
        "info",
        "journaltitle",
        "date",
        "references",
        "keywords",
    ],
)


def main():
    parser = argparse.ArgumentParser("Read cti file.")
    parser.add_argument("cti", type=Path)
    args = parser.parse_args()

    CTI(args.cti)


# Local Variables:
# mode: python
# compile-command: "poetry run tox"
# time-stamp-pattern: "30/__date__ = \"%:y/%02m/%02d %02H:%02M:%02S %u\""
# End:
