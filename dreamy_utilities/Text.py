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

from datetime import date, datetime
import re
from typing import Any, List, Optional, Tuple

# Non-standard packages.

from babel.dates import format_date
from babel.numbers import format_decimal
from titlecase import titlecase

#
#
#
# Constants.
#
#
#

VALID_ROMAN_NUMERAL_CHARACTERS = [
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

def Bytify(value: Any) -> bytes:

    ##
    #
    # Converts any value to bytes.
    #
    # @param value The data to be bytified.
    #
    # @return Bytified input value.
    #
    ##

    if value is None:
        return b""

    elif isinstance(value, bytes):
        return value

    else:
        return bytes(value, encoding = "utf-8")

def DeprettifyAmount(amount: str) -> Tuple[int, int]:

    ##
    #
    # Converts an "amount" (i.e. something like "1,036/2,316" to a tuple of integers; in this case
    # it would be (1036, 2316)).
    #
    # @param amount The textual amount.
    #
    # @return A tuple of integers.
    #
    ##

    DEFAULT_RETURN_VALUE = (0, 0)

    if not amount:
        return DEFAULT_RETURN_VALUE

    amount = amount.strip().split("/")
    if len(amount) < 2:
        return DEFAULT_RETURN_VALUE

    return (
        DeprettifyNumber(amount[0]),
        DeprettifyNumber(amount[1])
    )

def DeprettifyNumber(number: str) -> int:

    ##
    #
    # Converts a "pretty" number to integer. (I.e.: "1,036" to 1036).
    #
    # @param number The input number.
    #
    # @return Integer version of the input number.
    #
    ##

    DEFAULT_RETURN_VALUE = 0

    if not number:
        return DEFAULT_RETURN_VALUE

    number = number.strip().replace(",", "")

    try:

        number = int(number)

    except ValueError:

        return DEFAULT_RETURN_VALUE

    return number

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

    valuesDictionary = vars(values) if not isinstance(values, dict) else values
    availableValues = [x for x in valuesDictionary if not x.startswith("_")]

    for value in availableValues:
        template = template.replace(f"@@@{value}@@@", str(valuesDictionary[value]))

    return template

def FindFirstMatch(text: str, expression: str) -> Optional[str]:

    ##
    #
    # Returns the first regular expression match inside text.
    #
    # @param text       The text.
    # @param expression The regular expression.
    #
    # @return The first matching group; optionally **None**.
    #
    ##

    if (not text) or (not expression):
        return None

    match = re.search(expression, text)
    if not match:
        return None

    return match.group(1)

def GetCurrentDate() -> str:

    ##
    #
    # Returns today's date, in ISO 8601 format (YYYY-MM-DD).
    #
    # @return Today's date.
    #
    ##

    return date.today().isoformat()

def GetDateFromTimestamp(timestamp: str) -> str:

    ##
    #
    # Converts Unix timestamp to ISO 8601 date.
    #
    # @param timestamp The input timestamp.
    #
    # @return The input date converted to ISO 8601 date format (YYYY-MM-DD).
    #
    ##

    return date.fromtimestamp(timestamp).isoformat()

def GetLevenshteinDistance(firstString: str, secondString: str) -> int:

    ##
    #
    # Calculates the Levenshtein distance between a pair of strings.
    #
    # @param firstString  The first string.
    # @param secondString The second string.
    #
    # @return The distance between the two strings.
    #
    ##

    if (not firstString) and (not secondString):
        return 0

    sizeH = len(firstString) + 1
    sizeV = len(secondString) + 1

    matrix = [[0 for i in range(sizeV)] for j in range(sizeH)]

    for x in range(sizeH):
        matrix[x][0] = x
    for y in range(sizeV):
        matrix[0][y] = y

    for x in range(1, sizeH):

        for y in range(1, sizeV):

            if firstString[x - 1] == secondString[y - 1]:

                matrix[x][y] = min(
                    matrix[x - 1][y    ] + 1,
                    matrix[x - 1][y - 1]    ,
                    matrix[x    ][y - 1] + 1
                )

            else:

                matrix[x][y] = min(
                    matrix[x - 1][y    ] + 1,
                    matrix[x - 1][y - 1] + 1,
                    matrix[x    ][y - 1] + 1
                )

    return matrix[sizeH - 1][sizeV - 1]

def GetLongestLeadingSubstring(strings: List[str]) -> Optional[str]:

    ##
    #
    # Retrieves the longest leading (i.e. starting) substring from a list of strings.
    #
    # @param strings A list of strings.
    #
    # @return The longest leading substring, or **None**.
    #
    ##

    if not strings:
        return None

    shortestStringLength = 0
    for string in strings:
        shortestStringLength = max(shortestStringLength, len(string))

    if not shortestStringLength:
        return None

    longestLeadingSubstring = ""
    currentCharacter = strings[0][0]

    for characterIndex in range(0, shortestStringLength):

        allStringsMatchCharacter = True

        for string in strings:

            if string[characterIndex] != currentCharacter:
                allStringsMatchCharacter = False
                break

        if not allStringsMatchCharacter:
            break

        longestLeadingSubstring += currentCharacter

        if characterIndex != shortestStringLength - 2:
            currentCharacter = strings[0][characterIndex + 1]

    return longestLeadingSubstring

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

    if (not text) or any(x not in VALID_ROMAN_NUMERAL_CHARACTERS for x in text.strip()):
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
    locale: str = "en",
    isZeroSpecial: bool = False
) -> str:

    ##
    #
    # Returns a nicely formatted number.
    #
    # @param number        The input number.
    # @param locale        The locale to be used for formatting.
    # @param isZeroSpecial Should we replace zero with a question mark (0 -> "?")?
    #
    # @return Prettified input number.
    #
    ##

    if (0 == number) and isZeroSpecial:
        return "?"

    return format_decimal(
        number,
        locale = locale
    )

def PrettifyTitle(title: str, removeContext: bool) -> str:

    ##
    #
    # Returns a prettified title.
    #
    # @param title         The input title.
    # @param removeContext Should we remove the context? (Like "Chapter 3: ".)
    #
    # @return Prettified input title.
    #
    ##

    if not title:
        return title

    if removeContext:

        POSSIBLE_PREFIXES = [
            "Chapter \d+",
            "Ch\. \d+",
            "Update \d+",
            "Part \d+",
        ]

        POSSIBLE_POSTFIXES = [
            "Finale",
            "Final Part",
            "Final Update",
            "Final",
            "Chapter \d+",
            "Ch\. \d+",
            "Update \d+",
            "Part \d+",
        ]

        POSSIBLE_PREFIXES_JOINED = "|".join(POSSIBLE_PREFIXES)
        POSSIBLE_POSTFIXES_JOINED = "|".join(POSSIBLE_POSTFIXES)

        title = re.sub(
            f"^\[?\(?({POSSIBLE_PREFIXES_JOINED}|\d+)\)?\]?:?\.?",
            "",
            title,
            flags = re.IGNORECASE | re.MULTILINE
        )

        title = re.sub(
            f"\(?\[?({POSSIBLE_POSTFIXES_JOINED})\)?\]?$",
            "",
            title,
            flags = re.IGNORECASE | re.MULTILINE
        )

        pass

    title = titlecase(title)
    title = title.strip()

    if IsStringEmpty(title):
        title = ""

    return title

def SeparateSubtitle(title: str) -> Optional[str]:

    ##
    #
    # Retrieves the proper subtitle of the story ("aaa: bbbbb" will return "bbbbb").
    #
    # @param title The title as it was retrieved.
    #
    # @return The subtitle.
    #
    ##

    if not title:
        return None

    subtitle = re.sub("\d+\.+:*", ":", title)
    subtitle = re.sub("\s+-\s+", " : ", subtitle)

    semicolonPosition = subtitle.find(":")
    if -1 != semicolonPosition:
        subtitle = subtitle[semicolonPosition + 1:]

    subtitle = subtitle.strip()

    return subtitle

def Stringify(value: Any, encoding = "utf-8") -> str:

    ##
    #
    # Converts any value to a string.
    #
    # @param value    The input value.
    # @param encoding The expected text encoding.
    #
    # @return Stringified input value.
    #
    ##

    if value is None:
        return ""

    elif isinstance(value, str):
        return value

    elif isinstance(value, bytes):
        return value.decode(encoding, errors = "ignore")

    else:
        return str(value)

def Truncate(string: str, length: int, suffix: str = "…") -> str:

    ##
    #
    # Truncates a string to given length. Adds ellipsis at the end (if necessary).
    #
    # @param string The string to be truncated.
    # @param length Maximum length of the output string.
    # @param suffix The suffix of the output string.
    #
    # @return The truncated string.
    #
    ##

    if len(string) <= length:
        return string

    return string[:length - len(suffix)].rstrip() + suffix

def TruncateByWords(string: str, length: int, suffix: str = "…") -> str:

    ##
    #
    # Truncates a string to given length while trying to avoid cutting words in the middle.
    #
    # @param string The string to be truncated.
    # @param length Maximum length of the output string.
    # @param suffix The suffix of the output string.
    #
    # @return The truncated string.
    #
    ##

    if len(string) <= length:
        return string

    return string[:length - len(suffix)].rsplit(" ", 1)[0] + suffix