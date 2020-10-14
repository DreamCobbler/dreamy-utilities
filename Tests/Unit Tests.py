####
#
# Dreamy Utilities
# Copyright (C) (2020) Benedykt Synakiewicz <dreamcobbler@outlook.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
####

#
#
#
# Imports.
#
#
#

# Add the package directory to the PATH variable.

import sys

sys.path.insert(0, "../")

# Application.

import dreamy_utilities.Containers
import dreamy_utilities.Filesystem
import dreamy_utilities.HTML
import dreamy_utilities.Mathematics
import dreamy_utilities.Text
import dreamy_utilities.Web

# Standard packages.

from pathlib import Path
import unittest

#
#
#
# Tests.
#
#
#

class TestContainers(unittest.TestCase):

    def test_RemoveDuplicates(self):

        self.assertEqual(
            dreamy_utilities.Containers.RemoveDuplicates(["a", "a", "b", "d", "c", "c", "d", "d"]),
            ["a", "b", "d", "c"]
        )

class TestFilesystem(unittest.TestCase):

    def test_FindFiles(self):

        self.assertEqual(
            dreamy_utilities.Filesystem.FindFiles("./Environment/"),
            [
                Path("Environment/ABC.txt"),
                Path("Environment/A/1.txt"),
                Path("Environment/A/B/2.sql"),
            ]
        )

        self.assertEqual(
            dreamy_utilities.Filesystem.FindFiles("./Environment/", recursive = False),
            [
                Path("Environment/ABC.txt"),
            ]
        )

        self.assertEqual(
            dreamy_utilities.Filesystem.FindFiles("./Environment/", suffixes = [".sql"]),
            [
                Path("Environment/A/B/2.sql"),
            ]
        )

class TestHTML(unittest.TestCase):

    def test_EscapeHTMLEntities(self):

        self.assertEqual(
            dreamy_utilities.HTML.EscapeHTMLEntities("One & Two < Four"),
            "One &amp; Two &lt; Four"
        )

        self.assertEqual(
            dreamy_utilities.HTML.UnescapeHTMLEntities("One & Two &LT; Four"),
            "One & Two < Four"
        )

class TestMathematics(unittest.TestCase):

    def test_GetDimensionsToFit(self):

        self.assertEqual(
            dreamy_utilities.Mathematics.GetDimensionsToFit((300, 300), (1920, 1080)),
            (1080, 1080)
        )

class TestText(unittest.TestCase):

    def test_Bytify(self):

        self.assertEqual(
            dreamy_utilities.Text.Bytify("Test."),
            b"Test."
        )

    def test_DeprettifyAmount(self):

        self.assertEqual(
            dreamy_utilities.Text.DeprettifyAmount("1,036/2,316"),
            (1036, 2316)
        )

    def test_DeprettifyNumber(self):

        self.assertEqual(
            dreamy_utilities.Text.DeprettifyNumber(""),
            0
        )

        self.assertEqual(
            dreamy_utilities.Text.DeprettifyNumber("003"),
            3
        )

        self.assertEqual(
            dreamy_utilities.Text.DeprettifyNumber("1,036"),
            1036
        )

    def test_FillTemplate(self):

        self.assertEqual(
            dreamy_utilities.Text.FillTemplate(
                {"Name": "Ben", "Species": "Human"},
                "My name is @@@Name@@@. I'm a @@@Species@@@."
            ),
            "My name is Ben. I'm a Human."
        )

    def test_GetDateFromTimestamp(self):

        self.assertEqual(
            dreamy_utilities.Text.GetDateFromTimestamp(100000000),
            "1973-03-03"
        )

    def test_GetLevenshteinDistance(self):

        self.assertEqual(
            dreamy_utilities.Text.GetLevenshteinDistance("", ""),
            0
        )

        self.assertEqual(
            dreamy_utilities.Text.GetLevenshteinDistance("", "abcdef"),
            6
        )

        self.assertEqual(
            dreamy_utilities.Text.GetLevenshteinDistance("a", "b"),
            1
        )

        self.assertEqual(
            dreamy_utilities.Text.GetLevenshteinDistance("abcdef", "aXcdef"),
            1
        )

        self.assertEqual(
            dreamy_utilities.Text.GetLevenshteinDistance("ara", "aaaarrr"),
            5
        )

    def test_IsRomanNumeral(self):

        self.assertEqual(
            dreamy_utilities.Text.IsRomanNumeral("I"),
            True
        )

        self.assertEqual(
            dreamy_utilities.Text.IsRomanNumeral("IX"),
            True
        )

        self.assertEqual(
            dreamy_utilities.Text.IsRomanNumeral("MXVI"),
            True
        )

        self.assertEqual(
            dreamy_utilities.Text.IsRomanNumeral("i"),
            False
        )

        self.assertEqual(
            dreamy_utilities.Text.IsRomanNumeral("a"),
            False
        )

        self.assertEqual(
            dreamy_utilities.Text.IsRomanNumeral(""),
            False
        )

    def test_IsStringEmpty(self):

        self.assertEqual(
            dreamy_utilities.Text.IsStringEmpty("a"),
            False
        )

        self.assertEqual(
            dreamy_utilities.Text.IsStringEmpty(""),
            True
        )

        self.assertEqual(
            dreamy_utilities.Text.IsStringEmpty("\t\t"),
            True
        )

        self.assertEqual(
            dreamy_utilities.Text.IsStringEmpty("        "),
            True
        )

    def test_PrettifyDate(self):

        self.assertEqual(
            dreamy_utilities.Text.PrettifyDate("2004-01-01"),
            "Jan 1, 2004"
        )

        self.assertEqual(
            dreamy_utilities.Text.PrettifyDate("01-2004-01", inputFormat = "%M-%Y-%d"),
            "Jan 1, 2004"
        )

    def test_PrettifyNumber(self):

        self.assertEqual(
            dreamy_utilities.Text.PrettifyNumber(0),
            "0"
        )

        self.assertEqual(
            dreamy_utilities.Text.PrettifyNumber(0, isZeroSpecial = True),
            "?"
        )

        self.assertEqual(
            dreamy_utilities.Text.PrettifyNumber(1),
            "1"
        )

        self.assertEqual(
            dreamy_utilities.Text.PrettifyNumber(1000),
            "1,000"
        )

        self.assertEqual(
            dreamy_utilities.Text.PrettifyNumber(0.32400000),
            "0.324"
        )

    def test_Stringify(self):

        self.assertEqual(
            dreamy_utilities.Text.Stringify(None),
            ""
        )

        self.assertEqual(
            dreamy_utilities.Text.Stringify("Test."),
            "Test."
        )

        self.assertEqual(
            dreamy_utilities.Text.Stringify(b'Test.'),
            "Test."
        )

        self.assertEqual(
            dreamy_utilities.Text.Stringify(142),
            "142"
        )

    def test_Truncate(self):

        self.assertEqual(
            dreamy_utilities.Text.Truncate("Lorem ipsum dolor sit amet", 11),
            "Lorem ipsu…"
        )

        self.assertEqual(
            dreamy_utilities.Text.Truncate("Lorem ipsum dolor sit amet", 12),
            "Lorem ipsum…"
        )

        self.assertEqual(
            dreamy_utilities.Text.Truncate("Lorem ipsum dolor sit amet", 13),
            "Lorem ipsum…"
        )

        self.assertEqual(
            dreamy_utilities.Text.Truncate("Lorem ipsum dolor sit amet", 14),
            "Lorem ipsum d…"
        )

class TestWeb(unittest.TestCase):

    def test_GetHostname(self):

        self.assertEqual(
            dreamy_utilities.Web.GetHostname(self._TEST_URL_1),
            "spacebattles.com"
        )

        self.assertEqual(
            dreamy_utilities.Web.GetHostname(self._TEST_URL_2),
            "archiveofourown.org"
        )

        self.assertEqual(
            dreamy_utilities.Web.GetHostname(self._TEST_URL_4),
            "najlepszaerotyka.com.pl"
        )

    def test_GetSiteURL(self):

        self.assertEqual(
            dreamy_utilities.Web.GetSiteURL(self._TEST_URL_1),
            "https://forums.spacebattles.com"
        )

        self.assertEqual(
            dreamy_utilities.Web.GetSiteURL(self._TEST_URL_3),
            "https://harrypotterfanfiction.com"
        )

    _TEST_URL_1 = "https://forums.spacebattles.com/threads/star-wars-a-penumbral-path.814685"
    _TEST_URL_2 = "https://archiveofourown.org/works/25981912/chapters/63166141"
    _TEST_URL_3 = "https://harrypotterfanfiction.com/viewstory.php?psid=327112"
    _TEST_URL_4 = "https://najlepszaerotyka.com.pl/2018/03/01/blondynka-wedug-megasa-alexandrosa/"

#
#
#
# The start-up routine.
#
#
#

unittest.main()