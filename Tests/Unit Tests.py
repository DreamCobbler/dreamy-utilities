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

import dreamy_utilities.Text

# Standard packages.

import unittest

#
#
#
# Tests.
#
#
#

class TestText(unittest.TestCase):

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

#
#
#
# The start-up routine.
#
#
#

unittest.main()