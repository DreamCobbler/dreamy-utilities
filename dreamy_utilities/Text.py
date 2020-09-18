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

# Standard packages.

from typing import Any

# Non-standard packages.

from babel.dates import format_date
from babel.numbers import format_number

#
#
#
# Constants.
#
#
#

ValidRomanNumeralCharacters = [
    "I",
    "V",
    "X",
    "L",
    "C",
    "D",
    "M",
]

#
#
#
# Functions.
#
#
#

def FillTemplate(values: Any, template: str) -> str:

    ##
    #
    # Fills in a template string using values coming from an object, or a namespace, or anything
    # else iterable. Variable names in the template string need to be preceded and followed by three
    # "at" signs; example: @@@VariableName@@@.
    #
    # @param values   Iterable values.
    # @param template Template code.
    #
    # @return Template code with variables filled in.
    #
    ##

    availableValues = [x for x in vars(values) if not x.startswith("_")]

    for value in availableValues:
        template = template.replace(
            f"@@@{value}@@@",
            Stringify(getattr(values, value))
        )

    return template

def IsRomanNumeral(text: str) -> bool:

    ##
    #
    # Checks if given string is a Roman numeral.
    #
    # @param text The input string.
    #
    # @return **True** if the string is a Roman numeral, **False** otherwise.
    #
    ##

    if any(x not in ValidRomanNumeralCharacters for x in text.strip()):
        return False

    return True

def IsStringEmpty(text: str) -> bool:

    ##
    #
    # Checks whether a string is empty. A string is considered empty if its length is 0, or when
    # it's composed solely of whitespace, or when it doesn't exist at all.
    #
    # @param text The input string.
    #
    # @return **True** if the string is empty, **False** otherwise.
    #
    ##

    if (not text) or text.isspace():
        return True

    return False

def PrettifyDate(
    date: str,
    inputFormat: str = "%Y-%m-%d",
    locale: str = "en"
) -> str:

    ##
    #
    # Returns a nicely formatted date.
    #
    # @param date        The input date.
    # @param inputFormat The format of the input date.
    # @param locale      The locale to be used for formatting.
    #
    # @return Prettified input date.
    #
    ##

    if "?" == date:
        return date

    return format_date(
        datetime.strptime(date, inputFormat),
        locale = locale
    )

def PrettifyNumber(
    number: int,
    locale: str = "en"
) -> str:

    ##
    #
    # Returns a nicely formatted number.
    #
    # @param number The input number.
    # @param locale The locale to be used for formatting.
    #
    # @return Prettified input number.
    #
    ##

    if 0 == number:
        return "?"

    return format_number(
        number,
        locale = locale
    )

def Stringify(value: Any) -> str:

    ##
    #
    # Converts any value to a string.
    #
    # @param value The input value.
    #
    # @return Stringified input value.
    #
    ##

    if value is None:
        return ""

    elif isinstance(value, str):
        return value

    elif isinstance(value, bytes):
        return value.decode("utf-8")

    else:
        return str(value)

def Truncate(string: str, length: int) -> str:

    ##
    #
    # Truncates a string to given length. Adds ellipsis at the end (if necessary).
    #
    # @param string The string to be truncated.
    # @param length Maximum length of the output string.
    #
    # @return The truncated string.
    #
    ##

    if len(string) <= length:
        return string

    return string[:length - 1].rstrip() + "…"